import numpy as np
import fft
import sounds

def main():

    #Define the test signal
    fs = 1024 #sampling rate, assuming power of two, no need to change this
    s = 2 #length of sample sequence in seconds, assuming power of two, no need to change this
    #freq = 440 #update the pitch value "440", if you want to use Hz as parameter
    freq = sounds.to_freq("F4") #update the pitch value "F4", if you want to use the note name as parameter 
    noise_amp = 10 #update the noise amplitude value to amplify or attenuate noise

    sound = sounds.generate_sine(fs, s, freq)
    noisy_sound = sounds.generate_noisysine(fs, s, freq, noise_amp)
    #sound = sounds.record_sound(fs, s) #doesn't work

    #Plot and listen to test signals
    sounds.play_sound(sound, fs)
    sounds.plot_time(sound, fs)
    sounds.plot_freq(sound, fs)

    sounds.play_sound(noisy_sound, fs)
    sounds.plot_time(noisy_sound, fs)
    sounds.plot_freq(noisy_sound, fs)

    #Testing numpy fft.rfft function
    f0 = fft.fundamental_frequency_np(sound, fs)
    note = sounds.to_note(f0)
    print(f"Fundamental frequency using np.fft.rfft: {f0}, note {note}")
    
    f0 = fft.fundamental_frequency_np(noisy_sound, fs)
    note = sounds.to_note(f0)
    print(f"Fundamental frequency using np.fft.rfft: {f0}, note {note}")

    #Testing fft.fft function
    x = fft.sound_tolist(sound)
    X = fft.fft(x)
    f0 = fft.fundamental_frequency_fft(X, fs)
    note = sounds.to_note(f0)
    print(f"Fundamental frequency using fft.fft: {f0}, note {note}")

    x = fft.sound_tolist(noisy_sound)
    X = fft.fft(x)
    f0 = fft.fundamental_frequency_fft(X, fs)
    note = sounds.to_note(f0)
    print(f"Fundamental frequency using fft.fft: {f0}, note {note}")

if __name__ == "__main__":
    main()