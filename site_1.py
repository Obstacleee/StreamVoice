from flask import Flask, render_template, request
from Package import sql
import datetime
import locale

locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/',methods=["POST","GET"])  
def podcast():

   article_id_date = sql.get_article()
   date_last = sql.get_date([16])
   date_last = date_last[0][0]
   
   # Conversion de la date en chaîne de caractères
   date_last = date_last.strftime("%d %B %Y")

   #recherche = request.form.get("search")


   return render_template("index.html",  date_last=date_last , sql=article_id_date)

if __name__ == '__main__':
   # Run the app server on localhost:4449
   app.run('localhost', 4449, debug=True)
