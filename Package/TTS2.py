import os  # Library for interacting with the operating system
import tempfile  # Library for creating temporary files and directories

import requests  # Library for making HTTP requests
from moviepy.editor import concatenate_audioclips, AudioFileClip

from Package import discord_storage
from dotenv import load_dotenv

load_dotenv()


openai_key = os.getenv('OPENAIKEY')


def text_to_speech(texte, voice='alloy'):
    # If the text is too long, split it in half and synthesize each half separately
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

        # Raise an exception if the API call was unsuccessful
        if response.status_code != 200:
            raise Exception(f"Request failed with status code: {response.status_code}")

        # Save the speech to a temporary MP3 file and return the file path
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            tmpfile.write(response.content)
            files1 = tmpfile.name

        response = requests.post(
            "https://api.openai.com/v1/audio/speech",
            headers={"Authorization": f"Bearer {openai_key}"},
            json={"model": "tts-1", "input": partie2, "voice": voice}
        )

        # Raise an exception if the API call was unsuccessful
        if response.status_code != 200:
            raise Exception(f"Request failed with status code: {response.status_code}")

        # Save the speech to a temporary MP3 file and return the file path
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            tmpfile.write(response.content)
            files2 = tmpfile.name
        # Load each MP3 file as an AudioFileClip
        audio_clips = [AudioFileClip(files1) ,AudioFileClip(files2)]
        final_audio = concatenate_audioclips(audio_clips)

        # Write the final audio clip to the specified output file path
        final_audio.write_audiofile("mp3/final.mp3", codec='libmp3lame')

        # Close all the individual audio clips
        for clip in audio_clips:
            clip.close()
        lien = discord_storage.send_and_get_file_link("mp3/final.mp3")
        os.remove("mp3/final.mp3")
        return lien

    else:
        response = requests.post(
            "https://api.openai.com/v1/audio/speech",
            headers={"Authorization": f"Bearer {openai_key}"},
            json={"model": "tts-1", "input": texte, "voice": voice}
        )
        # Save the speech to a temporary MP3 file and return the file path
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
            tmpfile.write(response.content)
            lien = discord_storage.send_and_get_file_link(tmpfile.name)
            os.remove(tmpfile.name)
            return lien
