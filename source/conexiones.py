# -*- coding: utf-8 *-*

import os
import sys

class aplicacion():
    def __init__(self, name, dir_aplication, was_location,connection_list):
        self.dir_app = dir_aplication
        self.dir = was_location
        self.name = name
        self.connection_list = connection_list.split(',')
        self.updateStatus()

    def updateStatus(self):
        
        for connection_list in self.connection_list:
            if not os.path.exists(self.dir+connection_list+'-'+self.dir_app):
                print(self.dir+connection_list+'-'+self.dir_app)
                self.conexionActual = connection_list

    def changeConnection(self, Conexion_Input):
        print("intenta hacer el cambio")
        
        if self.connection_list[Conexion_Input] != self.conexionActual:
            print("intenta hacer cambio a ", self.connection_list[Conexion_Input])
            
            os.rename(self.dir+self.dir_app, self.dir+self.conexionActual+"-"+self.dir_app)
            os.rename(self.dir+self.connection_list[Conexion_Input]+"-"+self.dir_app, self.dir+self.dir_app)
        
#         if self.conexionActual == 'DES':
#             self.cambioQAS()
#         if self.conexionActual == 'QAS':
#             self.cambioDES()
#         self.updateStatus()

    #Funciones para cambiar los directorios de conexiones
#     def cambioDES(self):
#         print("intenta hacer el DES")
#         os.rename(self.dir+self.dir_app, self.dir+"QAS-"+self.dir_app)
#         os.rename(self.dir+"DES-"+self.dir_app, self.dir+self.dir_app)
# 
#     def cambioQAS(self):
#         print("intenta hacer el QAS")
#         os.rename(self.dir+self.dir_app, self.dir+"DES-"+self.dir_app)
#         os.rename(self.dir+"QAS-"+self.dir_app, self.dir+self.dir_app)

def showMenu(aplicaciones ,server,server_location):
    banderaReStart = False #
    while True:
        if os.name == "nt":
            os.system("cls")

        elif os.name == "posix":
            os.system("clear")

            #Menu de seleccion
        print("Elige a que aplicacion le deseas cambiar la conexion\n")

        indice = 1
        for obc_aplication in aplicaciones:
            print((indice), '.- ', obc_aplication.name,
                  ': ',
                   obc_aplication.conexionActual)
            indice += 1

        print("\n0 .- Salir\n\n")

        #input de opcion seleccionada
        aplicacion_Input = int(input('¿Que conexion desea cambiar?: '))

        #Compara que conexion tiene asignada para realizar el cambio}

        if aplicacion_Input != 0:
            banderaReStart = True

        if aplicacion_Input == 0:
            print('\n\nQue tengas en buen día ;)')
            if banderaReStart:
                os.system(server_location+'\\stopServer '+server)
                #os.system(bin+'\startServer '+server) reinicia el 
                #servidor pero eclipse no lo detecta :,C
                #shell.AppActivate("firefox")
                #shell.SendKeys('^+R', 0)
            exit()
        else:
            indice = 1
            print("Que conexion desea asiganar\n")
            for list_conection in aplicaciones[aplicacion_Input-1].connection_list:
                print((indice), '.- ', list_conection)
                indice += 1
                
            Conexion_Input = int(input('¿Que conexion desea cambiar?: '))
            
            aplicaciones[ConexionInput].changeConnection(Conexion_Input)
#             ConexionInput -=1
#             aplicaciones[ConexionInput].changeConnection()

def config_with_command(comandos, aplications_list):
    try:
        comands = [k.lower() for k in comandos]
        aplicacion = str(comands[comands.index("-a")+1])
        conecction = comands[comands.index("-c")+1].upper()

        print(aplicacion)
        print(conecction)

        for list_aplications in aplications_list:
            print(aplicacion.lower in str(list_aplications.name))
            if aplicacion.lower in list_aplications.name:
                print(">>>>>>>>>")
                if conecction != list_aplications.conexionActual:
                    list_aplications.changeConnection()
                    print('Cambio de conexion correcta')
                    return True
                else:
                    print('conexion ya se encontraba configurada')
                    return True
    except:
        print('\nlos argumentos no son correctos')
        return False
