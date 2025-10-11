#import numpy as np
#import fft
#import sounds
from flask import Flask, render_template, request
from sounds import generate_sine, generate_noisysine, play_sound, plot_time, plot_freq, to_note
from fft import sound_tolist, fft, fundamental_frequency_fft

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    chosen_signal = None
    signal = None
    play_signal = None
    plot_image = None
    pitch_result = None
    
    if request.method == "POST":
        chosen_signal = request.form.get("choose_signal")
        if chosen_signal == "Sine wave":
            signal = generate_sine(16384, 2, 440)
        elif chosen_signal == "Sine wave with noise":
            signal = generate_noisysine(16384, 2, 440, 50)

        """ if "play_button" in request.form and signal is not None:
            play_sound(signal, 1024)
            play_signal = f"Playing signal: {chosen_signal}" """

        if "plot_time_button" in request.form and signal is not None:
            plot_image = plot_time(signal, 16384)
        
        if "plot_freq_button" in request.form and signal is not None:
            plot_image = plot_freq(signal, 16384)

        if "freq_button" in request.form and signal is not None:
            signal_list = sound_tolist(signal)
            signal_list_fft = fft(signal_list)
            frequency = fundamental_frequency_fft(signal_list_fft, 16384)
            pitch_result = f"Frequency: {frequency:.2f} Hz"

        elif "note_button" in request.form and signal is not None:
            signal_list = sound_tolist(signal)
            signal_list_fft = fft(signal_list)
            frequency = fundamental_frequency_fft(signal_list_fft, 16384)
            note = to_note(frequency)
            pitch_result = f"Note: {note}"

    return render_template("index.html", chosen_signal=chosen_signal, play_signal=play_signal, plot_image=plot_image, pitch_result=pitch_result)

    #Define the test signal
    fs = 1024 #sampling rate, assuming power of two, no need to change this
    s = 2 #length of sample sequence in seconds, assuming power of two, no need to change this
    #freq = 440 #update the pitch value "440", uncomment if you want to use Hz as parameter
    freq = sounds.to_freq("F4") #update the pitch value "F4", if you want to use the note name as parameter 
    noise_amp = 10 #update the noise amplitude value to amplify or attenuate noise, for example 100 sould interfere pitch detection

    # sound = sounds.generate_sine(fs, s, freq)
    # noisy_sound = sounds.generate_noisysine(fs, s, freq, noise_amp)
    #sound = sounds.record_sound(fs, s) #doesn't work

    #Plot and listen to test signals, uncomment play_sound to listen
    #sounds.play_sound(sound, fs)
    # sounds.plot_time(sound, fs)
    # sounds.plot_freq(sound, fs)

    #sounds.play_sound(noisy_sound, fs)
    # sounds.plot_time(noisy_sound, fs)
    # sounds.plot_freq(noisy_sound, fs)

    #Testing numpy fft.rfft function
    # f0_a = fft.fundamental_frequency_np(sound, fs)
    # note_a = sounds.to_note(f0_a)
    # print(f"Fundamental frequency 'sound' using np.fft.rfft: {f0_a} Hz, note {note_a}")
    
    # f0_b = fft.fundamental_frequency_np(noisy_sound, fs)
    # note_b = sounds.to_note(f0_b)
    # print(f"Fundamental frequency 'noisy sound' using np.fft.rfft: {f0_b} Hz, note {note_b}")

    #Testing fft.fft function
    # x = fft.sound_tolist(sound)
    # X = fft.fft(x)
    # f0_c = fft.fundamental_frequency_fft(X, fs)
    # note_c = sounds.to_note(f0_c)
    # print(f"Fundamental frequency 'sound' using fft.fft: {f0_c} Hz, note {note_c}")

    # x = fft.sound_tolist(noisy_sound)
    # X = fft.fft(x)
    # f0_d = fft.fundamental_frequency_fft(X, fs)
    # note_d = sounds.to_note(f0_d)
    # print(f"Fundamental frequency 'noisy sound' using fft.fft: {f0_d} Hz, note {note_d}")

if __name__ == "__main__":
    app.run(debug=True)