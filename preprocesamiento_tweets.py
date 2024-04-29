#preprocesamiento de tweets
#IA
#versionfinal
import stanza
import nltk
from nltk.corpus import stopwords
import re

"punto 1 Eliminación de menciones (@usuario):"
def eliminar_menciones(tweet):
    # Dividir el tweet en palabras
    palabras = tweet.split()
    # Filtrar las palabras que no son menciones
    palabras_filtradas = [palabra for palabra in palabras if not (palabra.startswith('@') or palabra.startswith('"@') or palabra.startswith('.@') or palabra.startswith('metemierda...@juanmacastano:') )]
    # Unir las palabras nuevamente en un string
    tweet_sin_menciones = ' '.join(palabras_filtradas)
    return tweet_sin_menciones

"punto 2 eliminación de enlaces"
def limpiar_texto(texto):
    # Eliminar enlaces
    texto_limpio = re.sub(r'http\S+', '', texto)
    return texto_limpio

"punto 3. eliminación de signos y sustitución de emojis con diccionario"
diccionario_emojis = {
    ":o": "sorpresa",
    ":)": "feliz",
    ":(": "triste"
}
def limpiar_texto2(texto):
    # Eliminar enlaces
    texto_limpio = re.sub(r'[.,:;!?()\'\"`]', '', texto)
    for emoji, descripcion in diccionario_emojis.items():
        texto_limpio = texto_limpio.replace(emoji, descripcion)
    return texto_limpio

"punto 5. eliminacion de stopwords"
# Obtener la lista de stopwords en español
stopwords_es = set(stopwords.words('spanish'))
# Definir una función para eliminar las stopwords de un texto
def eliminar_stopwords(texto):
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stopwords_es]
    texto_sin_stopwords = ' '.join(palabras_filtradas)
    return texto_sin_stopwords
# Función para leer un archivo, aplicar el preprocesamiento y escribir el resultado
def preprocesar_archivo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        texto = file.read()
    
    texto_sin_stopwords = eliminar_stopwords(texto)
    
    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.write(texto_sin_stopwords)

"punto 8. sustitucion de entidades"
diccionario_entidades = {
    "españa": "españa_entidad_lugar",
    "mamasa": "mamasa_entidad_persona",
    "luis": "luis_entidad_persona",
    "enrique": "enrique_entidad_persona",
    "león": "león_entidad_lugar",
    "franco": "franco_entidad_persona",
    "matias": "matias_entidad_persona",
    "twitter": "twitter_entidad_marca",
    "toledo": "toledo_entidad_lugar",
    "messi": "messi_entidad_persona",
    "fb": "fb_entidad_marca",
    "córdoba": "córdoba_entidad_lugar",
    "alemania": "alemania_entidad_lugar",
    "pedro": "pedro_entidad_persona",
    "miguel": "miguel_entidad_persona",
    "edith hermida": "edith_hermida_entidad_persona",
    "ignacio gonzález": "ignacio_gonzález_entidad_persona",
    "valenciano": "valenciano_entidad_persona",
    "madrid": "madrid_entidad_lugar",
    "cristiano": "cristiano_entidad_persona",
    "jose cruz salas": "jose_cruz_salas_entidad_persona",
    "isabel carrasco": "isabel_carrasco_entidad_persona",
    "mendoza": "mendoza_entidad_lugar",
    "carmen": "carmen_entidad_persona",
    "rosario": "rosario_entidad_lugar",
    "air max": "air_max_entidad_marca",
    "mcdonalds": "mcdonalds_entidad_lugar",
    "silvio guerra": "silvio_guerra_entidad_persona",
    "iker casillas": "iker_casillas_entidad_persona",
    "cristina": "cristinaentidad_persona"
}
def sustituir_entidades(texto, diccionario_entidades):
    palabras = texto.split()
    for i in range(len(palabras)):
        palabra = palabras[i].lower() 
        if palabra in diccionario_entidades:
            palabras[i] = diccionario_entidades[palabra]
    return ' '.join(palabras)

"punto 10. normalizar texto: pasar todo a minusculas"
def convertir_a_minusculas(texto):
    return texto.lower()

"eliminar ID fecha y hora de los tweets"
def eliminar_id_fecha_hora(tweet):
    tweet_limpio = re.sub(r'\b\d{18}\b|\b\d{4}-\d{2}-\d{2} \d{1,2}:\d{1,2}:\d{1,2}\b|\b\d{4}-\d{2}-\d{2}\b|\d+', '', tweet)
    return tweet_limpio

