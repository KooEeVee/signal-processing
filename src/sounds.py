import io
import base64
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import librosa


def generate_sine(fs, s, f0):
    """Generate sine wave test signal

    Args:
        fs (int): sampling rate
        s (int): length of signal in seconds
        f0 (int): fundamental frequency

    Returns:
        array: sine wave test signal
    """
    t = np.linspace(0, s, int(fs * s))
    return np.sin(2 * np.pi * f0 * t)


def generate_noisysine(fs, s, f0, noise_amp):
    """Generate sine wave with noise test signal

    Args:
        fs (int): sampling rate
        s (int): length of signal in seconds
        f0 (int): fundamental frequency
        noise_amp (int): noise amplitude

    Returns:
        array: sine wave with noise test signal
    """
    t = np.linspace(0, s, int(fs * s))
    return np.sin(2 * np.pi * f0 * t) + noise_amp * np.random.uniform(-1, 1, len(t)) # type: ignore


def sampling_rate(file):
    """Convert the sampling rate to power of two for fft.fft

    Args:
        file (file): wav file

    Returns:
        array: sound sample with sampling rate 16384 Hz
    """
    x, fs = librosa.load(file, sr=None, mono=True)
    x_sampled = librosa.resample(x, orig_sr=fs, target_sr=16384)
    return x_sampled


def to_note(freq):
    """Convert frequencies to note names

    Args:
        freq (float): frequency Hz

    Returns:
        str: note name
    """
    return librosa.hz_to_note(freq)


def to_freq(note):
    """Convert note names to frequencies

    Args:
        note (_type_): _description_

    Returns:
        _type_: _description_
    """
    return librosa.note_to_hz(note)


def plot_time(sound, fs):
    """Plot numpy array audio signal in time-domain

    Args:
        sound (array): sound sample
        fs (int): sampling rate

    Returns:
        str: plot as a base64-encoded string
    """
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


def plot_time_sines(sound, fs):
    """Plot numpy array sine wave signal in time-domain, zoomed in the first 10 ms

    Args:
        sound (array): sound sample
        fs (int): sampling rate

    Returns:
        str: plot as a base64-encoded string
    """
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


def plot_freq(sound, fs):
    """Plot numpy array audio signal magnitude spectrum in frequency-domain (real signal input)

    Args:
        sound (array): sound sample
        fs (int): sampling rate

    Returns:
        str: plot as a base64-encoded string
    """
    sound = sound.ravel()
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


def plot_freq_sines(sound, fs):
    """Plot numpy array sine wave signal magnitude spectrum in frequency-domain (real signal input), zoomed in the first 2000 Hz

    Args:
        sound (array): sound sample
        fs (int): sampling rate

    Returns:
        str: plot as a base64-encoded string
    """
    sound = sound.ravel()
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
