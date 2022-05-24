'''
Name: Naya Mairena
HW3: tuner.py
May, 2, 2022
'''
import wave
import sys
import pyaudio
import numpy as np
import scipy.signal as signal
import scipy.fftpack as fft

#Report the frequency of a WAV file entered by command line arguments.
#Open the WAV file from command line
if len(sys.argv) > 1:

    wav = wave.open(sys.argv[1], 'rb')
    sample_rate = wav.getframerate()
    frames = np.frombuffer(wav.readframes(wav.getnframes()), dtype = np.int16).astype(np.float64)

    #Trim the file: frames per second size
    if len(frames) > 2**17:
        frames = frames[:2**17]
    else:
        trim = 2**int(np.log2(len(frames)))
        frames = frames[:trim]

    #Apply triangular window to the samples. 
    window = signal.windows.triang(len(frames))
    windowed = frames * window

    #Take DFT of windowed samples.
    DFT = fft.fft(windowed)

    #Get the largest bin.
    lbin = np.argmax(abs(DFT))

    #Get the center of frequency
    cfreq = sample_rate * lbin / len(frames)
    print(cfreq)

    wav.close()

else:
    #Continuously report the frequency of microphone input.
    chunk = 8192
    sformat = pyaudio.paInt16
    fs = 48000

    stream = pyaudio.PyAudio().open(format = sformat, channels = 1, rate = fs, frames_per_buffer = chunk, input = True)
    frames2 = []

    while(True):
        frames2 = np.frombuffer(stream.read(chunk), dtype = np.int16)
        window2 = signal.windows.triang(len(frames2))
        windowed2 = frames2 * window2
        DFT2 = fft.fft(windowed2)
        lbin2 = np.argmax(abs(DFT2))
        cfreq2 = fs * lbin2 / len(frames2)
        print(cfreq2)

    stream.stop_stream()
    stream.close()
    stream.terminate()
