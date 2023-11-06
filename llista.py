from registre import Registre
from article import Article
from categoria import Categoria
import json

class Llista:
    def __init__(self):
        self.registres = []
        self.categories = []

    def get_registres(self):
        return self.registres
    
    def create_registre(self, registre):
        self.registres.append(registre)
        return registre
    

    def read_registre(self, nom_article):

        for registre in self.registres:
            if registre.article.get_nom() == nom_article:
                return registre

    def update_registre(self, registre):
        for i, r in enumerate(self.registres):
           if r.article.get_nom() == registre.article.get_nom():
               self.registres[i] = registre
        
    def delete_registre(self, nom_article):
        for registre in self.registres:
            if registre.article.get_nom() == nom_article:
                self.registres.remove(registre)
                
    def create_categoria(self, categoria):
        self.categories.append(categoria)
        return categoria
    
    def update_categoria(self, categoria):
        for i, c in enumerate(self.categories):
            if c.get_nom() == categoria.get_nom():
                self.categories[i] = categoria
 
    def read_categoria(self, nom_categoria):
        for categoria in self.categories:
            if categoria.get_nom() == nom_categoria:
                return categoria
    
    def delete_categoria(self, nom_categoria):
        for categoria in self.categories:
            if categoria.get_nom() == nom_categoria:
                self.categories.remove(categoria)
    
   
    def desa_a_disc(self):
        data = {
            "registres": [
                {
                    "article": registre.article.get_nom(),
                    "quantitat": registre.quantitat
                } for registre in self.registres
            ],
            "categories": [
                {
                    "nom": categoria.get_nom(),
                    "articles": [article.get_nom() for article in categoria.get_articles()]
                } for categoria in self.categories
            ]
        }

        with open("llista.json", "w") as file:
            json.dump(data, file, indent=3)


    def llegeix_de_disc(self):
        with open("llista.json", "r") as file:
            data = json.load(file)

        for item in data["registres"]:
            nom_article = item["article"]
            quantitat = item["quantitat"]
            article = Article(nom_article)
            registre = Registre(article, quantitat)
            self.create_registre(registre)

        for nom_categoria in data["categories"]:
            categoria = Categoria(nom_categoria)
            self.create_categoria(categoria)

