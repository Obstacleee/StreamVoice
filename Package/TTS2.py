import pyttsx3 , os 
from Package import discord_storage
import tempfile    # Library for creating temporary files and directories
import os          # Library for interacting with the operating system
import requests    # Library for making HTTP requests
import openai      # Library for interacting with OpenAI API
import time

openai_api_key = "API KEY"
    
def text_to_speech(text, voice='alloy'):
    """
    Converts the provided text to speech using OpenAI's text-to-speech API.

    Parameters:
    - text (str): The text to be converted to speech.
    - voice (str, optional): The voice model to be used for the text-to-speech conversion. Defaults to 'alloy'.

    Returns:
    - str: The file path to the temporary MP3 file containing the speech.

    Raises:
    - Exception: If the request to OpenAI's API fails.

    """
    response = requests.post(
        "https://api.openai.com/v1/audio/speech",
        headers={"Authorization": f"Bearer {openai_api_key}"},
        json={"model": "tts-1", "input": text, "voice": voice}
    )
    
    # Raise an exception if the API call was unsuccessful
    if response.status_code != 200:
        response = requests.post(
        "https://api.openai.com/v1/audio/speech",
        headers={"Authorization": f"Bearer {openai_api_key}"},
        json={"model": "tts-1", "input": text, "voice": voice}
    )
        


    # Save the speech to a temporary MP3 file and return the file path
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
        tmpfile.write(response.content)
        lien = discord_storage.send_and_get_file_link(tmpfile.name)
        time.sleep(3)
        return lien

