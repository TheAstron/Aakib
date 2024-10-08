#This code Belongs to Aakib Patel & his Mohabbat

import keyboard
from gtts import gTTS
import pygame
import os
import threading
import time

# Configure the pause duration (in seconds) between words
PAUSE_DURATION = 1

def text_to_speech(text, lang='en', output_file='output.mp3'):
    try:
        # Generate speech from text
        tts = gTTS(text=text, lang=lang, slow=False)
        # Save the speech to a file
        tts.save(output_file)
        
        # Load and play the sound
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()
        
        # Wait for the sound to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Clean up the temporary file
#        os.remove(output_file)
        
    except Exception as e:
        print(f"An error occurred: {e}")

def play_text_with_pause(text):
    words = text.split()
    for word in words:
        # Generate and play each word
        text_to_speech(word)
        # Wait for a pause between words
        time.sleep(PAUSE_DURATION)

def main():
    print("Type your text. Press space to hear the text spoken aloud. Press 'q' to quit.")
    
    accumulated_text = ""

    while True:
        if keyboard.is_pressed('q'):
            break
        
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'space':
                if accumulated_text:
                    # Start a new thread to play the text with pause
                    threading.Thread(target=play_text_with_pause, args=(accumulated_text,)).start()
                    accumulated_text = ""  # Clear the accumulated text after reading
            elif event.name == 'backspace':
                accumulated_text = accumulated_text[:-1]
            elif len(event.name) == 1:  # Only process single character keys
                accumulated_text += event.name

if __name__ == "__main__":
    pygame.mixer.init()  # Initialize mixer here
    main()
