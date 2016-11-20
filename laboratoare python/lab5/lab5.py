import os
import platform
import shutil
import stat
import sys

# 1. Scrieti un program python care sa primeasca de la linia de comanda
# doua numere (a si b) si care sa afiseze:
# a) a-b
# b) a+b
# c) a/b
# d) a*b
def ex1():
    a = input("a=")
    b = input("b=")
    try:
        a = int(a)
        b = int(b)

        print("a+b=", a + b)
        print("a-b=", a - b)
        print("a*b=", a * b)
        print("a/b=", a / b)
    except ValueError:
        print("a si b trebuie sa fie numere")


# 2. Scrieti un script care primeste ca parametru de la linia de comanda
# un path si afiseaza primii 4096 bytes daca path-ul duce la un fisier,
# intrarile din acesta daca path-ul reprezinta un director si un mesaj de
# eroare daca path-ul nu este unul valid.

def ex2():
    path = input("path:")
    try:
        if os.path.isdir(path):
            print(os.listdir(path))
        elif os.path.isfile(path):
            file = os.open(path, os.O_RDONLY)
            print(os.read(file, 4096))
    except:
        print("invalid path")

# 3. Scrieti o functie care primeste ca parametru un nume de fisier.
# Aceasta va scrie in fisier datele din os.environ, fiecare linie
# continand cate o intrare din acest dictionar, sub forma cheie [tab] valoare.
def ex3(nume_fisier):
    try:
        file = open(nume_fisier, 'w')
        d = os.environ.copy()
        for item in d:
            file.write(item + "\t" + d[item] + "\n")
            print(item + "\t" + d[item])
        file.close()
    except:
        print("an error occured")


# 4. Scrieti o functie care primeste ca parametru un path ce reprezinta
# un director de pe sistem, parcurge recursiv structura de fisiere si
# directoare pe care acesta le contine si afiseaza in consola toate path-urile
# pe care le-a parcurs. NU aveti voie sa folositi os.walk.
def ex4(path):
    path = os.path.abspath(path)
    if os.path.isdir(path):
        dirs = os.listdir(path)
        for item in dirs:
            print(os.path.join(path, item))
            ex4(item)


# 5. Scrieti un script care primeste 2 parametri de la consola reprezentand
# un path catre un director de pe sistem si un nume de fisier. Scriptul va parcurge recursiv
# structura de fisiere si directoare din directorul dat ca parametru, utilizand os.walk si va
# scrie in fisierul dat ca parametru toate path-urile pe care le-a parcurs si tipul acestuia
# (FILE, DIRECTORY, UNKNOWN), separate de |. Fiecare path va fi scris pe cate o linie.
def ex5():
    path = input("path")
    file_name = input("nume fisier")
    walk = os.walk(path)
    file = open(file_name, "w+")
    for item in walk:
        for folder in item[1]:
            file.write()
        os.path.splitext()
    file.close()

# 6. Scrieti un script care primeste 3 parametri de la consola.
# Primul va fi un path catre un fisier, al doilea un path catre un
# director iar al treilea va fi dimensiunea unui buffer. Scriptul va
# copia fisierul dat ca parametru in directorul dat ca parametru,
# utilizand un buffer de marimea celui de-al treilea parametru, in bytes.

def ex6():
    file = input("file path")
    folder = input("folder path")
    buffer = input("buffer")
    file = os.path.abspath(file)
    file_name = os.path.basename(file)
    file = open(file, 'r')
    folder = os.path.abspath(folder)
    if not os.path.isdir(folder):
        os.mkdir(folder)
    copyed_file = os.path.join(folder, file_name)
    fd = open(copyed_file, 'w+')
    shutil.copyfileobj(file, fd, buffer)
    file.close()
    fd.close()

# 7. Creati-va un modul propriu in care sa implementati cel putin 3
# functii. Utilizati aceste functii intr-un script.
def ex7():
    pass

# 8. Sa se scrie un script care primeste urmatoarele argumente: path,
# tree_depth, filesize , filecount, dircount si care creeaza o structura
# de directoare de adancime depth astfel: incepand din radacina path vor
# fi create dircount directoare si filecount fisiere cu continut de filesize
#  octeti (doar caracterul "a" de exemplu") iar acest proces va fi repetat
# recursiv pentru fiecare director creat pana cand se obtine adancimea dorita
# (in directoarele aflate la adacimea maxima nu se vor crea alte directoare)
def ex8():
    pass

# 9. Sa se creeze un script care afiseaza urmatoarele informatii despre sistem:
# versiunea de python folosita. Daca se foloseste Python 2 va afisa in plus mesajul "=== Python 2 ==="
# iar daca se foloseste Python 3 va afisa in plus mesajul "Running under Py3" (hint: sys.version_info)
# numele user-ului care a executat scriptul,
# path-ul complet al scriptului.
# path-ul directorului in care se afla scriptul,
# tipul sistemului de operare,
# numarul de core-uri,
# directoarele din PATH-ul procesului cate unul pe linie,
def ex9():
    version = sys.version_info.major
    if version == 2:
        print("=== Python {} ===".format(version))
    elif version == 3:
        print("Running under Py3")
    environment_variables = os.environ.copy()
    print("user=", environment_variables['USERNAME'])
    print("path=", os.path.abspath(os.path.curdir))
    print("OS=", platform.uname().system)
    print("cores=", os.cpu_count())
    for path in environment_variables['PATH'].split(";"):
        print(path)

# 10. Sa se scrie o functie search_by_content care primeste ca parametru
# doua siruri de caractere target si to_search si returneaza o lista de
# fisiere care contin to_search. Fisierele se vor cauta astfel: daca target
# este un fisier, se cauta doar in fisierul respectiv iar daca este un director
# se va cauta recursiv in toate fisierele din acel director. Daca target nu este
#  nici fisier nici director, se va arunca o exceptie de tipul ValueError cu un
# mesaj corespunzator.

def ex10():
    pass

# 11. Sa se scrie o functie get_file_info care primeste ca parametru un sir de
#  caractere care reprezinta calea catre un fisier si returneaza un dictionar cu urmatoarele campuri:
# full_path = calea absoluta catre fisier,
# file_size = dimensiunea fisierului in octeti,
# file_extension = extensia fisierului (daca are) sau "",
# can_read si can_write = True/False daca se poate citi din/scrie in fisier.

def ex11(path):
    d = {}
    path = os.path.abspath(path)
    cans = os.stat(path).st_mode
    d["full_path"] = path
    d["file_size"] = os.path.getsize(path)
    _, d["file_extension"] = path.split('.') or None, ""
    d["can_read"] = str(os.O_RDONLY) in str(cans)
    d["can_write"] = str(os.O_WRONLY) in str(cans)
    return d




