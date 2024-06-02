import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

num_records = 200
num_features = 6
num_classes = 4

#preparacion de datos sinteticos
noCliente = np.arange(num_records)
edad = np.random.randint(18,70,num_records)
cp = np.random.randint(1000,9999,num_records)
saldo = np.random.randint(0, 100000, num_records)
adeudo = 100 * np.random.rand(num_records) - 50
situacion = np.random.randint(0, 2, num_records)

labels = np.random.randint(0, num_classes, num_records)

data = {
    'noCliente': noCliente,
    'edad': edad,
    'cp': cp,
    'saldo': saldo,
    'adeudo': adeudo,
    'situacion': situacion,
    'Label': labels
}

df = pd.DataFrame(data)

#guardado de datos en archivo
df.to_csv('datos sintacticos.csv', index=False)

#lecura de los datos del archivo creado
clientes = pd.read_csv('datos sintacticos.csv')

# 0 - sin adeudos y saldo corriente
# 1 - sin adeudos pero con saldo pendiente
# 2 - con adeudos y saldo corriente
# 3 - con adeudos pero con saldo pendiente

a0=clientes[clientes["Label"]==0]
a1=clientes[clientes["Label"]==1]
a2=clientes[clientes["Label"]==2]
a3=clientes[clientes["Label"]==3]

plt.scatter(a0["edad"], a0["saldo"],
            marker="*", s=150, color="blue",
            label="sin adeudos y saldo corriente")   

plt.scatter(a1["edad"], a1["saldo"],
            marker="*", s=150, color="red",
            label="sin adeudos  pero con saldo pendiente")

plt.scatter(a2["edad"], a2["saldo"],
            marker="*", s=150, color="yellow",
            label="con adeudos y saldo corriente")

plt.scatter(a3["edad"], a3["saldo"],
            marker="*", s=150, color="green",
            label="con adeudos  pero con saldo pendiente")

plt.ylabel("saldos")
plt.xlabel("Edad")
plt.legend(bbox_to_anchor=(1,.3))
plt.show()

#escalado de datos
datos=clientes[["edad","saldo"]]
clase=clientes["Label"]

escalar = preprocessing.MinMaxScaler()
datos = escalar.fit_transform(datos)



clasificador = KNeighborsClassifier(n_neighbors=3)
clasificador.fit(datos,clase)

edad = 20
monto = 25000

solicitante = escalar.transform([[edad,monto]])
print("clase", clasificador.predict(solicitante))
print("probabilidades por clase", clasificador.predict_proba(solicitante))

plt.scatter(a0["edad"], a0["saldo"],
            marker="*", s=150, color="blue",
            label="sin adeudos y saldo corriente")   

plt.scatter(a1["edad"], a1["saldo"],
            marker="*", s=150, color="red",
            label="sin adeudos  pero con saldo pendiente")

plt.scatter(a2["edad"], a2["saldo"],
            marker="*", s=150, color="yellow",
            label="con adeudos y saldo corriente")

plt.scatter(a3["edad"], a3["saldo"],
            marker="*", s=150, color="green",
            label="con adeudos  pero con saldo pendiente")
plt.scatter(edad,monto, marker="P", s=250, color="lime", label="solicitante")
plt.ylabel("saldos")
plt.xlabel("Edad")
plt.legend(bbox_to_anchor=(1,.3))
plt.show()

saldos = np.array([np.arange(0, 100200, 200)]*44).reshape(1, -1)
edades = np.array([np.arange(19, 72)]*416).reshape(1, -1)

edades = np.delete(edades, np.s_[-4:None])

saldos_df = pd.DataFrame(saldos.flatten(), columns=["saldo"])
edades_df = pd.DataFrame(edades.flatten(), columns=["edad"])

todos = pd.concat([edades_df, saldos_df], axis=1)

#Escalar los datos
solicitantes = escalar.transform(todos)

#Predecir todas las clases
clases_resultantes = clasificador.predict(solicitantes)

#Código para graficar
a00 = todos[clases_resultantes==0]
a01 = todos[clases_resultantes==1]
a02 = todos[clases_resultantes==2]
a03 = todos[clases_resultantes==3]
plt.scatter(a00["edad"], a00["saldo"],
            marker="*", s=150, color="blue",
            label="sin adeudos y saldo corriente")   

plt.scatter(a01["edad"], a01["saldo"],
            marker="*", s=150, color="red",
            label="sin adeudos  pero con saldo pendiente")

plt.scatter(a02["edad"], a02["saldo"],
            marker="*", s=150, color="yellow",
            label="con adeudos y saldo corriente")

plt.scatter(a03["edad"], a03["saldo"],
            marker="*", s=150, color="green",
            label="con adeudos  pero con saldo pendiente")
plt.ylabel("Monto del crédito")
plt.xlabel("Edad")
plt.legend(bbox_to_anchor=(1, 0.2))
plt.show()