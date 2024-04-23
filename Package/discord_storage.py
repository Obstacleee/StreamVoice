from discord import SyncWebhook, File
import os
from dotenv import load_dotenv

load_dotenv()

webhook = os.getenv('WEEBHOOK')

def send_and_get_file_link(file_path):
    webhook = os.getenv('WEEBHOOK')
    webhook = SyncWebhook.from_url(webhook)

    try:
        with open(file_path, 'rb') as f:
            my_file = File(f)
            response = webhook.send(file=my_file, wait=True)
    except Exception as e:
        print(f'Erreur lors de l\'envoi du fichier : {str(e)}')
        return None

    if response and response.attachments:
        file_url = response.attachments[0].url  # Obtenez l'URL du premier attachement
        return file_url
    else:
        print('Aucune réponse du serveur Discord ou pas d\'attachements dans la réponse.')
        return None