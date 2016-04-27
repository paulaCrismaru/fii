from oslo_log import log as logging
import testtools

from tempest import config
from tempest.scenario import manager
from tempest import test
from tempest import exceptions
# from tempest.common.utils.linux import remote_client
from tempest.common import waiters

CONF = config.CONF

LOG = logging.getLogger(__name__)


class TestNew(manager.ScenarioTest):
    """Demo test for LIS training."""

    def setUp(self):
        self.image = CONF.image.hypervisor_name
        if self.image is None:
            raise exceptions("no hypervisor_name")
        elif self.image != "kvm" or self.image != "hyperv":
            raise exceptions("no hyperv or kvm")
        self.user = CONF.validation.image_ssh_user

    def create_and_add_security_group_to_server(self, server):
        secgroup = self._create_security_group()
        self.servers_client.add_security_group(server['id'],
                                               name=secgroup['name'])
        self.addCleanup(self.servers_client.remove_security_group,
                        server['id'], name=secgroup['name'])

        def wait_for_secgroup_add():
            body = (self.servers_client.show_server(server['id'])
                    ['server'])
            return {'name': secgroup['name']} in body['security_groups']

        if not test.call_until_true(wait_for_secgroup_add,
                                    CONF.compute.build_timeout,
                                    CONF.compute.build_interval):
            msg = ('Timed out waiting for adding security group %s to server '
                   '%s' % (secgroup['id'], server['id']))
            raise exceptions.TimeoutException(msg)

    @testtools.skipUnless(CONF.compute_feature_enabled.pause,
                          'Pause is not available.')
    @test.services('compute', 'network')
    def test_mizerie(self):
        keypair = self.create_keypair()
        vm1 = self.create_server(image_id=self.image,
                                 key_name=keypair['name'],
                                 wait_until='ACTIVE')

        vm2 = self.create_server(image_id=self.image,
                                 keyname=keypair['name'],
                                 wait_until='ACTIVE')

        floating_ip1 = self.create_floating_ip(vm1)
        floating_ip2 = self.create_floating_ip(vm1)

        self.create_and_add_security_group_to_server(vm1)
        self.create_and_add_security_group_to_server(vm2)

        self.linux_client = self.get_remote_client(
            floating_ip1['ip'], private_key=keypair['private_key'])

        self.linux_client.ping_host(floating_ip2, 5)
        result = self.linux_client.exec_command("echo $?")
        if result != 0:
            raise exceptions("cannot ping between vms")

        self.servers_client.pause_server(vm1['id'])
        waiters.wait_for_server_status(self.servers_client, vm1['id'],
                                       'PAUSED')
        self.servers_client.unpause_server(vm1['id'])
        waiters.wait_for_server_status(self.servers_client, vm1['id'],
                                       'ACTIVE')

        self.servers_client.reboot_server(vm2['id'], type='SOFT')
        waiters.wait_for_server_status(self.servers_client, vm2['id'],
                                       'ACTIVE')

        self.linux_client.ping_host(floating_ip2, 5)
        result = self.linux_client.exec_command("echo $?")
        if result != 0:
            raise exceptions("cannot ping between vms after reboot/pause")
