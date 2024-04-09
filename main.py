from Package import sql 
from Package import scrapper 
from Package import cloud

dict_theme = [
    {"Catégorie":"1", "Lien":"https://www.lemonde.fr/pixels/rss_full.xml"},
    {"Catégorie":"2", "Lien":"https://www.lemonde.fr/sport/rss_full.xml"},
    {"Catégorie":"3", "Lien":"https://www.lemonde.fr/international/rss_full.xml"},
    {"Catégorie":"4", "Lien":"https://www.lemonde.fr/sciences/rss_full.xml"},
    {"Catégorie":"5", "Lien":"https://www.lemonde.fr/culture/rss_full.xml"}
]

# for categorie in dict_theme: 
#     a ,c ,d= scrapper.rss_collect(categorie["Lien"])
#     sql.add(a,c,categorie["Catégorie"] , d)
    
#sql.get(["4"])
cloud.download("save.mp3", "tets.mp3")


