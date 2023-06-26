import json 

def parsear_json(ruta:str)->list:
    """Lee un archivo json y devuelve una lista con los resultados."""
    with open(ruta,"r")as archivo:
        datos= json.load(archivo)
        return datos["results"]

def copiar_lista()->list:
    """Copia una lista obtenida desde la funcion parsear_json()
    modifica las keys y castea los values de tipo numerico y la retona"""
    ruta = "C:\\programacion I\\recuperatorio\\data.json"
    lista=parsear_json(ruta)
    lista_copiada = []
    for i in lista:
        dic={}
        dic["nombre"]=i["name"]
        dic["altura"]=int(i["height"])
        dic["peso"]=int(i["mass"]) 
        dic["genero"]=i["gender"]  
        lista_copiada.append(dic)
    return lista_copiada

def generar_separador(patron:str,largo:int,imprimir:bool=True)->str:
    """genera una patron segun el caracter y el largo que llega por parametro 
    el tercer parametro define si se imprime o se retorna"""
    nuevo_patron= patron.zfill(largo).replace("0",patron)
    if imprimir==True:
        print(nuevo_patron)
    else:
        return nuevo_patron

def calcular_likes(dic):
    """Calcula la cantidad de likes en base al valor de la masa
    retorna la cantidad de likes"""
    likes=int(dic["mass"])*100
    return likes