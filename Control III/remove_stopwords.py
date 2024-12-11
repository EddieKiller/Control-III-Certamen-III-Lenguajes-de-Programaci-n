import re

# Liste des stopwords
stopwords = [
  "a", "an", "the",
  "I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them", "my", "your", "his", "her", "its", "our", "their", "mine", "yours", "theirs",
  "and", "but", "or", "so", "yet", "for", "nor",
  "about", "above", "across", "after", "against", "along", "among", "around", "at", "before", "behind", "below", "beneath", "beside", "between", "beyond", "by", "down", "during", "except", "for", "from", "in", "into", "like", "near", "of", "off", "on", "over", "since", "through", "to", "toward", "under", "until", "up", "upon", "with", "within", "without",
  "am", "are", "is", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "shall", "should", "will", "would", "can", "could", "may", "might", "must",
  "how", "when", "where", "why", "now", "then", "there", "here", "again", "once", "all", "any", "both", "each", "every", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very",
  "if", "because", "as", "until", "while", "of", "with", "at", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once"
]

# Fonction pour vérifier si une ligne contient un stopword
def contains_stopwords(line, stopwords):
    words = re.split(r'\W+', line)  # Séparer les mots par des délimiteurs non-alphanumériques
    return any(word.lower() in stopwords for word in words)

# Fichiers d'entrée et de sortie
input_file = "inverted_index.txt"  # Remplacez par le nom du fichier d'entrée
output_file = "cleaned_file.txt"
log_file = "removed_lines_log.txt"

# Traitement du fichier
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile, open(log_file, 'w') as logfile:
    for line in infile:
        if contains_stopwords(line, stopwords):
            # Loguer la ligne supprimée
            logfile.write(f"stopword borrada : {line}")
        else:
            # Écrire la ligne sans stopwords
            outfile.write(line)

print(f"Traitement terminé. Lignes restantes enregistrées dans {output_file}. Lignes supprimées enregistrées dans {log_file}.")