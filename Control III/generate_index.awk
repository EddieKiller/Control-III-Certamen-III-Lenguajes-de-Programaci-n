#!/usr/bin/awk -f

BEGIN {
    FS = "\\|\\|"; # Définir le séparateur pour détecter les délimitations
    output_file = "inverted_index.txt";
    debug_file = "debug_log.txt";
    print "Démarrage du traitement des données..." > debug_file;
}

{
    # Vérifier qu'il y a au moins deux champs séparés par '||'
    if (NF < 2) {
        print "Erreur : Ligne mal formatée, ignorée : " $0 >> debug_file;
        next;
    }

    # L'URL est composée des colonnes avant le dernier champ
    url = $1;
    for (i = 2; i < NF; i++) {
        url = url "||" $i;
    }

    # Le contenu est la dernière colonne
    content = $NF;

    # Vérification de l'URL
    if (url == "" || content == "") {
        print "Erreur : URL ou contenu vide pour la ligne : " $0 >> debug_file;
        next;
    }

    print "URL traitée : " url >> debug_file;

    # Diviser le contenu en mots
    n = split(content, words, /[^a-zA-Z0-9]+/);

    for (i = 1; i <= n; i++) {
        word = tolower(words[i]); # Convertir en minuscule pour uniformité

        if (word != "" && length(word) > 1) { # Ignorer les mots vides ou trop courts
            # Ajouter l'URL à la liste pour ce mot
            if (!(word in inverted_index)) {
                inverted_index[word] = url;
            } else {
                if (index(inverted_index[word], url) == 0) {
                    inverted_index[word] = inverted_index[word] ", " url;
                }
            }
            print "Mot : " word ", URL ajoutée : " url >> debug_file;
        }
    }
}

END {
    print "Écriture de l'indice inversé dans un fichier unique..." >> debug_file;

    # Écrire l'indice inversé dans un fichier
    for (word in inverted_index) {
        print word ": " inverted_index[word] >> output_file;
    }

    close(output_file);
    print "Indice inversé généré avec succès dans " output_file;
    print "Journal de débogage disponible dans " debug_file;
}