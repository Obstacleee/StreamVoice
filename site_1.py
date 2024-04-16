from flask import Flask, render_template, request
from Package import sql
import datetime
import locale
from datetime import datetime as dt


locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.
@app.route('/test',methods=["POST","GET"])  
def test():
    return render_template("test.html")
@app.route('/',methods=["POST","GET"])  
def podcast():


    article_id_date_lien = sql.get_article()
    date_last = sql.get_last_date()
    date_last = date_last[0][2]
    print(date_last)
   

   # Conversion de la date en chaîne de caractères

    date_last = date_last.strftime("%d %B %Y")

   
   #recherche = request.form.get("search")

    date_search_min  = request.form.get("search")

    if date_search_min:
    
    # Convertir la chaîne de date en objet datetime
        try:
        
            date_search_min  = dt.strptime(date_search_min , "%Y-%m-%d")

            date_search_min = int(date_search_min.timestamp())

            date_search_max = date_search_min + 86400

        # Effectuer une recherche ou une action basée sur la date_object
        except ValueError:
        
        # Gérer l'erreur si la chaîne de date n'est pas au format attendu
            print("Format de date incorrect.")

    podcast_choisi = []

    for podcast in article_id_date_lien:

      if date_search_min:

         time_str = podcast[1].strftime("%d %B %Y")
         try:
               
               time_object = dt.strptime(time_str, "%d %B %Y")
               time_timestamp = int(time_object.timestamp())
               
               if time_timestamp >= date_search_min and time_timestamp < date_search_max:

                  podcast_choisi.append(podcast)

         except ValueError:
               
               print("Format de date incorrect :", time_str)

      else:
          
          podcast_choisi = article_id_date_lien

    print(podcast_choisi)
    return render_template("index.html",  date_last=date_last , sql=podcast_choisi)

if __name__ == '__main__':

   # Run the app server on localhost:4449

   app.run('localhost', 4449, debug=True)
