import numpy as np
import sounddevice as sd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import librosa
import io
import base64

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

#Convert frequencies to note names
def to_note(freq):
    freq = freq
    return librosa.hz_to_note(freq)

#Convert note names to frequencies
def to_freq(note):
    note = note
    return librosa.note_to_hz(note)

#Record sound with sounddevice as a numpy array, fs = sampling rate, s = length of sound in seconds
def record_sound(fs, s):
    fs = fs
    s = s
    sound = sd.rec(int(s * fs), samplerate=fs, channels=1, dtype="float32")
    sd.wait()
    return sound

#Play sound with sounddevice, sound = numpy array, fs = sampling rate
def play_sound(sound, fs):
    fs = fs
    sound = sound
    sd.play(sound, fs)

#Plot sound numpy array signal in time-domain
def plot_time(sound, fs):
    sound = sound
    fs = fs
    n = sound.shape[0]
    s = n / fs
    t = np.linspace(0, s, n)
    plt.figure()
    plt.plot(t, sound)
    plt.title("Time-domain signal")
    plt.xlabel("time [s]")
    plt.ylabel("amplitude")
    #plt.show()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode("ascii")
    plt.close()
    return image_base64
    

#Plot sound numpy array signal magnitude spectrum in frequency-domain (real signal input)
def plot_freq(sound, fs):
    sound = sound.ravel()
    fs = fs
    sound_fft = np.abs(np.fft.rfft(sound))
    n = sound.shape[0]
    freq = np.fft.rfftfreq(n, d=1/fs)
    plt.figure()
    plt.plot(freq, sound_fft)
    plt.title("Frequency spectrum")
    #plt.xlim(0, 5000)
    plt.xlabel("frequency [Hz]")
    plt.ylabel("magnitude")
    #plt.show()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode("ascii")
    plt.close()
    return image_base64