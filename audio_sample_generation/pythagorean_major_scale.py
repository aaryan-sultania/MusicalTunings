from audio_gen import AudioContex
audCtx = AudioContex(total_duration=10, sample_rate=44100, anti_clipping_scale=1)

c = 261
audCtx.add_wave(0, 1, 0.75, c, 2)
audCtx.add_wave(1, 1, 0.75, c * 9/8, 2)
audCtx.add_wave(2, 1, 0.75, c * 81/64, 2)
audCtx.add_wave(3, 1, 0.75, c * 4/3, 2)
audCtx.add_wave(4, 1, 0.75, c * 3/2, 2)
audCtx.add_wave(5, 1, 0.75, c * 27/16, 2)
audCtx.add_wave(6, 1, 0.75, c * 243/128, 2)
audCtx.add_wave(7, 1, 0.75, c * 2, 2)

audCtx.get_wav("pythagorean_major_scale.wav")