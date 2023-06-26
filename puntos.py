import re 
from funciones import calcular_likes
from funciones import parsear_json

#1
def ordenar(forma:str,key:str,lista:list)->list:
    """Ordena la lista en base a una key y la forma (ascendente o descendente)"""
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if forma=="desc" and lista[i][key]>lista[j][key] or forma=="asc" and lista[i][key]<lista[j][key] :
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista 

#2
def mas_alto(genero:str,lista:list)->dict:
    """Encuentra el personaje más alto de un género  yretorna el diccionario correspondiente"""
    altura_max=0
    for personajes in lista: 
        if personajes["genero"]==genero: 
            if altura_max<personajes["altura"]: 
                altura_max=personajes["altura"] 
                nombre = personajes["nombre"]
               
    return nombre,altura_max

#4
def buscador_personajes(nombre:str,lista,key:str)->dict: 
    """Busca un personaje por nombre en una lista de diccionarios
    y lo retorna"""
    for personaje in lista:
        nom=personaje[key].lower() 
        validacion=re.search(nombre,nom)
        if validacion !=None:
            return personaje

#5
def exportar_csv(ruta: str, lista: list, agregar_key: bool):
    """Exporta los datos de una lista a un archivo CSV en la ruta que ingresan por parametros"""
    with open(ruta, 'w') as archivo:
        for fila in lista:
            if agregar_key:
                mensaje = "\nnombre: {0}\naltura: {1}\npeso: {2}\ngenero: {3}\nlikes: {4}\n---------------".format(
                    fila["nombre"], fila["altura"], fila["peso"], fila["genero"], fila["likes"])
            else:
                mensaje = "\nnombre: {0}\naltura: {1}\npeso: {2}\ngenero: {3}\n---------------".format(
                    fila["nombre"], fila["altura"], fila["peso"], fila["genero"])
            archivo.write(mensaje)
        print("se guardaron los cambios") 

#### recuperatorio ####
#6
def Actualizar_Personajes()->list:
    """modifica la lista original agregando una nueva key (likes) y casteando las key de tipo numericas"""
    lista=parsear_json("data.json")
    lista_actializada = []
    for i in lista:
        dic={}
        dic["nombre"]=i["name"]
        dic["altura"]=int(i["height"])
        dic["peso"]=int(i["mass"]) 
        dic["genero"]=i["gender"] 
        dic["likes"]=calcular_likes(i)
        lista_actializada.append(dic)
    return lista_actializada

#8 
def buscar_likes(lista:list,cantidad:int):
    if cantidad<13600 and cantidad>3200:
        for personaje in lista:
            if cantidad>personaje["likes"]:
                print("nombre: {0}\nlikes: {1}\n{2}".format(personaje["nombre"],personaje["likes"],"-----------"))
    else:
        print("no existe un pesonaje con esa cantida de likes el rango es de 3200 a 13600")



