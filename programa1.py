import sys
#Programa 1. Inteligencia Artificial
#Manejo de cadenas, listas, tuplas y diccionarios
#Sánchez Barragán Rodrigo
#Trejo Reyes Adriana Vanessa

""" Se realizará una aplicación en la que se usen las cadenas, tuplas, listas y diccionarios. Dicha aplicación
consiste generar las citas para una veterinaria """

#bd de veterinarios usando diccionarios
veterinario1 = {
    "id": 1, 
    "nombre": "Dr. Carlos Moreno", 
    "área": "Estética",
    "cédula": "294023942"}

veterinario2 = {
    "id": 2, 
    "nombre": "Dr. Rodrigo Sánchez", 
    "área": "Quirófano",
    "cédula": "294023941"}

veterinario3 = {
    "id": 3, 
    "nombre": "Dra. Vanessa Trejo", 
    "área": "Consultorio general",
    "cédula": "294023947"}

veterinario4 = {
    "id": 4, 
    "nombre": "Dr. Alberto Navarro", 
    "área": "Entrenamiento",
    "cédula": "294023957"}

#lista de veterinarios-> se pueden agregar o modificar los veterinarioes del consultorio
lista_veterinarios = [veterinario1, veterinario2, veterinario3, veterinario4]
citas_medicas = [] #lista a la que agregaremos mediante append las citas que se van generando

#++++++++++++++++++++++++++++++++++++++++++++ 1. Imprimir ista de veterinarios +++++++++++++++++++++++++++++++++
def ver_veterinarios():
    print("\n\nLista de médicos disponibles: \n")
    print(veterinario1['id'],"-", veterinario1['nombre'],", Área:", veterinario1['área'], ", Cédula profesional:",veterinario1['cédula'])
    print(veterinario2['id'],"-", veterinario2['nombre'],", Área:", veterinario2['área'], ", Cédula profesional:",veterinario2['cédula'])
    print(veterinario3['id'],"-", veterinario3['nombre'],", Área:", veterinario3['área'], ", Cédula profesional:",veterinario3['cédula'])
    print(veterinario4['id'],"-", veterinario4['nombre'],", Área:", veterinario4['área'], ", Cédula profesional:",veterinario4['cédula'])

#++++++++++++++++++++++++++++++++++++++++++++ 2. Generar cita ++++++++++++++++++++++++++++++++++++++++++++++++++
def generar_cita():
    #aqui hacemos uso de las cadenas principalmente en el nombre y la área que menciona los aspectos a atender por el veterinario
    nombre_mascota = input("Ingrese el nombre del paciente: ")
    id_veterinario = int(input("Ingrese el ID del veterinario seleccionado: "))
    area = input("Ingrese los aspectos que atenderá su veterinario separado por comas: ")

    veterinario = next((m for m in lista_veterinarios if m["id"] == id_veterinario), None)

    if veterinario is not None:
        #tuplas para generar las citas-> una vez creada la cita no se puede modificar o eliminar algún elemento
        cita = (nombre_mascota, area, veterinario)

        citas_medicas.append(cita)
        print(f"\n\nCita generada para {nombre_mascota} con el {veterinario['nombre']} ({veterinario['área']}).")
    else:
        print("Veterinario no encontrado")


#++++++++++++++++++++++++++++++++++++++++++++ 3. Ver cita +++++++++++++++++++++++++++++++++++++++++++++++++++++++
def ver_citas():
    print("\n\nInformación de citas médicas: \n")

    if not citas_medicas:
        print("\nNo hay citas agendadas en este momento\n")
    else:
        #aqui hacemos uso y manejamos las cadenas creadas previamente en las variables nombre_paciente, area y veterinario
        incremento=1
        for cita in citas_medicas:
            nombre_paciente, area, veterinario = cita
            print(f"\n {incremento} - Nombre del paciente: {nombre_paciente} - Motivo de visita: {area} - Veterinario: {veterinario['nombre']} ({veterinario['área']})")
            incremento += 1

#++++++++++++++++++++++++++++++++++++++ Menú principal de la aplicación +++++++++++++++++++++++++++++++++++++++++

while True:
    print("\n\nBienvenido a PETKO. Seleccione la opción que desea.")
    print("1. Ver lista de veterinarios disponibles")
    print("2. Generar cita")
    print("3. Ver las citas agendadas")
    print("4. Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        ver_veterinarios()
    elif opcion == "2":
        generar_cita()
    elif opcion == "3":
        ver_citas()
    elif opcion == "4":
        print("\n¡Vuelva pronto!\n")
        sys.exit()
    else:
        print("Opción inválida. Intente nuevamente")