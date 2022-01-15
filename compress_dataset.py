import gzip
import subprocess
import os
import platform


def applyGetMaxFreqs(filepath):
    if platform.system().lower() == 'windows':
        res = subprocess.run(["GetMaxFreqs", "-w", f"./dataset/{filepath[0:-4]}.freqs", "./dataset/" + filepath])
        print(res, ' -> ', filepath)
    else:
        #TODOSomeone check if it works for Linux/Mac
        subprocess.run(["GetMaxFreqs", "-w", f"./dataset/{filepath[0:-4]}.freqs", "./dataset/" + filepath])


def main():
    for filepath in os.listdir("./dataset"):
        applyGetMaxFreqs(filepath)


if __name__ == '__main__':
    main()
