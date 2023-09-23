import numpy as np
import sounddevice as sd
from pynput import keyboard

NOTE_MAPPING = {
    'a': 440.0,  # A4
    'w': 466.16, # A#4/Bb4
    's': 493.88, # B4
    'd': 523.25, # C5
    'r': 554.37, # C#5/Db5
    'f': 587.33, # D5
    't': 622.25, # D#5/Eb5
    'g': 659.26, # E5
    'h': 698.46, # F5
    'u': 739.99, # F#5/Gb5
    'j': 783.99, # G5
    'i': 830.61  # G#5/Ab5
}

def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=0.5):
    """Generate a sine wave of given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return amplitude * np.sin(2 * np.pi * freq * t)

def play_sound(sound_array, sample_rate=44100):
    """Play the given sound array."""
    sd.play(sound_array, samplerate=sample_rate)
    sd.wait()

def on_key_release(key):
    try:
        key_char = key.char
    except AttributeError:
        # Skip special keys
        return

    if key_char in NOTE_MAPPING:
        sound = generate_sine_wave(NOTE_MAPPING[key_char], 0.5)
        play_sound(sound)

if __name__ == "__main__":
    # Start listening to keyboard events
    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()