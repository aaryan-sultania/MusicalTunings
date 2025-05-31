import numpy as np
from scipy.io.wavfile import write
from scipy import signal

class AudioContex:
    def __init__(self, total_duration, sample_rate, anti_clipping_scale):
        self.sample_rate = sample_rate
        self.total_duration = total_duration
        self.anti_clipping_scale = anti_clipping_scale

        self.time = np.linspace(0, total_duration, int(sample_rate * total_duration), False)
        self.audio = np.zeros(int(sample_rate * total_duration))
    
    @staticmethod
    def sine_wave(frequency, times):
        return np.sin(frequency * 2 * np.pi * times)
    @staticmethod
    def square_wave(frequency, times):
        return signal.square(frequency * 2 * np.pi * times)
    @staticmethod
    def square_wave(frequency, times):
        return signal.square(frequency * 2 * np.pi * times)
    @staticmethod
    def triangle_wave(frequency, times):
        return signal.sawtooth(frequency * 2 * np.pi * times, width=0.5)
    @staticmethod
    def sawtooth_wave(frequency, times):
        return signal.sawtooth(frequency * 2 * np.pi * times, width=1)

    def add_wave(self, location, duration, amplitude, frequency, type):
        match type:
            case 0:
                self.audio[int(self.sample_rate * location):int(self.sample_rate * (location+duration))] += amplitude * self.sine_wave(frequency, self.time[int(self.sample_rate * location):int(self.sample_rate * (location+duration))])
            case 1:
                self.audio[int(self.sample_rate * location):int(self.sample_rate * (location+duration))] += amplitude * self.square_wave(frequency, self.time[int(self.sample_rate * location):int(self.sample_rate * (location+duration))])
            case 2:
                self.audio[int(self.sample_rate * location):int(self.sample_rate * (location+duration))] += amplitude * self.triangle_wave(frequency, self.time[int(self.sample_rate * location):int(self.sample_rate * (location+duration))])
            case 3:
                self.audio[int(self.sample_rate * location):int(self.sample_rate * (location+duration))] += amplitude * self.sawtooth_wave(frequency, self.time[int(self.sample_rate * location):int(self.sample_rate * (location+duration))])
            
    def max_anticlip(self):
        self.anti_clipping_scale = np.max(np.abs(self.audio))
    def get_wav(self, audiofilename):
        audio_data = np.int16(self.anti_clipping_scale * self.audio * 32767)
        write(audiofilename, self.sample_rate, audio_data)



