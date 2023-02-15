import sys
import MySQLdb

def conectarBD(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.error as e:
        print("No ha sido posible conectarse a la base de datos",e)
        sys.exit(1)

def desconectarBD(db):
    db.close()

def menu():
    menu='''
    1.Listar contenido
    '''
    print(menu)
    while True:
        try:
            opcion = int(input("Introduce tu opcion"))
            return opcion
        except:
            print("Opcion incorrecta")
            
def listarAminales(db):
    sql="select * from animales"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro["codigo"],"--",registro["nombre"],"--",registro["especie"],"--",registro["raza"],"--",registro["color_pelo"],"--",registro["fecha_nacimiento"],"--",registro["DNI_propietario"])
    except:
        print("Error en la consulta")    