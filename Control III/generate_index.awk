#!/usr/bin/awk -f

BEGIN {
    FS = "\\|\\|"; # Definir el separador para detectar las delimitaciones
    output_file = "inverted_index.txt";
}

{
    # La URL está compuesta por las columnas antes del último campo
    url = $1;
    for (i = 2; i < NF; i++) {
        url = url "||" $i;
    }

    # El contenido es la última columna
    content = $NF;

    # Verificación de la URL
    if (url == "" || content == "") {
        next;
    }


    # Dividir el contenido en palabras
    n = split(content, words, /[^a-zA-Z0-9]+/);

    for (i = 1; i <= n; i++) {
        word = tolower(words[i]); # Convertir a minúsculas para uniformidad

        if (word != "" && length(word) > 1) { # Ignorar palabras vacías o demasiado cortas
            # Añadir la URL a la lista para esta palabra
            if (!(word in inverted_index)) {
                inverted_index[word] = url;
            } else {
                if (index(inverted_index[word], url) == 0) {
                    inverted_index[word] = inverted_index[word] ", " url;
                }
            }
        }
    }
}

END {

    # Escribir el índice invertido en un archivo
    for (word in inverted_index) {
        print word ": " inverted_index[word] >> output_file;
    }

    close(output_file);
    print "Índice invertido generado con éxito en " output_file;
    print "Registro de depuración disponible en " debug_file;
}