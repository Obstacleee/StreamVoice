import schedule
from Package import sql 
from Package import scrapper 
import time
from Package import TTS2
from Package import discord_storage
dict_theme = [
    {"Catégorie":"1", "Lien":"https://www.lemonde.fr/pixels/rss_full.xml"},
    {"Catégorie":"2", "Lien":"https://www.lemonde.fr/sport/rss_full.xml"},
    {"Catégorie":"3", "Lien":"https://www.lemonde.fr/international/rss_full.xml"},
    {"Catégorie":"4", "Lien":"https://www.lemonde.fr/sciences/rss_full.xml"},
    {"Catégorie":"5", "Lien":"https://www.lemonde.fr/culture/rss_full.xml"}
]


#TTS2.Text_to_spech(26)
#sql.get(["4"])
# cloud.download("22.mp3", "22.mp3")
#t= sql.get_article()
#response = discord_storage.send_and_get_file_link("static/son/22.mp3")
#print(sql.get_categorie())
def job():
    for categorie in dict_theme: 
        a ,c ,d= scrapper.rss_collect(categorie["Lien"])
        e = TTS2.text_to_speech(a)
        sql.add(a,c,categorie["Catégorie"] , d ,e)
    return

schedule.every().day.at("12:04").do(job())

while True:
    schedule.run_pending()
    time.sleep(5) # wait one minute 
