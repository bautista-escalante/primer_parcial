import re
from funciones import copiar_lista
from funciones import generar_separador
from puntos import ordenar
from puntos import mas_alto 
from puntos import buscador_personajes
from puntos import exportar_csv
from puntos import Actualizar_Personajes
from puntos import buscar_likes

patron1=generar_separador("|",2,False)
patron2=generar_separador("*",20,False)
patron3=generar_separador(" ",20,False)
patron4=generar_separador("-",20,False)
lista_copiada=copiar_lista()

def menu_principal()->None: 
    """imprime el menu de opciones y ejecuta la que el usuario eligio
        no ingresan parametros ni tampoco retorna algo 
    """
    while True:
        print("\n 1- Listar los personajes ordenados por altura \n 2- Mostrar el personaje "
            "más alto de cada genero \n 3- Ordenar y listar los personajes por peso \n"
            " 4- buscar personaje por nombre \n 5- exportar a csv \n 6- Actualizar Personajes \n"
            " 7- Exportar a CSV Personaje Actualizado \n 8- Listar Personajes Actualizados por Likes \n 9- salir")   
        opcion= input(" elige una opcion: ")
        print(patron3)
        while re.search(r"[0-9]",opcion)==None:
            print(" error. ingrese un numero del 1 al 9")
            opcion=input(" elige una opcion: ")
        opcion=int(opcion)
        match opcion:
                case 1:
                    respuesta= input("ingrese la forma que desea ordenar, ascendente (‘asc’) o descendente (‘desc’) ")
                    respuesta=respuesta.lower() 
                    verificacion=re.search("^(asc|desc)$", respuesta)
                    if verificacion != None : 
                        lista =ordenar(respuesta,"altura",lista_copiada)
                        for personaje in lista:
                            print("nombre: ",personaje["nombre"],"\naltura: ",personaje["altura"])
                            print(patron4)
                    else : 
                        print("\nerror. ingrese unicamente ASC o DESC \n")
                case 2:
                    hombre=mas_alto("male",lista_copiada)
                    print(patron2)
                    print("{0} {2} {1} cm".format(hombre[0],hombre[1],patron1))
                    print(patron2)
                    mujer=mas_alto("female",lista_copiada)
                    print("{0} {2} {1} cm".format(mujer[0],mujer[1],patron1))
                    print(patron2)
                    na=mas_alto("n/a",lista_copiada)
                    print("{0} {2} {1} cm".format(na[0],na[1],patron1))
                    print(patron2) 
                case 3: 
                    resultado= input("ingrese la forma que desea ordenar, ascendente (‘asc’) o descendente (‘desc’) ")
                    resultado=resultado.lower() 
                    verificacion=re.search("^(asc|desc)$", resultado)
                    lista=copiar_lista()
                    if verificacion != None : 
                        lista =ordenar(resultado,"peso",lista)
                        for personaje in lista:
                            print("nombre: ",personaje["nombre"],"\npeso: ",personaje["peso"])
                            print(patron4)
                    else : 
                        print("\nerror. ingrese unicamente ASC o DESC \n")
                case 4: 
                    nombre=input("ingrese el nombre ")
                    nombre.lower() 
                    personaje=buscador_personajes(nombre,lista_copiada,"nombre")
                    if  personaje != None:
                        print(patron2) 
                        print("nombre completo: {0}\naltura: {1}\npeso: {2}\ngenero: {3}".format(personaje["nombre"],personaje["altura"],
                                                                                        personaje["peso"],personaje["genero"]))
                        print(patron2)
                    else : 
                        print("personaje no encontrado")
                case 5:
                    nombre= input("como desea llamar al archivo ")
                    validacion=re.match(r"^[a-zA-Z0-9]+$",nombre)
                    if validacion!= None:
                        ruta="C:\\programacion I\\recuperatorio\\"+nombre+".csv"
                        exportar_csv(ruta,lista_copiada,False)
                    else:
                        print("caracter no valido") 
                case 6: 
                    lista_actualizada=Actualizar_Personajes() 
                    for i  in lista_actualizada:
                        print("nombre completo: {0}\naltura: {1}\npeso: {2}\ngenero: {3}\nlikes: {4}".format(i["nombre"],
                                                                                                    i["altura"],i["peso"],
                                                                                                i["genero"],i["likes"]))
                        print(patron4) 
                case 7:
                    lista_actualizada=Actualizar_Personajes() 
                    nombre= input("como desea llamar al archivo ")
                    validacion=re.match(r"^[a-zA-Z0-9]+$",nombre) 
                    if validacion!= None:
                        ruta="C:\\programacion I\\recuperatorio\\"+nombre+".csv"
                        exportar_csv(ruta,lista_actualizada,True)
                    else:
                        print("caracter no valido") 
                case 8:
                    lista_actualizada=Actualizar_Personajes()
                    respuesta=input("a partir de cuantos likes queres listar los personajes: ")
                    print(patron3)
                    while re.search(r"[0-9]+",respuesta)==None:
                        respuesta=input("error ingresa un numero: ")
                    respuesta=int(respuesta)
                    buscar_likes(lista_actualizada,respuesta)
                case 9:
                    break
menu_principal()