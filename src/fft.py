import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

#Record sound with sounddevice as a numpy array, fs = sample rate, len = length of sound in seconds
def record_sound(fs, len):
    fs = fs
    len = len
    sound = sd.rec(int(len * fs), samplerate=fs, channels=1, dtype="float32")
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
    len = n / fs
    t = np.linspace(0, len, n)
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
