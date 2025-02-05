import sounddevice as sd  # To record audio
import numpy as np  # For handling audio data
import scipy.io.wavfile as wav  # For saving the audio to a .wav file
import time  # To track the duration of recording

def record_audio(duration, samplerate=44100):
    """
    Function to record audio from the microphone.
    - duration: how long (in seconds) to record the audio
    - samplerate: the sample rate of the audio (default: 44100 samples per second)
    """
    print("Recording started...")

    # Record audio as a numpy array from the microphone
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    
    # Wait until the recording is finished
    sd.wait()

    print(f"Recording finished! {duration} seconds of audio recorded.")
    return audio_data

def save_audio(filename, audio_data, samplerate=44100):
    """
    Save the recorded audio data into a .wav file.
    - filename: name of the output file
    - audio_data: the audio data to save
    - samplerate: the sample rate used in the recording
    """
    wav.write(filename, samplerate, audio_data)
    print(f"Audio saved to {filename}")

def start_recording():
    """
    Main function to start the recording process and save the audio.
    """
    try:
        duration = float(input("Enter recording duration (in seconds): "))  # Ask user for recording duration
        if duration <= 0:
            print("Please enter a positive duration!")
            return

        # Start the recording
        audio_data = record_audio(duration)

        # Ask where to save the file
        filename = input("Enter the filename to save (e.g., 'recording.wav'): ")

        # Save the audio to the specified file
        save_audio(filename, audio_data)
        
    except ValueError:
        print("Invalid input! Please enter a valid number for duration.")

# Run the recording function
if __name__ == "__main__":
    start_recording()
