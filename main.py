from Package import sql
from Package import scrapper
from Package import TTS2
from Package import discord_storage

dict_theme = [
    {"Catégorie": "1", "Lien": "https://www.lemonde.fr/pixels/rss_full.xml"},
    {"Catégorie": "2", "Lien": "https://www.lemonde.fr/sport/rss_full.xml"},
    {"Catégorie": "3", "Lien": "https://www.lemonde.fr/politique/rss_full.xml"},
    {"Catégorie": "4", "Lien": "https://www.lemonde.fr/sciences/rss_full.xml"},
    {"Catégorie": "5", "Lien": "https://www.lemonde.fr/culture/rss_full.xml"}
]


def main():
    for categorie in dict_theme:
        a, c, d, f = scrapper.rss_collect(categorie["Lien"])
        e = TTS2.text_to_speech(a)
        sql.add(a, c, categorie["Catégorie"], d, e, f)


main()
