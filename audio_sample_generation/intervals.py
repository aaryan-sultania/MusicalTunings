from audio_gen import AudioContex

def createChordSample(pitch_list, audio_filename):
    audioContext = AudioContex(len(pitch_list)*2+2, 44100, 0.5)
    for i, pitch in enumerate(pitch_list):
        audioContext.add_wave(i*2, 1.75, 0.5, pitch, 2)
        audioContext.add_wave(len(pitch_list)*2, 1.75, 0.5, pitch, 2)
    audioContext.get_wav(audio_filename)

def edo_steps(edo, steps):
    return 2**(steps/edo)

a = 440
createChordSample((a, a*2),"octave.wav")
createChordSample((a, a*3/2),"just_perfect_fifth.wav")
createChordSample((a, a*5/4, a*3/2),"4-5-6_major_triad.wav")
createChordSample((a, a*(3/2)/(531441/524288)),"wolf-fifth.wav")