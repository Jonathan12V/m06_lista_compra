from llista import Llista
from article import Article
from categoria import Categoria
from registre import Registre

def main():
    # Crear instancias de Article, Categoria y Registre
    article_1 = Article("cocacola")
    article_2 = Article("fanta")
    categoria_1 = Categoria("Bebidas")
    registre_1 = Registre(article_1, 3)
    registre_2 = Registre(article_2, 10)

    # Crear una instancia de la clase Llista
    lista = Llista()

    # Probando los métodos de la clase Llista
    # Agregar registros
    lista.create_registre(registre_1)
    lista.create_registre(registre_2)

    print("Registros creados:")
    for registre in lista.registres:
        print(registre.article.get_nom(), registre.get_quantitat())

    # Obtener registros
    print(f"\nIntentando obtener registro '{article_1.get_nom()}':")
    registro_obtenido = lista.read_registre("cocacola")
    print("Registro obtenido:", registro_obtenido.get_quantitat())  # Imprimir la cantidad del registro obtenido

    # Eliminar registros
    print("\nEliminando el registro 'Artículo 2':")
    lista.delete_registre("Artículo 2")
    print("Registros restantes:")
    for registre in lista.registres:
        print(registre.article.get_nom(), registre.get_quantitat())

    # Crear categorías
    lista.create_categoria(categoria_1)

    print("\nCategoría creada:", categoria_1.get_nom())

    # Obtener categorías
    print("\nIntentando obtener categoría 'Categoría 1':")
    categoria_obtenida = lista.read_categoria("Categoría 1")
    print("Categoría obtenida:", categoria_obtenida)  # Imprimir la categoría obtenida

    # Eliminar categorías
    print("\nEliminando la categoría 'Nueva Categoría':")
    lista.delete_categoria("Nueva Categoría")

    #

main()