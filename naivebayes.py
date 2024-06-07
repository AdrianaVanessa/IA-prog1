#importamos todo lo que se va a utilizar a lo largo
#del programaS
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score

#importar el dataset
dataset = datasets.load_breast_cancer()

#Impresion de todo el dataset
print("Dataset")
print(dataset)

#Informacion del dataset
print("\n\nInformacion del Dataset")
print(dataset.keys())
#Imprimimos el arreglo de vectores con 30 parametros numericos
print("\n\nDATA")
print(dataset.get('data'))
#Imprimimos el valor numerico de la clasificacion del dataset(binario en este caso, 0 y 1)
print("\n\nTARGET")
print(dataset.get('target'))
#Imprimimos el nombre de las etiquetas de salida
print("\n\nTARGET_NAMES")
print(dataset.get('target_names'))
#Imprimimos la descripcion del dataset
print("\n\nDESCR")
print(dataset.get('DESCR'))
#Imprimimos los nombres de las caracteristicas
print("\n\nFEATURE_NAMES")
print(dataset.get('feature_names'))

#Asignamos los datos a 'X' y la clasificacion a 'y'
X = dataset.data
y = dataset.target
#Dividimos los datos 80% entrenamiento, 20% pruebas
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Imprimimos los datos de entrenamiento
print("\n\nX_train")
print(X_train)
#Imprimimos los datos de prubas
print("\n\nX_test")
print(X_test)
#Imprimimos los resultados con los que se entrena el modelo
print("\n\ny_train")
print(y_train)
#Imprimimos los resultados de prueba
print("\n\ny_test")
print(y_test)

escalar = StandardScaler()
#Escalamos y normalizamos los datos de entrenamiento
X_train = escalar.fit_transform(X_train)
#Escalamos los datos de pruebas
X_test = escalar.transform(X_test)

#Imprimimos los datos de entrenamiento escalados
print("\n\nX_train escalados")
print(X_train)

#Imprimimios los datos de prueba escalados
print("\n\nX_test escalados")
print(X_test)

#creamos una instancia del Naive-Bayes
algoritmo = GaussianNB()
#Lo entrenamos
algoritmo.fit(X_train, y_train)
#Realizamos una prediccion con el conjunto de pruebas
y_pred = algoritmo.predict(X_test)
#Calculamos la matriz de confusion
matriz = confusion_matrix(y_test, y_pred)

#Impresion de la matriz de confusion
print("\n\nMatriz de confusion")
print(matriz)

#Obtenemos la precision del modelo con el metodo precision_score
precision = precision_score(y_test, y_pred)
print("\n\nPrecision del modelo")
print(precision)