class articulo:
    def __init__(self, nombre):
        self._nombre = nombre

    def get_nom(self):
        return self._nombre

    def set_nom(self, nuevo_nombre):
        self._nombre = nuevo_nombre