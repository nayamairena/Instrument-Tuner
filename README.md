# HW3: Tuner

## Naya Mairena

Build an instrument tuner with two modes:

- Mode 1: Run the program with `python3 tuner.py guitar-a3.wav` with command line arguments.
- Mode 2: Run the program with `python3 tuner.py` for microphone input, no command line arguments taking in WAV files.
  ## **When doing Mode 2, it will be in an infinite loop, to exit the program: `ctrl+c`**
  Prints the frequency of either the WAV files or continuously print live mic frequency input.

Steps to follow for the program:

1. Trim the file to the first 2^17 samples (a few seconds) if it is longer than that. If it is shorter, trim to the largest possible power of 2.

2. Apply a triangular window to the samples. You can construct this window (linear increase from 0 to 1 halfway, then linear decrease to 0 at the end) manually, or get it from somewhere.

3. Take the DFT of the windowed samples.

4. Find the largest bin in the DFT.

5. Report the center frequency of that bin.

Resources utilized:  
https://docs.python.org/3/library/wave.html  
https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.windows.triang.html#scipy.signal.windows.triang  
https://docs.scipy.org/doc/scipy/tutorial/fft.html
