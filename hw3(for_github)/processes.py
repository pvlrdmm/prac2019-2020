import librosa
import librosa.display
import librosa.util
import librosa.feature
import numpy as np
import matplotlib.pyplot as plt
import os
import time
from multiprocessing import Process

path2files =[]
m = []
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

def func(start, end):

    for i in range(start, end):
        audio, sfreq = librosa.load(path2files[i])
        mfccs = librosa.feature.mfcc(audio, sr=sfreq)
        l = path2files[i].rfind('//')
        str_ = curr_dir+ '/np' + path2files[i][l+1:-3] + 'npy'
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
    
    proc1 = Process(target=func, args=(0, lenn//4,))
    proc2 = Process(target=func, args=(lenn//4 +1, lenn//2,))
    proc3 = Process(target=func, args=(lenn//2 + 1,  3*lenn//4,))
    proc4 = Process(target=func, args=(3*lenn//4 + 1,  lenn,))
    
    proc1.start()
    proc2.start()
    proc3.start()
    proc4.start()

    proc1.join()
    proc2.join()
    proc3.join()
    proc4.join()

    print(time.time() - start_time)