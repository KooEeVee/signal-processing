import numpy as np
import math

#Numpy fft function
def fft_np(sound):
    #sound = sound.ravel()
    sound_fft = np.fft.fft(sound)
    return sound_fft

#Return the lowest peak (fundamental frequency) of sound numpy array signal magnitude spectrum (real signal input)
def fundamental_frequency_np(sound, fs):
    sound = sound.ravel()
    fs = fs
    sound_fft = np.abs(np.fft.rfft(sound))
    n = sound.shape[0]
    freq = np.fft.rfftfreq(n, d=1/fs)
    peak = np.argmax(sound_fft)
    f0 = freq[peak]
    return f0

#Convert numpy array signal to list
def sound_tolist(x):
    if not isinstance(x, list):
        x_list = x.tolist()
        return x_list
    else:
        return x

#Implement FFT without numpy. Divide and conquer Cooley-Tukey algorithm with recursion (radix-2).
#Each sample n in the time-domain sequence x is transformed to frequency / phase component (frequency bin) k in sequence X.
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
        W = [] #twiddle factors wk = e^-2*pi*i*k/N = cos(2*pi*k/N) - i*sin(2*pi*k/N) --> unit circle divided in k angles
        for k in K:
            w = complex(math.cos(2 * math.pi * k / N), -math.sin(2 * math.pi * k / N))
            W.append(w)
        N_2 = len(X_even)
        for k in range(N_2): #combine the frequency + phase components k to a sequence X, which is the FFT output
            X.append(X_even[k] + W[k] * X_odd[k]) #these are the lower frequency bins (0 - N/2)
        for k in range(N_2): 
            X.append(X_even[k] - W[k] * X_odd[k]) # these are the higher frequency bins (N/2 - N-1)
    return X

#Return the lowest peak (fundamental frequency) of FFT magnitude spectrum (real input signal)
def fundamental_frequency_fft(X, fs):
    N = len(X) #number of samples in FFT output
    X_pos = X[0:N//2] #FFT output positive frequencies
    fs = fs #sampling rate
    mags = [abs(x) for x in X_pos] #magnitudes of FFT output
    freqs = [k / N * fs for k in range(N//2)] #frequencies
    peak = mags.index(max(mags)) #index of the maximum magnitude
    f0 = freqs[peak] #frequency of the maximum magnitude
    return f0