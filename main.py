from audio_gen import AudioContex
audioContext = AudioContex(25, 44100, 0.5)

def bachMotif(location, pitch1, pitch2, pitch3, pitch4, pitch5):
    audioContext.add_wave(location + 0, 2, 0.5, pitch1, 2)
    audioContext.add_wave(location + 0.25, 1.75, 0.5, pitch2, 2)
    audioContext.add_wave(location + 0.5, 0.25, 0.5, pitch3, 2)
    audioContext.add_wave(location + 0.75, 0.25, 0.5, pitch4, 2)
    audioContext.add_wave(location + 1, 0.25, 0.5, pitch5, 2)
    audioContext.add_wave(location + 1.25, 0.25, 0.5, pitch3, 2)
    audioContext.add_wave(location + 1.5, 0.25, 0.5, pitch4, 2)
    audioContext.add_wave(location + 1.75, 0.25, 0.5, pitch5, 2)

key_C = 261
bachMotif(0, key_C, key_C * 5/4, key_C * 3/2, key_C * 2, key_C * 5/2)
bachMotif(2, key_C, key_C * 5/4, key_C * 3/2, key_C * 2, key_C * 5/2)
bachMotif(4, key_C, key_C * 9/8, key_C * 27/16, key_C * 9/4, key_C * 9/4 * 7/6)
bachMotif(6, key_C, key_C * 9/8, key_C * 27/16, key_C * 9/4, key_C * 9/4 * 7/6)
bachMotif(8, key_C * 3/4 * 5/4, key_C * 9/8, key_C * 3/2, key_C * 9/4, key_C * 9/4 * 7/6)
bachMotif(10, key_C * 3/4 * 5/4, key_C * 9/8, key_C * 3/2, key_C * 9/4, key_C * 9/4 * 7/6)
bachMotif(12, key_C, key_C * 5/4, key_C * 3/2, key_C * 2, key_C * 5/2)
bachMotif(14, key_C, key_C * 5/4, key_C * 3/2, key_C * 2, key_C * 5/2)
audioContext.get_wav("bach.wav")