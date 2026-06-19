# Audio-Signal-Visualizer
Digital Signal Processing engine utilizing Fast Fourier Transforms (FFT) to convert continuous waveforms into frequency domains.
# Time-Frequency Domain Acoustic Signal Analyzer via Discrete Fourier Transforms
**Domain:** Digital Signal Processing (DSP) & Acoustic Wave Physics

## Project Abstract
Before constructing multi-layered deep learning architectures for sound processing, this project validates the fundamental physics of sound capture using Digital Signal Processing (DSP). The tool ingests continuous raw acoustic waveforms (such as an acoustic instrument note), maps the structural time-domain amplitude profiles, and executes a Fast Fourier Transform (FFT) calculation to shift the signal into a discrete frequency spectrum. This isolates harmonic frequencies from static background noise.

## Core Engineering Competencies Tested
* **Signal Transformation Processing:** Implementing mathematical Fourier Analysis (`np.fft`).
* **Waveform Array Manipulation:** Transforming multi-channel stereo wave arrays into balanced mono matrices.
* **Academic Data Presentation:** Generating time-frequency domain plots using clean visualization standards.

## Setup & Execution
Execute the analytical script:
'''bash
python signal_plotter.py
'''
