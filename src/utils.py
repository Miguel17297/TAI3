import os
import platform
import subprocess

ROOT = os.getcwd()
DB_PATH = os.path.join(ROOT, "dataset")
BIN_PATH = os.path.join(ROOT, "bin")

# Todo: redirecionar o resultado para uma variavel ou então ler o ficheiro

def applyGetMaxFreqs(filepath):
    if platform.system().lower() == 'windows':
        f_path = os.path.join(BIN_PATH, "windows", "GetMaxFreqs")
        return subprocess.run([f_path, "-w", f"./dataset/{filepath[0:-4]}.freqs", "./dataset/" + filepath])

    else:
        # TODOSomeone check if it works for Linux/Mac
        f_path = os.path.join(BIN_PATH, "mac", "GetMaxFreqs")
        return subprocess.run([f_path, "-w", f"./dataset/{filepath[0:-4]}.freqs", "./dataset/" + filepath])


def load_db():
    assert os.path.exists(DB_PATH), 'Invalid Database'

    db = {}

    for music in os.listdir(DB_PATH):
        with open(os.path.join(DB_PATH, music), "rb") as f:
            music_name = os.path.splitext(music)[0]
            db[music_name] = f.read()

    return db

