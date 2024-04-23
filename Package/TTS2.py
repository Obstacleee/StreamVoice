import os
import tempfile
import requests
import subprocess

from Package import discord_storage
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv('OPENAIKEY')

def text_to_speech(texte, voice='alloy'):
    
    partie1 = None
    partie2 = None
    if len(texte) > 4096:
        partie1 = texte[:len(texte) // 2]
        partie2 = texte[len(texte) // 2:]

        response = requests.post(
            "https://api.openai.com/v1/audio/speech",
            headers={"Authorization": f"Bearer {openai_key}"},
            json={"model": "tts-1", "input": partie1, "voice": voice}
        )
        if response.status_code != 200:
            raise Exception(f"Request failed with status code: {response.status_code}")

        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            tmpfile.write(response.content)
            files1 = tmpfile.name

        response = requests.post(
            "https://api.openai.com/v1/audio/speech",
            headers={"Authorization": f"Bearer {openai_key}"},
            json={"model": "tts-1", "input": partie2, "voice": voice}
        )

        if response.status_code != 200:
            raise Exception(f"Request failed with status code: {response.status_code}")

        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            tmpfile.write(response.content)
            files2 = tmpfile.name

        # Utilisation de FFmpeg pour concaténer les fichiers audio
        output_file = "mp3/final.mp3"
        command = f"ffmpeg -i 'concat:{files1}|{files2}' -acodec copy {output_file}"
        subprocess.run(command, shell=True, check=True)

        lien = discord_storage.send_and_get_file_link(output_file)
        os.remove(output_file)
        return lien

    else:
        response = requests.post(
            "https://api.openai.com/v1/audio/speech",
            headers={"Authorization": f"Bearer {openai_key}"},
            json={"model": "tts-1", "input": texte, "voice": voice}
        )
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            tmpfile.write(response.content)
            lien = discord_storage.send_and_get_file_link(tmpfile.name)
            os.remove(tmpfile.name)
            return lien
