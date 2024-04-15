import requests
from discord import SyncWebhook # Import SyncWebhook
import discord
webhook_link = 'https://discord.com/api/webhooks/1229419212444008478/QrQic988XoqowRULvfX5V7EVEetI3WL0tQoJ5XO923hMlF8CV7zoCNlV1dsd1tf28M_8'
def send_files(file_path):
    webhook = SyncWebhook.from_url(webhook_link) # Initializing webhook

    with open(file=file_path, mode='rb') as f:
        my_file = discord.File(f)

    webhook.send(username='RSS to Audio', file=my_file)