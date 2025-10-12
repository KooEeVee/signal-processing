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

#Convert the sampling rate to power of two for fft.fft
def sampling_rate(file):
    x, fs = librosa.load(file, sr=None, mono=True)
    print(len(x))
    print(fs)
    x_sampled = librosa.resample(x, orig_sr=fs, target_sr=16384)
    print()
    return x_sampled

#Convert frequencies to note names
def to_note(freq):
    freq = freq
    return librosa.hz_to_note(freq)

#Convert note names to frequencies
def to_freq(note):
    note = note
    return librosa.note_to_hz(note)

#Plot sound numpy array audio signal in time-domain
def plot_time(sound, fs):
    sound = sound
    fs = fs
    n = sound.shape[0]
    s = n / fs
    t = np.linspace(0, s, n)
    sound = sound / np.max(np.abs(sound))
    plt.figure()
    plt.plot(t, sound)
    plt.title("Time-domain signal")
    plt.xlabel("time [s]")
    plt.ylabel("amplitude")
    plt.xlim(0, t[-1])
    #plt.show()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode("ascii")
    plt.close()
    return image_base64

#Plot sound numpy array sine wave signal in time-domain
def plot_time_sines(sound, fs):
    sound = sound
    fs = fs
    n = sound.shape[0]
    s = n / fs
    t = np.linspace(0, s, n)
    sound = sound / np.max(np.abs(sound))
    plt.figure()
    plt.plot(t, sound)
    plt.title("Time-domain signal")
    plt.xlabel("time [s]")
    plt.ylabel("amplitude")
    plt.xlim(0, 0.01)
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
    sound_fft /= np.max(sound_fft)
    n = sound.shape[0]
    freq = np.fft.rfftfreq(n, d=1/fs)
    plt.figure()
    plt.plot(freq, sound_fft)
    plt.title("Frequency spectrum")
    plt.xlabel("frequency [Hz]")
    plt.ylabel("magnitude")
    plt.xlim(0, freq[-1])
    #plt.show()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode("ascii")
    plt.close()
    return image_base64

#Plot sound numpy array signal magnitude spectrum in frequency-domain (real signal input)
def plot_freq_sines(sound, fs):
    sound = sound.ravel()
    fs = fs
    sound_fft = np.abs(np.fft.rfft(sound))
    sound_fft /= np.max(sound_fft)
    n = sound.shape[0]
    freq = np.fft.rfftfreq(n, d=1/fs)
    plt.figure()
    plt.plot(freq, sound_fft)
    plt.title("Frequency spectrum")
    plt.xlabel("frequency [Hz]")
    plt.ylabel("magnitude")
    plt.xlim(0, 2000)
    #plt.show()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode("ascii")
    plt.close()
    return image_base64