import numpy as np
import sounddevice as sd
from pynput import keyboard

NOTE_MAPPING = {
    'z': 261.63,  # C4
    's': 277.18,  # C#4/Db4
    'x': 293.66,  # D4
    'd': 311.13,  # D#4/Eb4
    'c': 329.63,  # E4
    'v': 349.23,  # F4
    'g': 369.99,  # F#4/Gb4
    'b': 392.00,  # G4
    'h': 415.30,  # G#4/Ab4
    'n': 440.0,   # A4
    'j': 466.16,  # A#4/Bb4
    'm': 493.88,  # B4

    'q': 523.25,  # C5 
    '2': 554.37,  # C#5/Db5
    'w': 587.33,  # D5
    '3': 622.25,  # D#5/Eb5
    'e': 659.26,  # E5
    'r': 698.46,  # F5
    '5': 739.99,  # F#5/Gb5
    't': 783.99,  # G5
    '6': 830.61,  # G#5/Ab5
    'y': 880.00,  # A5
    '7': 932.33,  # A#5/Bb5
    'u': 987.77,  # B5

    'i': 1046.50, # C6
    '9': 1108.73, # C#6/Db6
    'o': 1174.66, # D6
    '0': 1244.51, # D#6/Eb6
    'p': 1318.51, # E6
}

def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return amplitude * np.sin(2 * np.pi * freq * t)

def play_sound(sound_array, sample_rate=44100):
    sd.stop()
    sd.play(sound_array, samplerate=sample_rate)
    sd.wait()

def on_key_release(key):
    if key == keyboard.Key.esc:
        listener.stop()
        return
    
    try:
        key_char = key.char
    except AttributeError:
        return

    if key_char in NOTE_MAPPING:
        sound = generate_sine_wave(NOTE_MAPPING[key_char], 0.27)
        play_sound(sound)

if __name__ == "__main__":
    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()