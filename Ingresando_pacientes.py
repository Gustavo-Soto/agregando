#Ingreso de pacientes a hospital
import csv
import os
import time

limpieza_pantalla = 'cls'

paciente = {}

#llamamos nuestro archivo csv y le damos permiso de escritura 'w'
with open('ingreso_pacientes.csv','w') as archivo_csv:
    lector_csv = csv.writer(archivo_csv)
    lector_csv.writerow(['nombre','rut','motivo ingreso','numero espera',])

#Este es el menu de ingreso de datos
while True:
    time.sleep(2)
    os.system(limpieza_pantalla)
    print('MENU HOSPITAL\n\nElija el numero de su eleccion\n\n1.-Agregar paciente \n2.-Consulta listado pacientes\n3.-Salir')

    ingreso = (int(input("")))

#Se ingresan pacientes y se agregan los datos al diccionario
    if ingreso ==1:
        time.sleep(1)
        os.system(limpieza_pantalla)
        nombre = input("Ingrese nombre paciente: ")
        paciente['Nombre'] = nombre

        rut = (input("Ingrese rut del paciente: "))
        paciente['Rut'] = rut

        motivo = input("Motivo de ingreso: ")
        paciente['Motivo de ingreso'] = motivo

        hora = (int(input("Ingrese numero de espera de paciente ")))
        paciente['Numero espera'] = hora

#Se agregan los datos correspondientes al archivo csv
        with open('ingreso_pacientes.csv','a',newline='') as archivo_csv:
            lector_csv = csv.writer(archivo_csv)
            lector_csv.writerows([[nombre,rut,motivo,hora]])
        print(nombre,rut,motivo,hora)
        print("")

        try:
            reanudar = (int(input("\nSeleccione un numero\n1.-Volver al menu principal\n2.-Salir\n")))
            if reanudar == 2:
                break
        except ValueError:
                print("\nElija un valor correcto")

    elif ingreso == 2:
        try:
#Se da permiso de lectura a archivo csv, en caso de estar en blanco no mostrara nada            
            with open("ingreso_pacientes.csv", 'r') as archivo_csv:
                lector_csv = csv.DictReader(archivo_csv)
                for fila in lector_csv:
                    print(fila)

            menu = (int(input("\nSeleccione un numero\n1.-Volver al menu principal\n2.-Salir\n")))
            if menu ==2:
                break    
        except FileNotFoundError:
            print("\nNo se ha encontrado archivo")      
    else:
        print("")
        break

print("Saliendo del programa")