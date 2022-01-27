import gzip
import subprocess
import os
import platform

ROOT = os.path.join(os.getcwd(), "../bin")


def applyGetMaxFreqs(filepath):
    if platform.system().lower() == 'windows':
        f_path = os.path.join(ROOT, "windows", "GetMaxFreqs")
        return subprocess.run([f_path, "-w", f"./dataset/{filepath[0:-4]}.freqs", "./dataset/" + filepath])

    else:
        # TODOSomeone check if it works for Linux/Mac
        f_path = os.path.join(ROOT, "mac", "GetMaxFreqs")
        return subprocess.run([f_path, "-w", f"./dataset/{filepath[0:-4]}.freqs", "./dataset/" + filepath])


def main():
    for filepath in os.listdir("../dataset"):
        applyGetMaxFreqs(filepath)


if __name__ == '__main__':
    main()
