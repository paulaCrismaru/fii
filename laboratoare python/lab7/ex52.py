# 5. Sa se creeze doua scripturi care sa comunice intre ele prin date serializate.
# Primul script va salva periodic o lista cu toate fisierele dintr-un director iar
# al doilea script va adauga intr-o arhiva toate fisierele cu size mai mic de 100kb
# si modificate cu cel mult 5 minute in urma (nu va fi adaugat acelasi fisier de 2 ori).
import os
import pickle
import time
import zipfile

def accept_file(path):
    if not os.path.isdir(path):
        print(path)
        path = os.path.abspath(path)
        x = os.stat(path).st_mtime
        mins, sec = divmod(time.time() - os.stat(path).st_mtime, 60)
        print(mins, sec)
        if mins > 5:
            return False
        return True
    return False

def accept_size(path):
    path = os.path.abspath(path)
    size = os.path.getsize(path)
    kbs = size / 1024
    if kbs >= 100:
        return False
    return True

def add_to_archive(archive, pathz):
    pathz = os.path.abspath(pathz)
    archive = os.path.abspath(archive)
    filez = zipfile.ZipFile(archive, 'w')
    if pathz not in filez.filelist:
        filez.write(pathz, os.path.basename(pathz))
    filez.close()

def read_pickle():
    serialization_path = os.path.abspath("serialization.pickle")
    data = pickle.load(open(serialization_path, "rb"))
    return data

if __name__ == "__main__":
    while True:
        data = read_pickle()
        for item in data:
            if accept_file(item) and accept_size(item):
                add_to_archive("some path/archive.zip", item)
        time.sleep(5*60)