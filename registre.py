class Registre:
    def __init__(self, article, quantitat):
        self.article = article
        self.quantitat = quantitat

    def get_quantitat(self):
        return self.quantitat

    def set_quantitat(self, quantitat):
        self.quantitat = quantitat