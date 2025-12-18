from audio_gen import AudioContex
import matplotlib.pyplot as plt

def createSample(stype, sname):
    audioContext = AudioContex(5, 44100, 0.5)
    audioContext.add_wave(0.5, 3, 1, 440, stype)
    audioContext.get_wav(f"{sname}.wav")
    plt.plot(audioContext.time, audioContext.audio)
    plt.xlim(1, 1.01)
    plt.savefig(f"{sname}.png")
    plt.xlabel("time")
    plt.ylabel("air pressure")
    plt.show()
    plt.close()

createSample(0, "sine440")
createSample(1, "square440")
createSample(3, "sawtooth440")