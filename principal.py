from BD.conexion import DAO
import funciones
def menu_principal():
    continuar=True
    while(continuar):
        opcion_correcta=False
        while(not opcion_correcta):
                   print("\n////////// MENU PRINCIPAL //////////\n")
                   print("1.- Listar pastillas")
                   print("2.- Registrar pastillas")
                   print("3.- Actualizar pastillas")
                   print("4.- Eliminar pastilla")
                   print("5.- Salir\n")

                   opcion = int(input("Selecione una opcion: "))
    
                   if opcion < 1 or opcion > 5:
                     print("Opcion incorrecta , intente nuevamente...")
                   elif opcion == 5:
                     continuar=False
                     print("Gracias por usar el sistema !!!")
                     break
                   else:
                        opcion_correcta = True
                        ejecutar_opcion(opcion)


def ejecutar_opcion(opcion):
    dao = DAO()
    if opcion == 1:
         try:
              pastillas = dao.listarpastillas()
              if len(pastillas) > 0:
                   funciones.listarpastillas(pastillas)
              else:
                   print("No se encontraron pastillas")
                   
         except:
              print("Ocurrio un error")

    elif opcion == 2:
         pastilla = funciones.validacion_de_datos_registro()
         try:
              dao.registrarpastilla(pastilla)
         except:
              print("Ocurrio un error en el registro...")

    elif opcion == 3:
         try:
              pastillas = dao.listarpastillas()
              if len(pastillas) > 0:
                  existemodelo, pastilla = funciones.datosctualizacion(pastillas)
                  if existemodelo:
                       dao.actualizarpastilla(pastilla)
                  else:
                       ("Pastilla no encontrada...\n")
              else:
                   print("No se encontro la pastilla...")      
         except:
            print("Ocurrio un error")

    elif opcion == 4:
         try:
              pastillas = dao.listarpastillas()
              if len(pastillas) > 0:
                   modeloeliminar = funciones.datoseliminacion(pastillas)
                   if not(modeloeliminar == ""):
                        dao.eliminarpastilla(modeloeliminar)
                   else:
                    print("Pastilla no encontrada...")
              else:
                   print("No se encontro la pastilla...")      
         except:
            print("Ocurrio un error")  
         

    else:
         print("Opcion invalida")
          

                   
         
  
         

menu_principal()

