import numpy as np
import fft
import math

def main():
    fs = 1024 #sample rate
    s = 1 #length of sample in seconds
    #sound_list = [5, 3, 2, 1]
    #sound = fft.record_sound(fs, s)
    t = np.linspace(0, s, int(fs * s))
    sound = np.sin(2 * np.pi * 440 * t)
    #sound_samples = []
    #for k in range(n):
    #    sample = math.sin(2 * math.pi * 440 * k / fs)
    #    sound_samples.append(sample)
    #sound = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 2 * 440 * t)
    #sound = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 2 * 440 * t) + 0.25 * np.sin(2 * np.pi * 3 * 440 * t)
    #fft.play_sound(sound, fs)
    #fft.plot_time(sound, fs)
    #fft.plot_freq(sound, fs)
    print(fft.fundamental_frequency_np(sound, fs))
    x = fft.sound_tolist(sound)
    X = fft.fft(x)
    print(fft.fundamental_frequency_fft(X, fs))


if __name__ == "__main__":
    main()