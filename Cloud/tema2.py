import cherrypy
import json
import urllib2
from bs4 import BeautifulSoup

def clean_text(text):
    text = text.replace("\t", "")
    text = text.replace("\n", "")
    text = text.replace("\r", "")
    return text



class Concerts:

    exposed = True

    def __init__(self):
        self.concerts = self.create_json()

    def GET(self, id=None, oras=None, stil=None):
        if id is None and oras is None and stil is None:
            return json.dumps(self.concerts)
        elif oras is None and stil is None: #numai id
            if id in self.concerts.keys():
                concert = self.concerts[id]
                return json.dumps(concert)
            else:
                return('Niciun concert cu ID %s' % id)
        elif id is None and stil is None: #numai oras
            oras = oras.encode('UTF-8')
            lista = {}
            for id in self.concerts:
                if self.concerts.get(id).get('oras') != None:
                    o = self.concerts.get(id).get('oras').encode('UTF-8')
                    if o.lower() == oras.lower():
                        i = str(len(lista) + 1)
                        lista[i] = self.concerts[id]
            return json.dumps(lista)
        elif id is None and oras is None: #numai stil
            stil = stil.encode('UTF-8')
            lista = {}
            for id in self.concerts:
                if self.concerts.get(id).get('stil') != None:
                    s = self.concerts.get(id).get('stil').encode('UTF-8')
                    if s.lower() == stil.lower():
                        i = str(len(lista) + 1)
                        lista[i] = self.concerts[id]
            return json.dumps(lista)
        elif id is None: # oras si stil
            stil = stil.encode('UTF-8')
            lista = {}
            for id in self.concerts:
                if self.concerts.get(id).get('stil') != None and self.concerts.get(id).get('oras') != None:
                    s = self.concerts.get(id).get('stil').encode('UTF-8')
                    o = self.concerts.get(id).get('oras').encode('UTF-8')
                    if o.lower() == oras.lower() and s.lower() == stil.lower():
                        lista[id] = self.concerts[id]
            return json.dumps(lista)


    def POST(self, nume, oras, locatie, data, stil):

        id = str(max([int(_) for _ in self.concerts.keys()]) + 1)

        self.concerts[id] = {
            'nume'    : nume,
            'oras'    : oras,
            'locatie' : locatie,
            'data'    : data,
            'stil'    : stil
        }
        return ('S-a creat concertul cu ID: %s' % id)

    def PUT(self, id, nume=None, data=None):
        id = str(id)
        if id in self.concerts:
            concert = self.concerts.get(id)

            concert['nume'] = nume or self.concerts.get(id)['nume']
            concert['data'] = data or self.concerts.get(id)['data']
            return json.dumps(concert)
        else:
            return('Nu exista niciun concert cu ID %s' % id)

    def DELETE(self, id):
        id = str(id)
        if id in self.concerts:
            self.concerts.pop(id)
            return('Concertul cu ID %s a fost sters.' % id)
        else:
            return('Nu exista niciun concert cu ID %s' % id)

    def create_json(self):
        url = "http://www.metalhead.ro/concerte"
        page  = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        concerts = {}
        #{'id':{'nume':'','oras':'','locatie':'','data':'','stil':''}}
        divs = soup.find_all('div')
        for div in divs:
            if div.get('class') == ['un_eveniment', 'vevent']:
                i = str(len(concerts) + 1)
                concerts[i] = {}
                for span in div.find_all('span'):
                    if len(span) > 1:
                        if span.get('class') == [u'dtstart']:
                            text = ''.join(span.find_all(text=True)[0].encode('UTF-8'))
                            text = clean_text(text)
                            concerts[i]['data'] = text
                        elif span.get('class') == [u'location'] or span.get('class') == [u' location']:
                            concerts[i]['locatie'] = ''.join(span.find_all(text=True)[1].encode('UTF-8'))
                            concerts[i]['oras'] =  ''.join(span.find_all(text=True)[3].encode('UTF-8'))
                        elif clean_text(span.find_all(text=True)[0].encode('UTF-8')) == "Stiluri: ":
                            concerts[i]['stil'] = span.find_all(text=True)[1].encode('UTF-8')
                for d in div.find_all('div'):
                    for h in d.find_all('h2'):
                        concerts[i]['nume'] = ''.join(h.find_all(text=True)[0].encode('UTF-8'))
        return concerts

if __name__ == '__main__':
    cherrypy.tree.mount(
        Concerts(), '/api/concerts',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
         }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