"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Función main+++++++++++++++++++++++++++++++++++++++++++++++++++++"
"Se empieza con el punto 1 eliminación de @------------------------------"
def main():
    #lee el archivo de texto
    with open('tweets_asco.txt', 'r', encoding='utf-8') as archivo:
        tweets = archivo.readlines()
    # Eliminar menciones de cada tweet
    tweets_sin_menciones = [eliminar_menciones(tweet) for tweet in tweets]
    # Escribir los tweets sin menciones en un nuevo archivo
    with open('tweets_1.txt', 'w') as archivo_salida:
        for tweet in tweets_sin_menciones:
            archivo_salida.write(tweet + '\n')
    print("\npunto 1. se eliminaron las menciones de los tweets (@usuaio) y se genero un nuevo archivo 'tweets_1.txt' sin las mismas")

    "Sigue el punto 2 eliminación de enlaces-------------------------------"
    # Leer el archivo de texto nuevo generado por el punto 1
    with open('tweets_1.txt', 'r', encoding='latin-1') as file:
        texto = file.read()
    # Limpiar el texto
    texto_limpio = limpiar_texto(texto)
    # Imprimir los resultados
    with open('tweets_2.txt', 'w', encoding='utf-8') as result_file:
        # archivo limpio
        result_file.write(texto_limpio)
    print("\npunto 2. se eliminaron las url y se genero un nuevo archivo 'tweets_2.txt' sin las mismas")
    
    "Sigue el punto 3 eliminación de signos de puntuación-------------------------------"
    # Leer el archivo de texto nuevo generado por el punto 2
    with open('tweets_2.txt', 'r', encoding='utf-8') as file:
        texto = file.read()
    for emoji, descripcion in diccionario_emojis.items():
        texto = texto.replace(emoji, descripcion)
    # Limpiar el texto
    texto = limpiar_texto2(texto)
    # Imprimir los resultados
    with open('tweets_3.txt', 'w', encoding='utf-8') as result_file:
        # archivo limpio
        result_file.write(texto)
    print("\npunto 3. se eliminaron los signos de puntuación y se sustituyeron los emojis, se genero un nuevo archivo 'tweets_3.txt' sin las mismas")

    "sigue el punto 5 eliminacion de stopwords"
    archivo_entrada = 'tweets_3.txt'
    archivo_salida = 'tweets_5.txt'  
    preprocesar_archivo(archivo_entrada, archivo_salida)
    print("\npunto 5. se eliminaron los stopswords y se genero un nuevo archivo 'tweets_5.txt' sin las mismas")

    "sigue el punto 8 sustitucion de entidades"
    archivo_entrada = 'tweets_5.txt'
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        texto = file.read()
    # Reemplazar entidades
    texto_con_entidades_sustituidas = sustituir_entidades(texto, diccionario_entidades)
    # Escribir el resultado en un nuevo archivo
    archivo_salida = 'tweets_8.txt'
    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.write(texto_con_entidades_sustituidas)
    print("\npunto 8. se sustituyeron las entidades y se genero un nuevo archivo 'tweets_8.txt'")

    "sigue el punto 10 Normalización de texto: hacer todas las letras minusculas"
    archivo_entrada = 'tweets_8.txt'
    archivo_salida = 'tweets_10.txt'
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        texto_original = file.read()
    # llamar a la funcion
    texto_minusculas = convertir_a_minusculas(texto_original)
    # nuevo txt
    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.write(texto_minusculas)
    print("\npunto 10. se normalizó el texto (minusculas) y se genero un nuevo archivo 'tweets_10.txt'.")

    "sigue el paso final. eliminar ID, fecha y hora"
    archivo_entrada = 'tweets_10.txt'
    archivo_salida = 'tweets_asco_limpio.txt'
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        texto_original = file.read()
    texto_preprocesado = eliminar_id_fecha_hora(texto_original)
    with open(archivo_salida, 'w', encoding='utf-8') as file:
        file.write(texto_preprocesado)
    print("\nse eliminaron los ID, la fecha y la hora de los tweets. El archivo txt final 'tweets_asco_limpio.txt' esta listo y limpio\n")
if __name__ == "__main__":
    main()
    