class Categoria:
    
    def __init__(self, nom):

        self.nom = nom
        self.articles = []

    def get_nom(self):
        return self._nombrre
    
    def set_nom(self, nom):
        self.nom = nom

    def get_articles(self):
        return self.articles

    def add_articles(self, articles):
        self.articles.append(articles)
        return articles
    
    def delete_article(self, nom_article):
        for article in self.articles:
            if article.get_nom() == nom_article:
                self.articles.remove(article)
                return True
        return False
            
    def __str__(self):
        return f"Categoria: {self.nom}, Articles: {', '.join(articles.get_nom() for articles in self.articles)}"
