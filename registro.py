class registro:
    def __init__(self, articulo, cantidad):
        self.articulo = articulo
        self.cantidad = cantidad

    def get_quantitat(self):
        return self.cantidad

    def set_nom(self, nueva_cantidad):
        self.cantidad = nueva_cantidad