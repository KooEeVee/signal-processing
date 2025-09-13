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
    sd.play(sound, fs)
    sd.wait()

#Plot sound numpy array in time-domain
def plot_sound(sound, fs):
    sound = sound
    fs = fs
    n = sound.shape[0]
    len = n / fs
    t = np.linspace(0., len, n)
    plt.plot(t, sound)
    plt.xlabel("time [s]")
    plt.ylabel("amplitude")
    plt.show()