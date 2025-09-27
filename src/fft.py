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

#Convert numpy array signal to list
def sound_tolist(x):
    if not isinstance(x, list):
        x_list = x.tolist()
        return x_list
    else:
        return x

#Implement FFT without numpy. Divide and conquer Cooley-Tukey algorithm with recursion (radix-2).
#Each sample n in the time-domain sequence "sound" is transformed to frequency / phase component (frequency bin) k in sequence "result".
def fft(x):
    X = [] #FFT output
    N = len(x) #assuming the number of samples in the signal (sequence of samples, list of values) is of power of two
    if N == 1: #base case
        return x
    else:
        x_even = x[::2] #divide the signal in even and odd sample values - samples at indices 0, 2, 4, ...
        x_odd = x[1::2] #samples at indices 1, 3, 5, ...
        X_even = fft(x_even)
        X_odd = fft(x_odd)
        K = [] #frequency component indices
        for k in range(N // 2):
            K.append(k)
        W = [] #twiddle factors wk = e^-2*pi*i*k/n = cos(2*pi*k/n) - i*sin(2*pi*k/n) - unit circle divided in k angles
        for k in K:
            w = complex(math.cos(2 * math.pi * k / N), -math.sin(2 * math.pi * k / N))
            W.append(w)
        N_2 = len(X_even)
        for k in range(N_2): #combine the frequency + phase components k to a sequence "result", which is the FFT output
            X.append(X_even[k] + W[k] * X_odd[k]) #these are the lower frequency bins (0 - N/2)
        for k in range(N_2): 
            X.append(X_even[k] - W[k] * X_odd[k]) # these are the higher frequency bins (N/2 - N-1)
    return X

#Return the lowest peak (fundamental frequency) of FFT magnitude spectrum
def fundamental_frequency_fft(X, fs):
    N = len(X)
    X_pos = X[0:N//2]
    fs = fs
    mags = [abs(x) for x in X_pos]
    freqs = [k / N * fs for k in range(N//2)]
    peak = mags.index(max(mags))
    f0 = freqs[peak]
    return f0

#Return the lowest peak (fundamental frequency) of sound numpy array signal magnitude spectrum
def fundamental_frequency_np(sound, fs):
    sound = sound.ravel()
    fs = fs
    sound_fft = np.abs(np.fft.rfft(sound))
    n = sound.shape[0]
    freq = np.fft.rfftfreq(n, d=1/fs)
    peak = np.argmax(sound_fft)
    f0 = freq[peak]
    return f0
