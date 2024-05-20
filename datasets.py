from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = datasets.load_breast_cancer()

print(dataset)

print('Informacion del dataset')

print(dataset.keys())

print('Caracteristicas del dataset')

print(dataset.DESCR)

X = dataset.data

y = dataset.target

print('Valores de X')

print(X)

print('Valores de Y')

print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print('Valores de X_train')

print(X_train)

print('Valores de X_test')

print(X_test)

print('Valores de y_train')

print(y_train)

print('Valores de y_test')

print(y_test)

escalar = StandardScaler()

X_train = escalar.fit_transform(X_train)
X_test = escalar.transform(X_test)

print('Valores de X_train escalados')

print(X_train)

print('Valores de X_test escalados')

print(X_test)

