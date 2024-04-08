from flask import Flask, render_template, request

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/',methods=["POST","GET"])  
def podcast():
   musique=[
   {"titre": "lucas", "musique":"Ayana" , "Nom":"dada", "lang":"fr"},
   {"titre": "lucas", "musique":"denjfe" , "Nom":"ddd", "lang":"fr"},
   {"titre": "delon", "musique":"dnzd" , "Nom":"fjefe", "lang":"en"}
   ]
   langue = request.form.get("lang")
   
   recherche = request.form.get("search")
   print(langue,recherche  )

   if langue == "all" and recherche is None:
      musique_selec = musique
   elif langue == "all" and recherche:
      musique_selec = [musiq for musiq in musique if  musiq["titre"].lower() == recherche.lower()]
   elif langue is not None and langue != "all" and recherche:
      musique_selec = [musiq for musiq in musique if musiq["lang"] == langue and recherche.lower() in musiq["titre"].lower()]
   else:
      musique_selec = musique

   return render_template("index.html", podcas=musique_selec)

if __name__ == '__main__':
   # Run the app server on localhost:4449
   app.run('localhost', 4449, debug=True)
