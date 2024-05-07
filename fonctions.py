import requests, json, ipaddress
from flask import request

def get_headers():

    ip = []

    for i in range(0, 4):
        ip.append(random.randint(0, 254))

    random_ip = ''
    for i in range(0, 3):
        random_ip += str(ip[i]) + '.'

    random_ip += str(ip[3])

    headers = {"X-Forwarded-For": random_ip}

    return headers

class Livre:
    def __init__(self, title, author, publish, isbn, img_url):
        self.title = title
        self.author = author
        self.publish = publish
        self.isbn = isbn
        self.img_url = img_url

def get_books():

    livres = []
    headers = get_headers()
    
    # La condition if permet de n'afficher du contenue de l'API que lorsqu'il y a une requête qui est effectué.
    if request.method == "POST":
        choix = request.form["choix"]
        
        # Concaténations a l'url de l'API du choix de l'utilisateur reçu via request.form et on choisi les informations que nous souhaitons récuperer.
        url = "https://openlibrary.org/search.json?q=" + choix + "&fields=title,author_name,first_publish_year,isbn"
        response = requests.get(url, headers)
        
        # Transformation des données reçu de l'API en objet JSON pour les avoir sous forme clé/valeur.
        datas = json.loads(response.text)

        for e in datas["docs"]:
            # A l'aide du constructeur de la classe Livre on affine les données reçu et on concaténe isbn a l'url images. 
            livre = Livre(e["title"], e["author_name"][0], e["first_publish_year"], e["isbn"][0], "https://covers.openlibrary.org/b/isbn/" + e["isbn"][0] + "-L.jpg")
    
            # Informations ajouté au dictionnaire livres definit plus haut.
            livres.append(livre)
    else:
        print("Pas de requête effectué")
        livres.append("No datas")

    return livres