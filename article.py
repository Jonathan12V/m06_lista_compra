class Article:
    def __init__(self, nom):
        self._nom = nom

    def get_nom(self):
        return self._nom

    def set_nom(self, nou_nom):
        self._nom = nou_nom