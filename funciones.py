
def listarpastillas(pastillas):
    if not pastillas:
        print("No hay pastillas")
        return
    else:
        print("Existecias: \n")
        contador = 1
        for p in pastillas:
            datos = "{0}. codigo: {1} / modelo: {2} / año: {3} / añofinal: {4} / existecias: {5}"
            print(datos.format(contador,p[0],p[1],p[2],p[3],p[4]))
            contador = contador + 1
          


def datosctualizacion(pastillas):
    listarpastillas(pastillas)
    codigocorrecto = False
    existecodigo = False
    pastilla = None
    try:
        while not codigocorrecto:
            codigoeditar = input("Ingrese el codigo de la pastilla que desea editar: ")
            if codigoeditar.isnumeric():
                codigocorrecto = True
            else:
                print("Error , el codigo debe ser unicamente un numero...")
            
        for p in pastillas:
            if p[0] == codigoeditar:
                pastilla = validacion_de_datos_actualizacion(codigoeditar)
                existecodigo = True
                break
                
            if not existecodigo:
                    print("Codigo no encontrado, ingrese otro...")
    except:
         print("Ocurrio un error.........")
                
    return existecodigo, pastilla


def datoseliminacion(pastillas):
    listarpastillas(pastillas)
    existemodelo = False
    modeloeliminar = input("Ingrese el modelo que desea eliminar: ")
    for p in pastillas:
        if p[0] == modeloeliminar:
            existemodelo = True
            break

    if not existemodelo:
        modeloeliminar = ""
    return modeloeliminar

def validacion_de_datos_registro():
    
    try:
        codigocorrecto = False
        añocorrecto = False
        añofinalcorrecto = False
        existenciascorrecto = False
        while not codigocorrecto:
            codigo = input("Ingrese el codigo de la pastilla: ")
            if len(codigo) == 4 and codigo.isnumeric():
                codigocorrecto = True
            else:
                print("Error , el codigo debe ser unicamente un numero de 4 digitos...")
        
        modelo = input("Ingrese el modelo correspondinte: ")

        while not añocorrecto:
            año = input("Ingrese el año de inicio: ")
            if len(año) == 4 and año.isnumeric():
                añocorrecto = True
            else:
                print("Error , el año debe ser unicamente un numero de 4 digitos...")
                
        while not añofinalcorrecto:
            añofinal = input("Ingrese el año final, si no tiene año final ingrese un 0: ")
            if len(añofinal) == 4 or añofinal == "0":
                añofinalcorrecto = True
            else:
                print("Error , el año final debe ser unicamente un numero de 4 digitos o un 0...")

        while not existenciascorrecto:
            existencias = input("Ingrese la cantidad de pastillas disponibles: ")
            if existencias.isnumeric():
                existenciascorrecto = True
            else:
                print("Error , la existecia debe ser unicamente un numero entero...")

        if codigocorrecto == True and añocorrecto == True and añofinalcorrecto == True and existenciascorrecto == True:
            pastilla = (codigo, modelo, año, añofinal, existencias)
            return pastilla
    except:
        print("Ocurrio un error...")

def validacion_de_datos_actualizacion(codigoeditar):
    try:
        añocorrecto = False
        añofinalcorrecto = False
        existenciascorrecto = False
        
        modelo = input("Ingrese el modelo correspondinte: ")

        while not añocorrecto:
            año = input("Ingrese el año de inicio: ")
            if len(año) == 4 and año.isnumeric():
                añocorrecto = True
            else:
                print("Error , el año debe ser unicamente un numero de 4 digitos...")
                
        while not añofinalcorrecto:
            añofinal = input("Ingrese el año final, si no tiene año final ingrese un 0: ")
            if len(añofinal) == 4 or añofinal == "0":
                añofinalcorrecto = True
            else:
                print("Error , el año final debe ser unicamente un numero de 4 digitos o un 0...")

        while not existenciascorrecto:
            existencias = input("Ingrese la cantidad de pastillas disponibles: ")
            if existencias.isnumeric():
                existenciascorrecto = True
            else:
                print("Error , la existecia debe ser unicamente un numero entero...")

        if añocorrecto == True and añofinalcorrecto == True and existenciascorrecto == True:
            pastilla = (codigoeditar, modelo, año, añofinal, existencias)
            return pastilla
    except:
        print("Ocurrio un error...")
    


        


"""try:
        ingresovalido = False
        while not ingresovalido:
            codigocorrecto = False
            while not codigocorrecto:
                codigo = input("Ingrese el codigo de la pastilla que desea registrar: ")
                if len(codigo) == 4 and codigo.isnumeric():
                    codigocorrecto = True
                    modelo = input("Ingrese el modelo correspondiente: ")
                    año = input("Ingrese el año en que se fabrico: ")
                    if len(año)== 4 and año.isdigit():
                        añofinal = input("ingrese el año en que se dejo de fabricar , si aun se esta fabricando ingrese un 0 : ")
                        if len(añofinal) == 4 or añofinal == 0:
                            existecias = input("Ingrese la cantidad de pastillas disponibles: ")
                            if existecias.isnumeric():
                                ingresovalido = True
                                pastilla = (codigo, modelo, año, añofinal, existecias)
                            else:
                                print("Error , debe ingresar solo numeros....")
                        else:
                            print("Error , debe ingresar unicamente un numero de 4 digitos o un signo + ....")
                    else:
                        print("Error , debe ingresar unicamente un numero de 4 digitos....")
                else:
                    print("Error , debe ingresar unicamente un numero de 4 digitos.... ")
        return pastilla
    except:
        print("Ocurrio un error...")"""