import numpy as np
import sounddevice as sd

def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=0.5):
    """Generate a sine wave of given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return amplitude * np.sin(2 * np.pi * freq * t)

def play_sound(sound_array, sample_rate=44100):
    """Play the given sound array."""
    sd.play(sound_array, samplerate=sample_rate)
    sd.wait()

if __name__ == "__main__":
    frequency = float(input("Enter the frequency (in Hz): "))
    duration = float(input("Enter the duration (in seconds): "))

    sound = generate_sine_wave(frequency, duration)
    play_sound(sound)