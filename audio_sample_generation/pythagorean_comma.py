from audio_gen import AudioContex
audCtx = AudioContex(total_duration=20, sample_rate=44100, anti_clipping_scale=1)

c = 261
audCtx.add_wave(0, 1, 0.75, c * ((3/2)**0)/((2/1)**0), 2)
audCtx.add_wave(1, 1, 0.75, c * ((3/2)**1)/((2/1)**0), 2)
audCtx.add_wave(2, 1, 0.75, c * ((3/2)**2)/((2/1)**1), 2)
audCtx.add_wave(3, 1, 0.75, c * ((3/2)**3)/((2/1)**1), 2)
audCtx.add_wave(4, 1, 0.75, c * ((3/2)**4)/((2/1)**2), 2)
audCtx.add_wave(5, 1, 0.75, c * ((3/2)**5)/((2/1)**2), 2)
audCtx.add_wave(6, 1, 0.75, c * ((3/2)**6)/((2/1)**3), 2)
audCtx.add_wave(7, 1, 0.75, c * ((3/2)**7)/((2/1)**4), 2)
audCtx.add_wave(8, 1, 0.75, c * ((3/2)**8)/((2/1)**4), 2)
audCtx.add_wave(9, 1, 0.75, c * ((3/2)**9)/((2/1)**5), 2)
audCtx.add_wave(10, 1, 0.75, c * ((3/2)**10)/((2/1)**5), 2)
audCtx.add_wave(11, 1, 0.75, c * ((3/2)**11)/((2/1)**6), 2)
audCtx.add_wave(12, 1, 0.75, c * ((3/2)**12)/((2/1)**7), 2)

audCtx.add_wave(14, 0.9, 0.75, c, 2)
audCtx.add_wave(15, 0.9, 0.75, c * ((3/2)**12)/((2/1)**7), 2)
audCtx.add_wave(16, 0.9, 0.75, c, 2)
audCtx.add_wave(17, 0.9, 0.75, c * ((3/2)**12)/((2/1)**7), 2)

audCtx.get_wav("pythagorean_comma.wav")