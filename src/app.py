import numpy as np
import fft

def main():
    fs = 44100
    len = 3
    #sound = fft.record_sound(fs, len)
    t = np.linspace(0, len, int(fs * len))
    #sound = np.sin(2 * np.pi * 440 * t)
    #sound = np.sin(2 * np.pi * 440 * t)+ 0.5*np.sin(2 * np.pi * 2 * 440 * t)
    sound = np.sin(2 * np.pi * 440 * t)+ 0.5 * np.sin(2 * np.pi * 2 * 440 * t) + 0.25 * np.sin(2 * np.pi * 3 * 440 * t)
    fft.play_sound(sound, fs)
    #fft.plot_time(sound, fs)
    fft.plot_freq(sound, fs)
    print(fft.fundamental_frequency(sound, fs))

if __name__ == "__main__":
    main()