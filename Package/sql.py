import mysql.connector
import os

user_bd = os.getenv('USER_BD')
password_bd = os.getenv('PASSWORD_BD')
host_bd = os.getenv('HOST_BD')

cnx = mysql.connector.connect(user=user_bd, password=password_bd,
                            host=host_bd)
cursor = cnx.cursor()

def connection():

    return cnx

def add(contenu , dateDebut, ID_thématique , dateFin , lien_audio , lien_site):
    cursor.execute("USE yourss_db")
    # Écrire la requête SQL
    query = "INSERT INTO actu (Contenu , DateDébut , ID_Thématique , DateFin , lien_audio, lien_site) VALUES (%s , %s , %s, %s , %s, %s)"

    # Les données à insérer
    data = (contenu , dateDebut , ID_thématique , dateFin , lien_audio , lien_site)
    # Exécuter la requête
    cursor.execute(query, data)

    # Valider les modifications
    cnx.commit()


def get_last_date():
    cursor.execute("USE yourss_db")
    # Écrire la requête SQL
    query = "SELECT * FROM `actu` ORDER BY `actu`.`DateFin` DESC LIMIT 1"

    
    # Exécuter la requête
    cursor.execute(query)
    table = cursor.fetchall()
    return table


def get_id_from_Contenu(Contenu):
    cursor.execute("USE yourss_db")
    # Écrire la requête SQL
    query = "SELECT ID FROM actu WHERE Contenu = %s"

    # Les données à insérer
    data = (Contenu)
    # Exécuter la requête
    cursor.execute(query, data)
    table = cursor.fetchall()
    return table


def get_Contenu_from_id(ID):
    cursor.execute("USE yourss_db")
    # Écrire la requête SQL
    query = "SELECT Contenu FROM actu WHERE ID = %s"

    # Les données à insérer
    data = (ID)
    # Exécuter la requête
    cursor.execute(query, data)
    table = cursor.fetchall()
    return table


def get_article():
    cursor.execute("USE yourss_db")
    query = "SELECT id, DateFin, lien_audio , ID_Thématique , lien_site FROM actu ORDER BY DateFin DESC;"
    cursor.execute(query)
    table = cursor.fetchall()
    return table

def get_categorie():
    cursor.execute("USE yourss_db")
    query ="SELECT ID_Thématique, Thématique FROM categorie"
    cursor.execute(query)
    table = cursor.fetchall()
    return table
def get(id):
    cursor.execute("USE yourss_db")
    # Écrire la requête SQL
    query = "SELECT id, DateFin, lien_audio , ID_Thématique , lien_site FROM actu WHERE ID_Thématique = %s ORDER BY DateFin DESC "

    # Les données à insérer
    data = (id)
    # Exécuter la requête
    cursor.execute(query, data)
    table = cursor.fetchall()
    return table

