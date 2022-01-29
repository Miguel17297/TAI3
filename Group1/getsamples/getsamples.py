import sox
import os
import random

#tfm = sox.Transformer()
# trim the audio between 5 and 10.5 seconds.
#tfm.trim(20, 30)

musics_path="musics/"

samples_path="samples/"

musics = [f for f in os.listdir(os.path.join(os.getcwd(), r'musics')) if f[-4:]==".wav"]

def obtain_samples(music,musics_path,samples_path):
    sample_size=[10,20,30]
    for size in sample_size:
        tfm = sox.Transformer()
        duration=sox.file_info.duration(musics_path+music)
        randomstart=random.uniform(0,duration-size)
        tfm.trim(randomstart,randomstart+size)
        tfm.build_file(musics_path+music, f"{samples_path}{music[:-4]}_sample{size}.wav")
        print(music[:-4])
        print("Done!")

for music in musics:
    obtain_samples(music,musics_path,samples_path)
