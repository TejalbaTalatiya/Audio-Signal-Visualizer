import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def generate_signal_spectrogram(audio_path):
    """
    Processes raw audio binaries, plots time-domain wave dynamics, 
    and applies Fast Fourier Transform (FFT) logic.
    """
    sampling_rate, audio_data = wavfile.read(audio_path)
    
    if len(audio_data.shape) > 1:
        audio_data = audio_data.mean(axis=1)
        
    duration = len(audio_data) / sampling_rate
    time_steps = np.linspace(0, duration, len(audio_data))
    
    plt.figure(figsize=(10, 5))
    
    # Plot 1: Waveform (Amplitude vs Time)
    plt.subplot(2, 1, 1)
    plt.plot(time_steps, audio_data, color='teal')
    plt.title('Time-Domain Acoustic Waveform')
    plt.ylabel('Amplitude')
    
    # Plot 2: Frequency Spectrum (Magnitude vs Frequency)
    plt.subplot(2, 1, 2)
    fft_transformed = np.fft.fft(audio_data)
    frequencies = np.fft.fftfreq(len(fft_transformed), 1/sampling_rate)
    
    pos_freqs = frequencies[:len(frequencies)//2]
    pos_mags = np.abs(fft_transformed[:len(fft_transformed)//2])
    
    plt.plot(pos_freqs, pos_mags, color='darkorange')
    plt.title('Frequency Spectrum via Fast Fourier Transform (FFT)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    
    plt.tight_layout()
    print("[Success] Image arrays generated locally.")

if __name__ == "__main__":
    sr = 22050
    t = np.linspace(0, 2, 2 * sr)
    synthetic_note = np.sin(2 * np.pi * 440 * t) * 32767
    wavfile.write("synthetic_pitch.wav", sr, synthetic_note.astype(np.int16))
    
    generate_signal_spectrogram("synthetic_pitch.wav")
