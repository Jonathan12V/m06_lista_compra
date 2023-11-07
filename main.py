from llista import Llista
from article import Article
from categoria import Categoria
from registre import Registre

def main():
    # Lista con todas las categorias
    categorias = [
        # Categorias Predefinidas
        Categoria("Frescos"),
        Categoria("Begudes"),
        Categoria("Lactis"),
        Categoria("Neteja"),
        Categoria("Fruita i verdures"),
        # Categorias creadas despues
        Categoria("Begudes"),
        Categoria("Almacen")
    ]

    # Lista con todos los articulos
    articles = [
        Article("cocacola"),
        Article("fanta"),
        Article("manzana"),
        Article("leche"),
        Article("pan"),
        Article("agua"),
        Article("detergente"),
        Article("zanahoria"),
        Article("naranja")
    ]

    # Lista con todos los registros
    registros = [
        Registre(articles[0], 3),
        Registre(articles[1], 6),
        Registre(articles[2], 2),
        Registre(articles[3], 1),
        Registre(articles[4], 8),
        Registre(articles[5], 2),
        Registre(articles[6], 5),
        Registre(articles[7], 3),
        Registre(articles[8], 9),
    ]

    # Crear una instancia de la clase Llista
    lista = Llista()

    # Probando los métodos de la clase Llista
    # Agregar registros
    for i in range(len(registros)):
        lista.create_registre(registros[i])

    print("\n------ Registros Creados ------")
    print("Registros creados:")
    print("Articulos".ljust(13) + "Cantidad")
    for registre in lista.registres:
        print(registre.article.get_nom().ljust(13) + str(registre.get_quantitat()))

    # Obtener registros
    print("\n------ Obtener Registro ------")
    registro_obtenido = lista.read_registre("fanta")
    print(f"Intentando obtener registro '{registro_obtenido.article.get_nom()}':")
    print("Registro obtenido:", registro_obtenido.get_quantitat())  # Imprimir la cantidad del registro obtenido

    # Actualizar Registro
    print("\n------ Actualizar Registro ------")
    nuevo_registro = Registre(articles[1], 15)
    lista.update_registre(nuevo_registro)
    print(f"Registro '{nuevo_registro.article.get_nom()}' actualizado a {nuevo_registro.get_quantitat()}")
    print("Categoria".ljust(13) + "Cantidad")
    for registre in lista.registres:
        print(registre.article.get_nom().ljust(13) + str(registre.get_quantitat()))

    # Eliminar registros
    print("\n------ Eliminando Registro ------")
    print(f"Eliminando el registro '{registro_obtenido.article.get_nom()}':")
    
    lista.delete_registre("fanta")
    print("Registros restantes:")
    print("Categoria".ljust(13) + "Cantidad")
    for registre in lista.registres:
        print(registre.article.get_nom().ljust(13) + str(registre.get_quantitat()))

    print("\n------ Creación de Categoria ------")
    # Crear un conjunto para rastrear los nombres de categorías existentes
    nombres_categorias = set()
    # Iterar sobre las categorías
    for categoria in categorias:
        if categoria.get_nom() not in nombres_categorias:
            lista.create_categoria(categoria)
            nombres_categorias.add(categoria.get_nom())
        else:
            print(f"La categoría '{categoria.get_nom()}' ya existe. No se ha creado.")

    # Agregar artículos a categorías
    lista.read_categoria("Begudes").add_articles(articles[0])
    lista.read_categoria("Begudes").add_articles(articles[1])
    lista.read_categoria("Frescos").add_articles(articles[2])
    lista.read_categoria("Lactis").add_articles(articles[3])
    lista.read_categoria("Frescos").add_articles(articles[4])
    lista.read_categoria("Begudes").add_articles(articles[5])
    lista.read_categoria("Neteja").add_articles(articles[6])
    lista.read_categoria("Fruita i verdures").add_articles(articles[7])
    lista.read_categoria("Fruita i verdures").add_articles(articles[8])
    lista.read_categoria("Almacen").add_articles(articles[8])

    # Obtener categorías
    print("\n------ Obtener Categoria ------")
    for categoria in categorias: 
        print("Intentando obtener categoria:", categoria)

    # Actualizar Categoria
    print("\n------ Actualizar Categoria ------")
    categoria_a_actualizar = Categoria("Refrescos")
    lista.update_categoria(categoria_a_actualizar)
    print(f"Categoria '{categoria_a_actualizar.get_nom()}'")

    # Eliminar categoría
    print("\n------ Eliminando Categoria ------")
    print(f"Eliminando la categoría '{categoria.get_nom()}':")
    lista.delete_categoria("Bebidas")

    # Invocar el método desa_a_disc para guardar los datos en un archivo
    lista.desa_a_disc()

    # Crear una nueva instancia de la lista para simular la lectura de los datos desde el archivo
    lista_nueva = Llista()

    # Invocar el método llegeix_de_disc para leer los datos del archivo
    lista_nueva.llegeix_de_disc()

    # Verificar si los datos se han recuperado correctamente
    print("\n------ Datos recuperados desde el archivo ------")
    print("Registros recuperados:")
    print("Articulo".ljust(13) + "Cantidad")
    for registre in lista_nueva.registres:
        print(registre.article.get_nom().ljust(13) + str(registre.get_quantitat()))

    print("\nCategorías recuperadas:")
    for categoria in lista_nueva.categories:
        print("Categoría:", categoria.get_nom())
    
if __name__ == "__main__":
    main()