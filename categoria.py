from articulo import articulo
class categoria():
    
    def __init__(self, nombre):

        self.nombre = nombre
        self.articulos = []

    def get_nombre(self):
        return self._nombrre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_articulos(self):
        return self.articulos

    def add_articulos(self, articulos):
        self.articulos.append(articulos)
        return articulos
    
    def delete_article(self, nom_article):
        for article in self.articulos:
            if article.get_nom() == nom_article:
                self.articulos.remove(article)
                return True
        return False
            
    def __str__(self):
        return f"Categoria: {self.nombre}, Articulos: {', '.join(articulo.get_nom() for articulo in self.articulos)}"