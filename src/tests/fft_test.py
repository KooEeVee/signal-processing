import pytest
import fft
import numpy as np

def test_fft_compare_integers():
    """np.allclose relative tolerance between elements 1e-5, absolute tolerance between elements 1e-8
    """
    signal = [1,2,3,4]
    signal_fft = fft.fft(signal)
    signal_fft_np = np.fft.fft(signal)
    assert np.allclose(signal_fft, signal_fft_np)

def test_fft_compare_zeros():
    signal = [0,0,0,0]
    signal_fft = fft.fft(signal)
    signal_fft_np = np.fft.fft(signal)
    assert np.allclose(signal_fft, signal_fft_np)

def test_fft_compare_sine():
    fs = 16384
    s = 2
    f0 = 440
    t = np.linspace(0, s, int(fs * s))
    signal = np.sin(2 * np.pi * f0 * t)
    signal_fft = fft.fft(signal)
    signal_fft_np = np.fft.fft(signal)
    assert np.allclose(signal_fft, signal_fft_np)

def test_fft_compare_two_sines():
    fs = 16384
    s = 2
    f0a = 440
    f0b = 261.63
    t = np.linspace(0, s, int(fs * s))
    signal = np.sin(2 * np.pi * f0a * t) + np.sin(2 * np.pi * f0b * t)
    signal_fft = fft.fft(signal)
    signal_fft_np = np.fft.fft(signal)
    assert np.allclose(signal_fft, signal_fft_np)

def test_fft_compare_random():
    fs = 16384
    s = 2
    signal = np.random.randn(fs * s)
    signal_fft = fft.fft(signal)
    signal_fft_np = np.fft.fft(signal)
    assert np.allclose(signal_fft, signal_fft_np)

def test_fft_ifft_integers():
    signal = [1,2,3,4]
    signal_fft = fft.fft(signal)
    signal_ifft = np.fft.ifft(signal_fft)
    assert np.allclose(signal, signal_ifft)

def test_fft_ifft_zeros():
    signal = [0,0,0,0]
    signal_fft = fft.fft(signal)
    signal_ifft = np.fft.ifft(signal_fft)
    assert np.allclose(signal, signal_ifft)

def test_fft_ifft_sine():
    fs = 16384
    s = 2
    f0 = 440
    t = np.linspace(0, s, int(fs * s))
    signal = np.sin(2 * np.pi * f0 * t)
    signal_fft = fft.fft(signal)
    signal_ifft = np.fft.ifft(signal_fft)
    assert np.allclose(signal, signal_ifft)

def test_fft_ifft_two_sines():
    fs = 16384
    s = 2
    f0a = 440
    f0b = 261.63
    t = np.linspace(0, s, int(fs * s))
    signal = np.sin(2 * np.pi * f0a * t) + np.sin(2 * np.pi * f0b * t)
    signal_fft = fft.fft(signal)
    signal_ifft = np.fft.ifft(signal_fft)
    assert np.allclose(signal, signal_ifft)

def test_fft_ifft_random():
    fs = 16384
    s = 2
    signal = np.random.randn(fs * s)
    signal_fft = fft.fft(signal)
    signal_ifft = np.fft.ifft(signal_fft)
    assert np.allclose(signal, signal_ifft)