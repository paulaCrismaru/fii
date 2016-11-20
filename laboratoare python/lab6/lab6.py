import re

# 1. Sa se scrie o functie care extrage cuvintele dintr-un text dat ca parametru.
# Un cuvant este definit ca o secventa de caractere alfa-numerice.

def ex1(text):
    results = re.search("[\w\d]*", text)
    for item in results:
        print(item)

# 2. Sa se scrie o functie care primeste ca parametru un sir de caractere regex,
# un sir de caractere text si un numar intreg x si returneaza acele substring-uri
# de lungime maxim x care fac match pe expresia regulata data.

def ex2(regex, string, number):
    results = re.search(regex, string)
    print(type(results))
    # for item in results:
        # if len(item) > number:
            # results.

# 3. Sa se scrie o functie care primeste ca parametru un sir de caractere
#  text si o lista de expresii regulate si returneaza o lista de siruri de
# caractere care fac match pe cel putin o expresie regulata daca ca parametru.

def ex3(text, regs):
    l = []
    for reg in regs:
        p = re.compile(reg)
        r = re.match(p, text)

# 4. Sa se scrie o functie care primeste ca parametru path-ul catre un
# document xml si un dictionar attrs si returneaza acele elemente care
# au ca atribute toate cheile din dictionar si ca valoare valorile corespunzatoare.
# De exemplu, pentru dictionarul {"class": "url", "name": "url-form", "data-id": "item"}
# se vor selecta elementele care au atributele: class="url" si name="url-form" si data-id="item".

def ex4():
    pass

# 5. Sa se scrie o alta varianta a functiei de la exercitiul anterior care
# returneaza acele elemente care au cel putin un atribut care corespunde cu
# o pereche cheie-valoare din dictionar.
def ex5():
    pass

# 6. Sa se scrie o functie care pentru un text dat ca parametru, cenzureaza
# cuvintele care incep si se termina cu vocale. Prin cenzurare se intelege
# inlocuirea caracterelor de pe pozitii impare cu caracterul * .

def ex6():
    pass

# 7. Sa se verifice, folosind o expresie regulata, daca un sir de caractere reprezinta un CNP valid.
def ex7(cnp):
    reg = "[1-6][0-9][0-9][0-1][0-9]"

# 8. Sa se scrie o functie care parcurge recursiv un director si afiseaza acele fisiere a caror
# nume face match pe o expresie regulata data ca parametru sau contine un sir de caractere
# care face match pe aceeasi expresie. Fisierele care satisfac ambele conditii vor fi afisate
# prefixate cu ">>"
def ex8():
    pass