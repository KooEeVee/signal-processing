import numpy as np
import math


def fft_np(sound):
    """Numpy fft function

    Args:
        sound (array): sound sample

    Returns:
        array: array of complex numbers of the same length as sound, each element corresponds to a frequency bin
    """
    sound_fft = np.fft.fft(sound)
    return sound_fft


def fundamental_frequency_np(sound, fs):
    """Return the lowest peak (fundamental frequency) of numpy array signal magnitude spectrum (real signal input)

    Args:
        sound (array): sound sample
        fs (int): sampling rate

    Returns:
        float: fundamental frequency
    """
    sound = sound.ravel()
    fs = fs
    sound_fft = np.abs(np.fft.rfft(sound))
    n = sound.shape[0]
    freq = np.fft.rfftfreq(n, d=1/fs)
    peak = np.argmax(sound_fft)
    f0 = freq[peak]
    return f0


def sound_tolist(x):
    """Convert numpy array signal to list

    Args:
        x (array): sound sample

    Returns:
        list: sound sample
    """
    if not isinstance(x, list):
        x_list = x.tolist()
        return x_list
    else:
        return x


def fft(x):
    """Implement FFT without numpy. Divide and conquer Cooley-Tukey algorithm with recursion (radix-2).
    Samples n in the time-domain sequence x are transformed to frequency / phase component (frequency bin) k in sequence X.

    Args:
        x (list): sound sample

    Returns:
        list: list of complex numbers of the same length as x, each element corresponds to a frequency bin
    """
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
        W = [] #twiddle factors wk = e^-2*pi*i*k/N = cos(2*pi*k/N) - i*sin(2*pi*k/N) --> complex plane unit circle divided in k angles
        for k in K:
            w = complex(math.cos(2 * math.pi * k / N), -math.sin(2 * math.pi * k / N))
            W.append(w)
        N_2 = len(X_even)
        for k in range(N_2): #combine the frequency + phase components k to a sequence X, which is the FFT output
            X.append(X_even[k] + W[k] * X_odd[k]) #these are frequency bins 0 --> N/2
        for k in range(N_2): 
            X.append(X_even[k] - W[k] * X_odd[k]) #these are the frequency bins N/2 --> N-1
    return X


def fundamental_frequency_fft(X, fs):
    """Return the lowest peak (fundamental frequency) of fft magnitude spectrum (real input signal)

    Args:
        X (list): fft function output
        fs (int): sampling rate

    Returns:
        float: fundamental frequency
    """
    N = len(X) #number of samples in fft output
    X_pos = X[0:N//2] #fft output positive frequencies
    fs = fs #sampling rate
    mags = [abs(x) for x in X_pos] #magnitudes of fft output
    freqs = [k / N * fs for k in range(N//2)] #frequencies
    peak = mags.index(max(mags)) #index of the maximum magnitude
    f0 = freqs[peak] #frequency of the maximum magnitude
    return f0