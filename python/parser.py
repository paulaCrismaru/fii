import os
import sys

if __name__ == "__main__":
    for index in xrange(1, len(sys.argv)):
        script = open(sys.argv[index], 'r')
        auxiliary_file = open(sys.argv[index] + ".file", 'w')
        for line in script:
            if len(line) > 82:
                a = line[:len(line) / 2]
                b = line[len(line) / 2:]
                if a.count("\"") % 2 == 1:
                    a += "\""
                    b = "\"" + b
                if not a.count("(") > a.count(")"):
                    b = (1 + a.count("    ")) * "    " + b        
                else:
                    a += " \\" 
                    b = (1 + a.rfind("(")) * " " + b
                auxiliary_file.write(a)
                auxiliary_file.write('\n')
                auxiliary_file.write(b)
            else:
                auxiliary_file.write(line)
        auxiliary_file.close()
        script.close()
        os.system ("copy %s %s" %  (sys.argv[index] + ".file", (sys.argv[index])))
        os.remove(sys.argv[index] + ".file")