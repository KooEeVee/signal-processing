import numpy as np
import librosa

#Generate test signal, fs = sampling rate, s = length of signal in seconds, f0 = fundamental frequency
def generate_sine(fs, s, f0):
    fs = fs
    s = s
    f0 = f0
    t = np.linspace(0, s, int(fs * s))
    return np.sin(2 * np.pi * f0 * t)

#Generate test signal, fs = sampling rate, s = length of signal in seconds, f0 = fundamental frequency, noise_amp = noise amplitude
def generate_noisysine(fs, s, f0, noise_amp):
    fs = fs
    s = s
    f0 = f0
    t = np.linspace(0, s, int(fs * s))
    return np.sin(2 * np.pi * f0 * t) + noise_amp * np.random.uniform(-1, 1, len(t)) # type: ignore

#Convert frequencies to notes
def to_note(freq):
    freq = freq
    return librosa.hz_to_note(freq)