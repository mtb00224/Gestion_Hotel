import requests

def connectionAPI(url):
    req = requests.get(url)
    resultat = req.json()
    return resultat.get("articles")


def envoieData(url, data):
    envoie = requests.post(url, data)
    return envoie

def dataDictionnaire(*elemnt):
    data = {
        "nom" : elemnt[0],
        "prenom" : elemnt[1],
        "telephone" : elemnt[2],
        "date_reserv"   : elemnt[3],
        "date_entree"   :   elemnt[4],
        "nuitee"        :   elemnt[5],
        "choix_etage"   : elemnt[6]
    }

    return data