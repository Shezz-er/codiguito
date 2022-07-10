from DAOpersonas import *

def exists(registro:Login):
    #se envia a datos para saber si los atributos existen en la DB
    if DAOpersonas.verifyLogin(registro.id,registro.password)==1:
    #se retorna respuesta a presentacion    
        return True
    else:
        return False

