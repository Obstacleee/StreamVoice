import requests
from discord import SyncWebhook, File
import time

webhook_link = 'https://discord.com/api/webhooks/1229419212444008478/QrQic988XoqowRULvfX5V7EVEetI3WL0tQoJ5XO923hMlF8CV7zoCNlV1dsd1tf28M_8'

def send_and_get_file_link(file_path):
    webhook = SyncWebhook.from_url(webhook_link)

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