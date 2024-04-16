import mysql.connector

cnx = mysql.connector.connect(user='yourss', password='rssTMTC31@',
                              host='mysql-yourss.alwaysdata.net')
cursor = cnx.cursor()

def connection():

    return cnx

def add(contenu , dateDebut, ID_thématique , dateFin , lien_audio):
    cursor.execute("USE yourss_db")
    # Écrire la requête SQL
    query = "INSERT INTO actu (Contenu , DateDébut , ID_Thématique , DateFin , lien_audio) VALUES (%s , %s , %s, %s , %s)"

    # Les données à insérer
    data = (contenu , dateDebut , ID_thématique , dateFin , lien_audio)
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
    query = "SELECT id, DateFin, lien_audio FROM actu ORDER BY DateFin DESC;"
    cursor.execute(query)
    table = cursor.fetchall()
    return table


def get(id):
    cursor.execute("USE yourss_db")
    # Écrire la requête SQL
    query = "SELECT * FROM actu WHERE ID_Thématique = %s"

    # Les données à insérer
    data = (id)
    # Exécuter la requête
    cursor.execute(query, data)
    table = cursor.fetchall()
    return table
