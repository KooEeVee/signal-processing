
import fft

def main():
    fs = 44100
    len = 3
    sound = fft.record_sound(fs, len)
    fft.play_sound(sound, fs)
    fft.plot_sound(sound, fs)

if __name__ == "__main__":
    main()