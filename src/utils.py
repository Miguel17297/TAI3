import os
import platform
import subprocess
import shutil

ROOT = '/'.join(os.getcwd().split("/")[:-1])
DB_PATH = os.path.join(ROOT, "dataset")
BIN_PATH = os.path.join(ROOT, "bin")
TEMP_PATH = os.path.join(ROOT, "temp")


def applyGetMaxFreqs(filepath):
    """
    Computes the signature (most relevant frequencies) of a music

    Internally uses the module GetMaxFreqs

    :param filepath: path to the music
    :return: music signature
    """

    f_name, f_format = os.path.splitext(filepath)

    freq_file = f"{f_name}.freqs"

    if f_format != ".freqs":  # if already a .freqs file dont need to recompute

        if platform.system().lower() == 'windows':
            p_path = os.path.join(BIN_PATH, "windows", "GetMaxFreqs")  # program path

        else:
            p_path = os.path.join(BIN_PATH, "mac", "GetMaxFreqs")

        subprocess.run([p_path, "-w", freq_file, filepath])

    with open(freq_file, "rb") as f:
        return f.read()


def load_db():
    """
    Loads the musics database
    :return: dict with name of the music and the respective signature
    """

    assert os.path.exists(DB_PATH), 'Invalid Database'

    db = {}

    for music in os.listdir(DB_PATH):
        with open(os.path.join(DB_PATH, music), "rb") as f:
            music_name = os.path.splitext(music)[0]
            db[music_name] = f.read()

    return db


def add_noise(audio, noise, noise_type):
    """
    Add noise to audio file
    :param audio: path to the audio file
    :param noise: amount of noise (-0.4, 0.4)
    :param noise_type: type of noise [whitenoise or brownnoise)
    :return: path to new audio with noise
    """

    assert -0.4 <= noise <= 0.4, 'Noise must be between -0.4 and 0.4'

    if not os.path.exists(TEMP_PATH):  # create temp folder
        os.makedirs(TEMP_PATH)

    audio_path, extension = os.path.splitext(audio)

    audio_name = ''.join([audio_path.split("/")[-1], extension])

    temp_path = os.path.join(TEMP_PATH, audio_name)

    if platform.system().lower() == 'windows':
        p_path = os.path.join(BIN_PATH, "windows", "sox")  # program path

    else:
        p_path = os.path.join(BIN_PATH, "mac", "sox")

    out = subprocess.run(
        [p_path, audio, "-p", "synth", noise_type, "vol", str(noise)], check=True,
        capture_output=True)  # pipe the output

    subprocess.run([p_path, "-m", audio, "-", temp_path], input=out.stdout)

    return temp_path


def clean():
    """
            Delete all files generated during the find music processing
    :return: None
    """

    if os.path.exists(TEMP_PATH):  # delete temporary files if they exist
        shutil.rmtree(TEMP_PATH)


def music_sampling(music):
    return


if __name__ == '__main__':
    print(add_noise("test.wav", 0.4, "whitenoise"))
