
def listarpastillas(pastillas):
    if not pastillas:
        print("No hay pastillas")
        return
    else:
        print("Existecias: \n")
        contador = 1
        for p in pastillas:
            datos = "{0}. modelo: {1} / codigo: {2} / codigo_disco: {3} / precio: {4}"
            print(datos.format(contador,p[0],p[1],p[2],p[3]))
            contador = contador + 1
          


def datosctualizacion(pastillas):
    listarpastillas(pastillas)
    existemodelo = False
    while not existemodelo:
        try:
            modeloeditar = input("Ingrese el modelo del vehiculo que desea editar: ")
            for p in pastillas:
              if p[0] == modeloeditar:
                pastilla = validacion_de_datos_actualizacion(modeloeditar)
                existemodelo = True
            if not existemodelo:
                print("Modelo no encontrado, ingrese otro...")
        except:
            print("Ocurrio un error")
                
    return existemodelo, pastilla


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
    modelo = input("Ingrese el modelo: ")
    ingresos_valido = False
    while not ingresos_valido:
        codigo = (input("Ingrese el codigo de la pastilla: "))
        if len(codigo) == 4 and codigo.isdigit():
            ingresos_valido = True
        else:
            print("Codigo no valido , debe ser unicamente un numero de 4 digitos...")
    ingresos_valido = False
    while not ingresos_valido:
        codigo_disco = (input("Ingrese el codigo del disco: "))
        if len(codigo_disco) == 4 and codigo_disco.isdigit():
            ingresos_valido = True
        else:
            print("Codigo no valido , debe ser unicamente un numero de 4 digitos...")
    ingresos_valido = False
    while not ingresos_valido:
        valor = (input("Ingrese el precio de la pastilla: "))
        if valor.isdigit():
            ingresos_valido = True

    pastilla = (modelo, codigo, codigo_disco, valor)
    return pastilla

def validacion_de_datos_actualizacion(modeloeditar):
    ingresos_valido = False
    while not ingresos_valido:
        codigo = (input("Ingrese el codigo de la pastilla: "))
        if len(codigo) == 4 and codigo.isdigit():
            ingresos_valido = True
        else:
            print("Codigo no valido , debe ser unicamente un numero de 4 digitos...")
    ingresos_valido = False
    while not ingresos_valido:
        codigo_disco = (input("Ingrese el codigo del disco: "))
        if len(codigo_disco) == 4 and codigo_disco.isdigit():
            ingresos_valido = True
        else:
            print("Codigo no valido , debe ser unicamente un numero de 4 digitos...")
    ingresos_valido = False
    while not ingresos_valido:
        valor = (input("Ingrese el precio de la pastilla: "))
        if valor.isdigit():
            ingresos_valido = True

    pastilla = (modeloeditar, codigo, codigo_disco, valor)
    return pastilla

    


        
