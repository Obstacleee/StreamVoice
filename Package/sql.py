import mysql.connector

cnx = mysql.connector.connect(user='admin', password='adminadmin',
                              host='dbactu.cfwaimucg5lz.eu-west-3.rds.amazonaws.com')
cursor = cnx.cursor()

def connection():

    return cnx

def add(contenu , dateDebut, ID_thématique , dateFin):
    cursor.execute("USE RSS")
    # Écrire la requête SQL
    query = "INSERT INTO actu (Contenu , DateDébut , ID_Thématique , DateFin) VALUES (%s , %s , %s, %s)"

    # Les données à insérer
    data = (contenu , dateDebut , ID_thématique , dateFin)
    # Exécuter la requête
    cursor.execute(query, data)

    # Valider les modifications
    cnx.commit()


def get_date(id):
    cursor.execute("USE RSS")
    # Écrire la requête SQL
    query = "SELECT DateFin FROM actu WHERE ID = %s"

    # Les données à insérer
    data = (id)
    # Exécuter la requête
    cursor.execute(query, data)
    table = cursor.fetchall()
    return table


def get_id_from_Contenu(Contenu):
    cursor.execute("USE RSS")
    # Écrire la requête SQL
    query = "SELECT ID FROM actu WHERE Contenu = %s"

    # Les données à insérer
    data = (Contenu)
    # Exécuter la requête
    cursor.execute(query, data)
    table = cursor.fetchall()
    return table


def get_Contenu_from_id(ID):
    cursor.execute("USE RSS")
    # Écrire la requête SQL
    query = "SELECT Contenu FROM actu WHERE ID = %s"

    # Les données à insérer
    data = (ID)
    # Exécuter la requête
    cursor.execute(query, data)
    table = cursor.fetchall()
    return table


def get_article():
    cursor.execute("USE RSS")
    query = "SELECT id, DateFin FROM actu ORDER BY DateFin DESC;"
    cursor.execute(query)
    table = cursor.fetchall()
    return table


def get(id):
    cursor.execute("USE RSS")
    # Écrire la requête SQL
    query = "SELECT * FROM actu WHERE ID_Thématique = %s"

    # Les données à insérer
    data = (id)
    # Exécuter la requête
    cursor.execute(query, data)
    table = cursor.fetchall()
    return table

