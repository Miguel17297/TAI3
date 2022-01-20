import os
import platform
import subprocess

ROOT = os.getcwd()
DB_PATH = os.path.join(ROOT, "dataset")
BIN_PATH = os.path.join(ROOT, "bin")


# Todo: redirecionar o resultado para uma variavel ou então ler o ficheiro

def applyGetMaxFreqs(filepath):
    assert os.path.exists(filepath), f'Invalid file: {filepath}'

    f_name, f_format = os.path.splitext(filepath)

    freq_file = f"{f_name}.freqs"

    if f_format != ".freqs":  # if already a .freqs file dont need to recompute

        if platform.system().lower() == 'windows':
            f_path = os.path.join(BIN_PATH, "windows", "GetMaxFreqs")
            subprocess.run([f_path, "-w", freq_file, filepath])

        else:
            f_path = os.path.join(BIN_PATH, "mac", "GetMaxFreqs")
            subprocess.run([f_path, "-w", freq_file, filepath])

    with open(freq_file, "rb") as f:
        return f.read()


def load_db():
    assert os.path.exists(DB_PATH), 'Invalid Database'

    db = {}

    for music in os.listdir(DB_PATH):
        with open(os.path.join(DB_PATH, music), "rb") as f:
            music_name = os.path.splitext(music)[0]
            db[music_name] = f.read()

    return db
