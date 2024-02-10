import numpy as np
import librosa as librosa


y, sr = librosa.load("gamme_violon.wav")

Y = np.fft.fft(y)