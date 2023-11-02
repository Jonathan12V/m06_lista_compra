from registre import Registre
class Llista:
    def __init__(self):
        self.registres = []
        self.categories = []

    def get_registre(self):
        return Registre
    
    def create_registre(self, registre):
        self.registres.append(registre)
        return registre
    

    def read_registre(self, nom_article):

        for registre in self.registres:
            if registre.article.get_nom() == nom_article:
                return registre

    def update_registre(self, registre):
        for i, r in enumerate(registre):
           if r.get_nom() == registre.get_nom():
               self.registres[i] = registre
        
    def delete_registre(self, nom_article):
        for registre in self.registres:
            if registre.article.get_nom() == nom_article:
                self.registres.remove(registre)
                
    def create_categoria(self, categoria):
        self.categories.append(categoria)
        return categoria
    
    def update_categoria(self, categoria):
        for i, c in enumerate(categoria):
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
    