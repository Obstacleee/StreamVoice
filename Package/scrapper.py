import requests
from bs4 import BeautifulSoup
import re
import feedparser
#https://rss.app/feeds/lZUHcLwGD5mIZaFT.xml

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
#avec le feed rss il récupére les liens pour les exploiter
def rss_collect(feed):

    news_feed = feedparser.parse(feed)


    entries = []
    for entry in news_feed.entries:
        entries.append(entry.link)
    
    return entries


#Récupere le code source de la page (brut)
def scraptxt(lien):

    page = requests.get(lien, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    return str(soup)

#Supprime tout le code css ou javaScript qui est en trop  
def supprimer_codes_css_js(texte):

    texte = re.sub(r'<style.*?</style>', '', texte, flags=re.DOTALL)
    texte = re.sub(r'<a.*?</a>', '', texte, flags=re.DOTALL)
    texte = re.sub(r'<script.*?</script>', '', texte, flags=re.DOTALL)

    return texte

#Récupere que le texte en titre et en liste (obsoléte)
def recuperer_contenu_p_h2_et_ol(texte):
    # Use regex to find all content between <p>, <h2> and <li> tags
    contenu = re.findall(r'<p>(.*?)</p>|<h2.*?>(.*?)</h2>|<ol.*?><li>(.*?)</li></ol>', texte, flags=re.DOTALL)
    # Join all the content found into a single string, placing <h2> and <li> content at the right place

    contenu = ' '.join([item for sublist in contenu for item in sublist if item])
    
    return contenu

# Récupere tout le texte visible a l'écran qui n'est pas compris entre <> . 
def supprimer_strong(texte):
    texte = re.sub(r'<.*?>', '', texte, flags=re.DOTALL)

    return texte

# Récupere la langue de l'article 
def langue(lien):
    page = requests.get(lien, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    soup = str(soup)
    pattern = r'("en"|"fr"|"es"|"ru")'
    resultats = re.search(pattern, soup)

    if resultats:
        langue = resultats.group(1).replace('"', '')  
        return langue
    else:
        return None
    
def titre(lien):
    page = requests.get(lien, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    Titre = soup.title.string
    return Titre

