import mysql.connector
from mysql.connector import Error

class DAO():
    
    def __init__(self):
         try:
              self.conexion=mysql.connector.connect(
                   host='localhost',
                   port=3306,
                   user='root',
                   password='18718207-7',
                   db='pastillas'     
              )

         except Error as ex:
              print("error al intentar la conexion:{0}".format(ex))

    def listarpastillas(self):
         if self.conexion.is_connected():
              try:
                   cursor=self.conexion.cursor()
                   cursor.execute("SELECT * FROM toyota ORDER BY modelo ASC")
                   resultados=cursor.fetchall()
                   return resultados
                                 
              except Error as ex:
                   print("error al intentar la conexion:{0}".format(ex))
    
    def registrarpastilla(self, pastilla):
         if self.conexion.is_connected():
              try:
                   cursor = self.conexion.cursor()
                   sql = "INSERT INTO toyota (modelo, codigo, codigo_disco, precio) VALUES ('{0}', '{1}', '{2}', '{3}');"
                   cursor.execute(sql.format(pastilla[0], pastilla[1], pastilla[2], pastilla[3]))
                   self.conexion.commit()
                   print("Datos registrados exitosamente !!")

              except Error as ex:
                   print("error al intentar la conexion:{0}".format(ex))

    def actualizarpastilla(self, pastilla):
         if self.conexion.is_connected():
              try:
                   cursor = self.conexion.cursor()
                   sql = "UPDATE toyota SET codigo = '{0}', codigo_disco = '{1}', precio = '{2}' WHERE modelo = '{3}';"
                   cursor.execute(sql.format(pastilla[1], pastilla[2], pastilla[3], pastilla[0]))
                   self.conexion.commit()
                   print("Datos actualizados exitosamente !!")

              except Error as ex:
                   print("error al intentar la conexion:{0}".format(ex))
         
         

    def eliminarpastilla(self, modeloeliminar):
         if self.conexion.is_connected():
              try:
                   cursor = self.conexion.cursor()
                   sql = "DELETE FROM toyota WHERE modelo = '{0}';"
                   cursor.execute(sql.format(modeloeliminar))
                   self.conexion.commit()
                   print("Datos eliminados exitosamente !!")

              except Error as ex:
                   print("error al intentar la conexion:{0}".format(ex))
              
         

"""def actualizarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE curso SET nombre = '{0}', creditos = {1} WHERE codigo = '{2}'"
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print("¡Curso actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))"""
                   

