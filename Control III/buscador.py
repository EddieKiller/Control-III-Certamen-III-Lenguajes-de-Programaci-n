# Función para cargar el índice invertido limpiado de stopwords
def load_inverted_index(file_path):
    inverted_index = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Cada línea debe tener el formato: palabra: url1, url2, url3
            if ": " in line:
                word, urls = line.strip().split(": ", 1)
                inverted_index[word] = urls.split(", ")
    return inverted_index

# Función recursiva para realizar la intersección de las listas de URLs
def intersect_lists(lists, index=0):
    if index == len(lists) - 1:
        return set(lists[index])
    return set(lists[index]).intersection(intersect_lists(lists, index + 1))

# Función para realizar una búsqueda en el índice invertido
def search_inverted_index(inverted_index, query):
    terms = query.lower().split()  # Dividir la consulta del usuario en palabras clave
    lists = []

    for term in terms:
        if term in inverted_index:
            lists.append(inverted_index[term])
        else:
            return []  # Ningún resultado si falta un término

    return list(intersect_lists(lists)) if lists else []


def process_queries_from_file(inverted_index, query_file, output_file):
    with open(query_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            query = line.strip()
            results = search_inverted_index(inverted_index, query)
            outfile.write(f"Consulta: {query}\n")
            if results:
                outfile.write("Resultados:\n")
                for url in results:
                    outfile.write(f"- {url}\n")
            else:
                outfile.write("No se encontraron resultados.\n")
            outfile.write("\n")
            
# Programa principal
def main():
    # Cargar el índice invertido desde el archivo limpiado
    index_file = "cleaned_file.txt"  # Reemplace con la ruta a su archivo
    inverted_index = load_inverted_index(index_file)

    print("Motor de búsqueda cargado con éxito.")
    print("Escriba 'file' para usar un archivo de consultas, o ingrese sus términos de búsqueda directamente.")
    print("Escriba 'exit' para salir.")

    while True:
        query = input("Búsqueda: ")
        if query.lower() == "exit":
            print("¡Adiós!")
            break

        if query.lower() == "file":
            # Procesar consultas desde un archivo
            query_file = "queries.txt"  # Archivo que contiene las consultas
            result_file = "results.txt"  # Archivo donde almacenar los resultados

            print(f"Procesando consultas desde el archivo {query_file}...")
            with open(query_file, 'r') as infile, open(result_file, 'w') as outfile:
                for line in infile:
                    words = line.strip().split()  # Dividir las palabras en cada línea
                    for word in words:
                        results = search_inverted_index(inverted_index, word)
                        outfile.write(f"Consulta: {word}\n")
                        if results:
                            outfile.write("Resultados:\n")
                            for url in results:
                                outfile.write(f"- {url}\n")
                        else:
                            outfile.write("No se encontraron resultados.\n")
                        outfile.write("\n")
            print(f"Resultados guardados en {result_file}.")
        else:
            # Procesar una consulta única ingresada por el usuario
            results = search_inverted_index(inverted_index, query)
            if results:
                print("Resultados encontrados:")
                for url in results:
                    print(f"- {url}")
            else:
                print("No se encontraron resultados.")

if __name__ == "__main__":
    main()
