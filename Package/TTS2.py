import pyttsx3 , os 
from Package import discord_storage

def Text_to_spech(texte):
    
    print(texte)

    engine = pyttsx3.init()
    save= f"C:/Users/lucas/Desktop/projet rss/Projet-RSS/mp3/{texte[:8]}.mp3"
    engine.save_to_file(texte, save)
    engine.runAndWait()
    lien = discord_storage.send_and_get_file_link(save)
    os.remove(save)
    return lien
    


 