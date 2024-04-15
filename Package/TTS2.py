import pyttsx3 , os 
from Package import sql
from Package import cloud

def Text_to_spech(id):
    texte = sql.get_Contenu_from_id([id])
    texte = texte[0][0]
    print(texte)
    engine = pyttsx3.init()
    save= f"C:/Users/lucas/Desktop/projet rss/Projet-RSS/mp3/{id}.mp3"
    print(save)
    engine.save_to_file(texte, save)
    engine.runAndWait()
    cloud.upload(save , f"{str(id)}.mp3")
    os.remove(save)

 