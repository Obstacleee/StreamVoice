import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='podcast')
cursor = cnx.cursor()

def connection():

    return cnx

def add(titre , contenue , lien, lang):
    
    # Écrire la requête SQL
    query = "INSERT INTO podcast_not (Titre, contenue, lien , lang) VALUES (%s, %s , %s, %s)"

    # Les données à insérer
    data = (titre, contenue, lien , lang)
    # Exécuter la requête
    cursor.execute(query, data)

    # Valider les modifications
    cnx.commit()

def remove(titre):
    query = "DELETE FROM podcast_not WHERE titre = %s"
    data = (titre, )

    # Exécuter la requête
    cursor.execute(query, data)

    # Valider les modifications
    cnx.commit()

def update(titre ,lien_transfo=None , lienficher=None ):
    if titre and lien_transfo and lienficher:
        query = "UPDATE podcast_not SET lientransfo = %s, lienficher = %s WHERE titre = %s"
        data = (lien_transfo, lienficher, titre)
        cursor.execute(query, data)
        cnx.commit()
        return f"Lien Ficher et tranfo modifier pour {lienficher} et {lienficher}"
    elif titre and lien_transfo:
        query = "UPDATE podcast_not SET lientransfo = %s WHERE titre = %s"
        data = (lien_transfo , titre)
        cursor.execute(query, data)
        cnx.commit()
        return f"Lien transfo modifier pour {lien_transfo}"
    elif titre and lienficher:
        query = "UPDATE podcast_not SET lienficher = %s WHERE titre = %s"
        data = (lien_transfo, lienficher, titre)
        cursor.execute(query, data)
        cnx.commit()
        return f"Lien Ficher modifier pour {lienficher}"
    else : 
        return "Erreur de syntage dans la fonction"
    # Exécuter la requête
    
def find(chiffre , titre):
    match chiffre:
        case 1:
            query = "SELECT contenue FROM podcast_not WHERE Titre = %s;"
            data = [titre]
        case 2:
            query = "SELECT lien FROM podcast_not WHERE Titre = %s;"
            data = [titre]
        case 3:
            query = "SELECT lang FROM podcast_not WHERE Titre = %s;"
            data = [titre]
        case 4:
            query = "SELECT lientransfo FROM podcast_not WHERE Titre = %s;"
            data = [titre]
        case 5:
            query = "SELECT lienficher FROM podcast_not WHERE Titre = %s;"
            data = [titre]
        

    # Exécuter la requête
    cursor.execute(query, data)

    # Récupérer tous les résultats
    results = cursor.fetchall()

    # Valider les modifications
    cnx.commit()

    # Afficher les résultats
    return results

def close():
    cnx.close()
    return close

#find(1, "CPI And Earnings On Tap")