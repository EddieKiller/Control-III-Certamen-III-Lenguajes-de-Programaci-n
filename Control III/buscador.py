# Fonction pour charger l'indice inversé nettoyé des stopwords
def load_inverted_index(file_path):
    inverted_index = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Chaque ligne doit être du format : mot: url1, url2, url3
            if ": " in line:
                word, urls = line.strip().split(": ", 1)
                inverted_index[word] = urls.split(", ")
    return inverted_index

# Fonction récursive pour effectuer l'intersection des listes d'URLs
def intersect_lists(lists, index=0):
    if index == len(lists) - 1:
        return set(lists[index])
    return set(lists[index]).intersection(intersect_lists(lists, index + 1))

# Fonction pour effectuer une recherche dans l'indice inversé
def search_inverted_index(inverted_index, query):
    terms = query.lower().split()  # Diviser la requête utilisateur en mots-clés
    lists = []

    for term in terms:
        if term in inverted_index:
            lists.append(inverted_index[term])
        else:
            return []  # Aucun résultat si un terme est absent

    return list(intersect_lists(lists)) if lists else []


def process_queries_from_file(inverted_index, query_file, output_file):
    with open(query_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            query = line.strip()
            results = search_inverted_index(inverted_index, query)
            outfile.write(f"Query: {query}\n")
            if results:
                outfile.write("Results:\n")
                for url in results:
                    outfile.write(f"- {url}\n")
            else:
                outfile.write("No results found.\n")
            outfile.write("\n")
            
# Programme principal
def main():
    # Charger l'indice inversé depuis le fichier nettoyé
    index_file = "cleaned_file.txt"  # Remplacez par le chemin vers votre fichier
    inverted_index = load_inverted_index(index_file)

    print("Moteur de recherche chargé avec succès.")
    print("Tapez 'file' pour utiliser un fichier de requêtes, ou entrez vos termes de recherche directement.")
    print("Tapez 'exit' pour quitter.")

    while True:
        query = input("Recherche : ")
        if query.lower() == "exit":
            print("Au revoir!")
            break

        if query.lower() == "file":
            # Traiter les requêtes depuis un fichier
            query_file = "queries.txt"  # Fichier contenant les requêtes
            result_file = "results.txt"  # Fichier où stocker les résultats

            print(f"Traitement des requêtes depuis le fichier {query_file}...")
            with open(query_file, 'r') as infile, open(result_file, 'w') as outfile:
                for line in infile:
                    words = line.strip().split()  # Diviser les mots dans chaque ligne
                    for word in words:
                        results = search_inverted_index(inverted_index, word)
                        outfile.write(f"Query: {word}\n")
                        if results:
                            outfile.write("Results:\n")
                            for url in results:
                                outfile.write(f"- {url}\n")
                        else:
                            outfile.write("No results found.\n")
                        outfile.write("\n")
            print(f"Résultats sauvegardés dans {result_file}.")
        else:
            # Traiter une requête unique entrée par l'utilisateur
            results = search_inverted_index(inverted_index, query)
            if results:
                print("Résultats trouvés :")
                for url in results:
                    print(f"- {url}")
            else:
                print("Aucun résultat trouvé.")

if __name__ == "__main__":
    main()