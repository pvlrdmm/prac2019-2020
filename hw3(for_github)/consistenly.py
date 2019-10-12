import librosa
import librosa.display
import librosa.util
import librosa.feature
import numpy as np
import matplotlib.pyplot as plt
import os
import time

path2files =[]
f = 0
lenn = 0

def GetFiles(path):
    tmp = [] 
    for i in os.walk(path):
        tmp.append(i)

    for address, dirs, files in tmp:
        for file in files:
            path2files.append(address+'/'+file)

    return path2files

def func():
    for file in path2files:
        audio, sfreq = librosa.load(file)
        mfccs = librosa.feature.mfcc(audio, sr=sfreq)
        l = file.rfind('//')
        str_ = curr_dir+ '/np' + file[l+1:-3] + 'npy'
        k = str_.rfind('/')
        n = len(str_) - k
        if not os.path.exists(str_[:-n]):
            os.makedirs(str_[:-n])
        filename = str_[k+1:] 
        filepath = os.path.join(str_[:-n], filename)
        f = open(filepath, 'w')
        mfccs_str = str (mfccs)
        f.write(mfccs_str)
        f.close


if __name__ == '__main__':
    start_time = time.time()
    curr_dir = os.path.abspath(os.curdir)
    dir2read =  curr_dir +'/wav//'
    GetFiles(dir2read)
    path2files = np.asarray(path2files)
    lenn = len(path2files)
    print(lenn)
    func()
    print(time.time() - start_time)
