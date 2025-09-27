import numpy as np
import fft
import math

def main():
    fs = 1024 #sampling rate
    s = 2 #length of sample sequence in seconds
    #sound = fft.record_sound(fs, s)
    t = np.linspace(0, s, int(fs * s))
    sound = np.sin(2 * np.pi * 440 * t)
    noisy_sound = np.sin(2 * np.pi * 440 * t) + 0.5 * np.random.uniform(-1, 1, len(t))
    fft.plot_time(noisy_sound, fs)
    fft.plot_freq(noisy_sound, fs)
    print(fft.fundamental_frequency_np(noisy_sound, fs))
    x = fft.sound_tolist(noisy_sound)
    X = fft.fft(x)
    print(fft.fundamental_frequency_fft(X, fs))
    fft.play_sound(sound, fs)
    fft.plot_time(sound, fs)
    fft.plot_freq(sound, fs)
    print(fft.fundamental_frequency_np(sound, fs))
    x = fft.sound_tolist(sound)
    X = fft.fft(x)
    print(fft.fundamental_frequency_fft(X, fs))


if __name__ == "__main__":
    main()