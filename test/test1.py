# import keyboard
import numpy as np
import pygame
import sounddevice as sd
from scipy.io.wavfile import write
# from pynput.keyboard import Key, Listener, Controller
# from pynput import keyboard
import keyboard

def record_audio(file_name: str = "recording") -> str:
    sampling_frequency = 44100
    recording_started = False

    audio_data = []

    # with Listener(on_press=on_press, on_release=on_release) as listener:
    #     listener.join()
    exit = False

    with sd.InputStream(samplerate=sampling_frequency, channels=2) as stream:
        
        
        while True:
            event = keyboard.read_event(suppress=True)
            if event and event.event_type == keyboard.KEY_DOWN:
                if not recording_started:
                    recording_started = True
                    print("Recording Started")

                audio_chunk, overflowed = stream.read(1024)
                audio_data.append(audio_chunk)

            elif event and event.event_type == keyboard.KEY_UP and recording_started:
                print("Recording stopped.")
                break
                
    print('here')
    if audio_data:
        audio_data = np.concatenate(audio_data, axis=0)
        sd.wait()
        write(f"{file_name}.wav", sampling_frequency, audio_data)
    else:
        print("No audio recorded.")

    return f"{file_name}.wav"

if __name__ == "__main__":
    record_audio()