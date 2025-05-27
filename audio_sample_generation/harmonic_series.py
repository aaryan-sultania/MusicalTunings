from audio_gen import AudioContex

audioContext = AudioContex(25, 44100, 0.5)

fundamental = 220
for i in range(20):
    audioContext.add_wave(i, audioContext.total_duration-i, 1/(2*i+1), fundamental*(2*i+1), 0)
audioContext.get_wav("audio_samples/harmonic_series.wav")

squareContext = AudioContex(15, 44100, 0.5)
squareContext.add_wave(1, 10, 1, fundamental, 1)
squareContext.get_wav("audio_samples/square.wav")