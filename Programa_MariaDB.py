from Funciones_MariaDB import *

db = conectarBD("localhost","josema","josema","proyecto")
opcion = menu()
while opcion!=0:
    if opcion ==1:
        listarAminales(db)
    opcion=menu()