from flask import Flask, render_template, request
from Package import sql
import datetime
from datetime import datetime as dt

# Configuration de la locale pour les dates en français
import locale
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def podcast():
    categorie = sql.get_categorie()

    article_id_date_lien = sql.get_article()
    
    date_last = sql.get_last_date()
    date_last = date_last[0][2]  # Assurez-vous que cette ligne extrait correctement la date

    # Conversion de la date en chaîne de caractères
    date_last_str = date_last.strftime("%d %B %Y")

    # Initialisation des variables pour la recherche
    date_search_min = request.form.get("search")
    choix_categorie = request.form.get("categorie")

    podcast_choisi = []

    if choix_categorie:
        podcast_categorie = sql.get([choix_categorie])
    else:
        podcast_categorie = article_id_date_lien

    date_search_max = None
    if date_search_min:
        try:
            date_search_min = dt.strptime(date_search_min, "%Y-%m-%d")
            date_search_min = int(date_search_min.timestamp())
            date_search_max = date_search_min + 86400
        except ValueError:
            print("Format de date incorrect.")
    
    if date_search_min and date_search_max:
        for podcast in podcast_categorie:
            podcast_date = podcast[1]
            if isinstance(podcast_date, datetime.datetime):
                podcast_timestamp = int(podcast_date.timestamp())
                if date_search_min <= podcast_timestamp < date_search_max:
                    podcast_choisi.append(podcast)
    else:
        podcast_choisi= podcast_categorie
        
    return render_template("index.html", date_last=date_last_str, sql=podcast_choisi, categorie=categorie)

if __name__ == '__main__':
    app.run('localhost', 4449, debug=True)
