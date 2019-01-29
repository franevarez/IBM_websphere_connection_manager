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
        for con in self.connection_list:
            if not os.path.exists(self.dir+con+'-'+self.dir_app):
                self.conexionActual = con
                break

    def changeConnectionMenu(self, Conexion_Input):
        print("intenta hacer el cambio")

        if self.connection_list[Conexion_Input] != self.conexionActual:
            print("intenta hacer cambio a ",
                  self.connection_list[Conexion_Input])

            os.rename(self.dir+self.dir_app, self.dir +
                      self.conexionActual+"-"+self.dir_app)
            os.rename(
                self.dir+self.connection_list[Conexion_Input]+"-"+self.dir_app, self.dir+self.dir_app)
            self.updateStatus()

    def changeConnectionCom(self, Conexion_Input):
        print("intenta hacer el cambio")

        print("intenta hacer cambio a ", Conexion_Input)
        
        os.rename(self.dir+self.dir_app, self.dir+self.conexionActual+"-"+self.dir_app)
        os.rename(self.dir+Conexion_Input+"-" +
                  self.dir_app, self.dir+self.dir_app)
        self.updateStatus()


def showMenu(aplicaciones, server, server_location):
    banderaReStart = False 
    banderaNoselecc = False
    while True:
        if os.name == "nt":
            os.system("cls")

        elif os.name == "posix":
            os.system("clear")

        if banderaNoselecc:
            print("\033[93m La aplicacion que selecciono no esta disponible, favor de elegir otra o salir.\033[0m\n")

           # Menu de seleccion
        print("Elige a que aplicacion le deseas cambiar la conexion\n")

        indice = 1
        for obc_aplication in aplicaciones:
            print((indice), '.- ', obc_aplication.name,': ',
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

        elif aplicacion_Input < len(aplicaciones):
            appV = aplicaciones[aplicacion_Input-1]
            if len(appV.connection_list) > 2:
                indice = 1
                print("Que conexion desea asiganar\n")
                for list_conection in appV.connection_list:
                    print((indice), '.- ', list_conection)
                    indice += 1
                    
                Conexion_Input = int(input('¿Que conexion desea cambiar?: '))
                
                appV.changeConnectionMenu(Conexion_Input-1)
            else:
                if appV.connection_list[0] == appV.conexionActual:
                    appV.changeConnectionMenu(1)
                else:
                     appV.changeConnectionMenu(0)
        else:
            banderaNoselecc = True
                


def config_with_command(comandos, aplications_list, server, server_location):
    try:
        comands = [k.lower() for k in comandos]
        aplicacion_In = comands[comands.index("-a")+1]
        conecction = comands[comands.index("-c")+1].upper()

        for list_aplications in aplications_list:
            if aplicacion_In in list_aplications.name:
                if conecction != list_aplications.conexionActual:
                    list_aplications.changeConnectionCom(conecction)
                    print('Cambio de conexion correcta')
                    os.system(server_location+'\\stopServer '+server)
                    print('\n Listo, todo salio bien ;)')
                    return True
                else:
                    print('conexion ya se encontraba configurada')
                    return True
    except:
        print('\nlos argumentos no son correctos')
        return False