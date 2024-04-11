import stanza

def tokenizar_lematizar(texto):
    # Configurar el pipeline de Stanza para español
    nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')
    
    # Procesar el texto
    doc = nlp(texto)
    
    # Extraer tokens y lemas
    tokens = []
    lemas = []
    for sentence in doc.sentences:
        for word in sentence.words:
            tokens.append(word.text)
            lemas.append(word.lemma)
    
    return tokens, lemas, doc.sentences

def main():
    # Leer el archivo de texto
    with open('pinocho.txt', 'r', encoding='utf-8') as file:
        texto = file.read()
    
    # Tokenizar y lematizar el texto
    tokens, lemas, sentences = tokenizar_lematizar(texto)
    
    # Imprimir los resultados
    sentence_id = 0
    word_id = 0
    with open('pinocho_result.txt', 'w', encoding='utf-8') as result_file:
        # imprimir el texto de pinocho.txt
        result_file.write(texto)
        result_file.write("\n\n")
        # imprimir los tokens y lemas

        for sentence in sentences:
            result_file.write(f"\n====== frase {sentence_id + 1} ======\n")
            for word in sentence.words:
                result_file.write(f"id: {word_id:<5} palabra: {tokens[word_id]:<20} lema: {lemas[word_id]}\n")
                word_id += 1
            sentence_id += 1

if __name__ == "__main__":
    main()

