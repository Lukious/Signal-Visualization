import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import librosa
import librosa.display
import pywt
import pywt.data

#filename = input("Input ecg file name:")
#ecg_filename = filename
ecg_filename = "208_data"
ecg_raw_data = pd.read_csv("./"+ecg_filename+".csv")
data = pd.DataFrame(ecg_raw_data,columns=["f_ml","f_v1","ml","v1"])
ecg_use_data = pd.DataFrame(data,columns=["f_ml"])

ecg_test=ecg_use_data.to_numpy()
ecgcutter = ecg_test[0:1000]







"""
D = np.abs(librosa.stft(ecgcutter))
librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), y_axis='linear', x_axis='time')
plt.title('Dual Tone')
plt.ylim(0, 4000)
plt.show()
"""



'''
fs = 10e3
amp = 2 * np.sqrt(2)


t, f, Zxx = signal.stft(ecg_use_data, fs, nperseg=1000)
plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp)
'''