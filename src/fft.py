import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import math

#Record sound with sounddevice as a numpy array, fs = sample rate, len = length of sound in seconds
def record_sound(fs, s):
    fs = fs
    s = s
    sound = sd.rec(int(s * fs), samplerate=fs, channels=1, dtype="float32")
    sd.wait()
    return sound

#Play sound with sounddevice, sound = numpy array, fs = sample rate
def play_sound(sound, fs):
    fs = fs
    sound = sound
    print(sound.shape)
    sd.play(sound, fs)
    sd.wait()

#Plot sound numpy array signal in time-domain
def plot_time(sound, fs):
    sound = sound
    fs = fs
    n = sound.shape[0]
    s = n / fs
    t = np.linspace(0, s, n)
    plt.plot(t, sound)
    plt.xlabel("time [s]")
    plt.ylabel("amplitude")
    plt.show()

#Plot sound numpy array signal magnitude spectrum in frequency-domain
def plot_freq(sound, fs):
    sound = sound.ravel()
    fs = fs
    sound_fft = np.abs(np.fft.rfft(sound))
    n = sound.shape[0]
    freq = np.fft.rfftfreq(n, d=1/fs)
    plt.plot(freq, sound_fft)
    plt.xlim(0, 5000)
    plt.xlabel("frequency [Hz]")
    plt.ylabel("magnitude")
    plt.show()

#Implement FFT without numpy.
def fft(sound):
    result = []
    n = len(sound)
    if n == 1:
        return sound
    else:
        sound_e = sound[::2]
        sound_o = sound[1::2]
        ye = fft(sound_e)
        yo = fft(sound_o)
        K = []
        for k in range(n // 2):
            K.append(k)
        W = []
        for k in K:
            w = complex(math.cos(2 * math.pi * k / n), -math.sin(2 * math.pi * k / n))
            W.append(w)
        n_half = len(ye)
        for k in range(n_half):
            result.append(ye[k] + W[k] * yo[k])
        for k in range(n_half):
            result.append(ye[k] - W[k] * yo[k])
    # print(f"EVEN: {sound_e}\n")
    # print(f"ODD: {sound_o}\n")
    # print(len(sound_e))
    # print(len(sound_o))
    # print(len(sound))
    return result

#Return the lowest peak (fundamental frequency) of sound numpy array signal magnitude spectrum
def fundamental_frequency(sound, fs):
    sound = sound.ravel()
    fs = fs
    sound_fft = np.abs(np.fft.rfft(sound))
    n = sound.shape[0]
    freq = np.fft.rfftfreq(n, d=1/fs)
    peak = np.argmax(sound_fft)
    f0 = freq[peak]
    return f0
