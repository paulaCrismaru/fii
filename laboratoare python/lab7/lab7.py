import random
import time
# 1. Scrieti un program care la fiecare x secunde unde x va fi
# aleator ales la fiecare iteratie (din intervalul [a, b] , unde
# a, b sunt date ca argumente) afiseaza de cate minute ruleaza
# programul (in minute, cu doua zecimale). Programul va rula la infinit.

def ex1(a, b):
    start = time.time()
    while True:
        x = random.randint(a, b)
        print("x=", x)
        time.sleep(x)
        current_time = time.time()
        print(time.strftime("%M", time.localtime(current_time - start)))

# 2. Scrieti doua functii de verificare daca un numar este prim,
# si verificati care dintre ele este mai eficienta din punct de vedere
# al timpului.

def prim1(x):
    for i in range(2, int(x/2)):
        if x % i == 0:
            return False
    return True

def prim2(x):
    import math
    time.sleep(5)
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

def ex2(x):
    start = time.time()

    start1 = time.time()
    prim1(x)
    stop1 = time.time()

    start2 = time.time()
    prim2(x)
    stop2 = time.time()

    if stop1 - start1 < stop2 - start2:
        print("1")
    elif stop1 - start1 > stop2 - start2:
        print("2")
    else:
        print("both")

    stop = time.time()
    print(stop - start, "seconds")

# 3. Gasiti toate fisierele duplicate dintr-un director dat ca argument si
# afisati timpul de rulare. Calea grupurilor de fisiere duplicate vor fi scrise
# intr-un fisier output.txt.

def ex3(path):
    import os
    import hashlib
    path = os.path.abspath(path)
    d = {}
    if os.path.isdir(path):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            content = open(file_path).read()
            md5_ = hashlib.md5()
            md5_.update(content.encode())
            file_md5 = md5_.hexdigest()
            if file_md5 not in d:
                d[file_md5] = [file_path]
            else:
                d[file_md5].append(file_path)
        f = open("output.txt", "w+")
        for md5 in d:
            if len(d[md5]) > 1:
                for file in d[md5]:
                    f.write(file + "\n")
        f.close()

    else:
        print("not a directory")


# 4. Sa se scrie un script care primeste ca argument un director si
# creeaza un fisier JSON cu date despre toate fisierele din acel director.
# Pentru fiecare fisier vor fi afisate urmatoarele informatii: nume_fisier,
# md5_fisier, sha256_fisier, size_fisier (in bytes), cand a fost creat fisierul
# (in format human-readable) si calea absoluta catre fisier.

def ex4(p):
    import os
    import hashlib
    import json
    d = {}
    p = os.path.abspath(p)
    if os.path.isdir(p):
        for file_name in os.listdir(p):
            file_path = os.path.join(p, file_name)
            info = {}
            info["nume_fisier"] = file_name
            info["md5_fisier"] = hashlib.md5(file_path.encode()).hexdigest()
            info["sha256_fisier"] = hashlib.sha256(file_path.encode()).hexdigest()
            info["size_file"] = os.path.getsize(file_path)
            info["creat_la"] = os.path.getmtime(file_path)
            info["cale_absoluta"] = file_path
            d[file_name] = info
        fd = open(os.path.join(p, "details.json"), 'w+')
        fd.write(json.dumps(d))
        fd.close()

# 5. Sa se creeze doua scripturi care sa comunice intre ele prin date serializate.
# Primul script va salva periodic o lista cu toate fisierele dintr-un director iar
# al doilea script va adauga intr-o arhiva toate fisierele cu size mai mic de 100kb
# si modificate cu cel mult 5 minute in urma (nu va fi adaugat acelasi fisier de 2 ori).

def ex5():
    pass

# 6. Sa se scrie un script care afiseaza in ce zi a saptamanii este anul nou, pentru
# ultimii x ani (x este dat ca argument).
def ex6(a):
    import calendar
    current_year = time.localtime().tm_year
    the_year = current_year - a
    print(the_year)
    print(time.gmtime(the_year))
    # ffs

# 7. Sa se simuleze extragerea 6/49.

def ex7():
    import random
    import time
    bol = [i for i in range(1, 50)]
    for i in range(7):
        random.shuffle(bol)
        time.sleep(2)
        poz = random.randint(0, len(bol)-1)
        print(bol.pop(poz))

