from Package import sql 
from Package import scrapper 


lien = "https://www.forbes.com/sites/jjkinahan/2024/04/08/cpi-and-earnings-on-tap/?sh=64b3571a2cb5"
txt = scrapper.scraptxt(lien)
java = scrapper.supprimer_codes_css_js(txt)
strong = scrapper.supprimer_strong(java)
lang= scrapper.langue(lien)
titre = scrapper.titre(lien)

sql.remove(titre)

#sql.add(titre,strong,lien,lang)

#sql.find(1, "CPI And Earnings On Tap")
