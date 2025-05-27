from audio_gen import AudioContex

audioContext = AudioContex(25, 44100, 0.5)

fundamental = 220
for i in range(20):
    audioContext.add_wave(i, audioContext.total_duration-i, 1/(2*i+1), fundamental*(2*i+1), 0)
audioContext.get_wav("tester.wav")