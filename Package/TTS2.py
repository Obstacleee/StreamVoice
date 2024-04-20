import  os 
from Package import discord_storage
import tempfile    # Library for creating temporary files and directories
import os          # Library for interacting with the operating system
import requests    # Library for making HTTP requests
import openai      # Library for interacting with OpenAI API
from pydub import AudioSegment


openai_key = os.getenv('OPENAIKEY')


def text_to_speech(texte, voice='alloy'):
    # If the text is too long, split it in half and synthesize each half separately
    partie1 = None
    partie2 = None
    if len(texte) > 4096:
        partie1 = texte[:len(texte)//2]
        partie2 = texte[len(texte)//2:]

    if partie2:

        response = requests.post(
            "https://api.openai.com/v1/audio/speech",
            headers={"Authorization": f"Bearer {openai_key}"},
            json={"model": "tts-1", "input": partie1, "voice": voice}
        )
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            tmpfile.write(response.content)
            lien1 = tmpfile.name

        response = requests.post(
            "https://api.openai.com/v1/audio/speech",
            headers={"Authorization": f"Bearer {openai_key}"},
            json={"model": "tts-1", "input": partie1, "voice": voice}
        )
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfiles:
            tmpfiles.write(response.content)
            lien2 = tmpfiles.name

        audio1 = AudioSegment.from_file(lien1 , format="mp3")
        audio2 = AudioSegment.from_file(lien2 , format="mp3")
        audio = audio1 + audio2
        audio.export("mp3/audio.mp3",format = "mp3")
        lien = discord_storage.send_and_get_file_link("mp3/audio.mp3")
        return lien
    else : 
        response = requests.post(
            "https://api.openai.com/v1/audio/speech",
            headers={"Authorization": f"Bearer {openai_key}"},
            json={"model": "tts-1", "input": texte, "voice": voice}
        )
        # Save the speech to a temporary MP3 file and return the file path
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            tmpfile.write(response.content)
            lien = discord_storage.send_and_get_file_link(tmpfile.name)
            return lien


    
    

