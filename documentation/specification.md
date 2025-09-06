# Specification

## Programming language
Python

## Core algorithm
Fast Fourier Transform FFT (Cooley-Tukey algorithm)

## Implementing pitch detection with FFT
For analysis, signals are often transformed from time-domain to frequency-domain. Discrete Fourier Transform DFT is a method for converting a discrete signal, sequence of samples in time-domain, to frequency-domain components. But it is computationally slow. Fast Fourier Transform FFT is an algorithm to compute DFT faster. DFT requires O(n²) operations, while FFT as a divide-and-conquer algorithm requires O(n log n) operations.

The pitch of a sound can be detected by analysing the audio signal in frequency-domain. FFT creates the spectrum of signal's frequencies and their amplitudes. The pitch corresponds to the fundamental frequency, which is usually the lowest frequency peak in the spectrum.

## Inputs
Audio signals in waveform will be transformed to discrete-time signals: sequence of samples (floats in array or vector). One wav file contains one note recorded for example with accordion, piano, acoustic guitar or flute.

## Sources and references
Proakis, John G. & Manolakis, Dimitris K.: Digital Signal Processing. Pearson Education Limited 2014.
[Wikipedia Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)
[Wikipedia Cooley–Tukey FFT algorithm](https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm)

## Course info
Study program: Bachelor's in Computer Science (TKT)
Language of project documentation: English

