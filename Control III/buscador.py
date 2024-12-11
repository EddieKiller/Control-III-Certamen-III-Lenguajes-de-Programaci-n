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

# Fonction pour effectuer une recherche dans l'indice inversé
def search_inverted_index(inverted_index, query):
    terms = query.lower().split()  # Diviser la requête utilisateur en mots-clés
    results = None

    for term in terms:
        if term in inverted_index:
            if results is None:
                results = set(inverted_index[term])  # Initialiser avec les résultats du premier mot
            else:
                results.intersection_update(inverted_index[term])  # Intersection avec les résultats précédents
        else:
            return []  # Aucun résultat si un mot-clé est absent

    return list(results) if results else []

# Programme principal
def main():
    # Charger l'indice inversé depuis le fichier nettoyé
    index_file = "cleaned_file.txt"  # Remplacez par le chemin vers votre fichier
    inverted_index = load_inverted_index(index_file)

    print("Moteur de recherche chargé avec succès.")
    print("Tapez vos termes de recherche (séparés par des espaces). Tapez 'exit' pour quitter.")

    while True:
        query = input("Recherche : ")
        if query.lower() == "exit":
            print("Au revoir!")
            break

        results = search_inverted_index(inverted_index, query)
        if results:
            print("Résultats trouvés :")
            for url in results:
                print(f"- {url}")
        else:
            print("Aucun résultat trouvé.")

if __name__ == "__main__":
    main()