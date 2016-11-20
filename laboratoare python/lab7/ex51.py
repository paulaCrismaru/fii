# 5. Sa se creeze doua scripturi care sa comunice intre ele prin date serializate.
# Primul script va salva periodic o lista cu toate fisierele dintr-un director iar
# al doilea script va adauga intr-o arhiva toate fisierele cu size mai mic de 100kb
# si modificate cu cel mult 5 minute in urma (nu va fi adaugat acelasi fisier de 2 ori).

import os
import pickle
import time

def f(path):
    path = os.path.abspath(path)
    if os.path.isdir(path):
        l = [os.path.join(path, item) for item in os.listdir(path)]
        print(l)
        buffer = pickle.dumps(l)
        serialization_path = os.path.abspath("serialization.pickle")
        f = open(serialization_path, 'wb+')
        f.write(buffer)
        f.close()

if __name__ == "__main__":
    while True:
        f("some path")
        time.sleep(5 * 60)
