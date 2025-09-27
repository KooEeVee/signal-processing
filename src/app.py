import numpy as np
import fft
import sounds

def main():

    #Define the test signal
    fs = 1024 #sampling rate, assuming power of two, no need to change this
    s = 2 #length of sample sequence in seconds, assuming power of two, no need to change this
    #freq = 440 #update the pitch value "440", uncomment if you want to use Hz as parameter
    freq = sounds.to_freq("F4") #update the pitch value "F4", if you want to use the note name as parameter 
    noise_amp = 10 #update the noise amplitude value to amplify or attenuate noise, for example 100 sould interfere pitch detection

    sound = sounds.generate_sine(fs, s, freq)
    noisy_sound = sounds.generate_noisysine(fs, s, freq, noise_amp)
    #sound = sounds.record_sound(fs, s) #doesn't work

    #Plot and listen to test signals, uncomment to listen
    #sounds.play_sound(sound, fs)
    sounds.plot_time(sound, fs)
    sounds.plot_freq(sound, fs)

    #sounds.play_sound(noisy_sound, fs)
    sounds.plot_time(noisy_sound, fs)
    sounds.plot_freq(noisy_sound, fs)

    #Testing numpy fft.rfft function
    f0_a = fft.fundamental_frequency_np(sound, fs)
    note_a = sounds.to_note(f0_a)
    print(f"Fundamental frequency 'sound' using np.fft.rfft: {f0_a}, note {note_a}")
    
    f0_b = fft.fundamental_frequency_np(noisy_sound, fs)
    note_b = sounds.to_note(f0_b)
    print(f"Fundamental frequency 'noisy sound' using np.fft.rfft: {f0_b}, note {note_b}")

    #Testing fft.fft function
    x = fft.sound_tolist(sound)
    X = fft.fft(x)
    f0_c = fft.fundamental_frequency_fft(X, fs)
    note_c = sounds.to_note(f0_c)
    print(f"Fundamental frequency 'sound' using fft.fft: {f0_c}, note {note_c}")

    x = fft.sound_tolist(noisy_sound)
    X = fft.fft(x)
    f0_d = fft.fundamental_frequency_fft(X, fs)
    note_d = sounds.to_note(f0_d)
    print(f"Fundamental frequency 'noisy sound' using fft.fft: {f0_d}, note {note_d}")

if __name__ == "__main__":
    main()