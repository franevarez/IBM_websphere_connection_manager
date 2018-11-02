# -*- encoding: utf-8 -*-
#!/usr/bin/env python3

import os
import sys
import win32com.client

#directorio de properties
configs = open("config.txt", "r")

bin = configs.readline().strip()
server = configs.readline().strip()
dir = configs.readline().strip()

#Nombres de carpetas de aplicacionea
dirProd = configs.readline().strip()
dirMotor = configs.readline().strip()
dirConsulta = configs.readline().strip()
configs.close()

banderaReStart = False
shell = win32com.client.Dispatch("WScript.Shell")

#Funciones para cambiar los directorios de conexiones
def cambioDES(dirChange):
    os.rename(dir+dirChange, dir+"QAS-"+dirChange)
    os.rename(dir+"DES-"+dirChange, dir+dirChange)

def cambioQAS(dirChange):
    os.rename(dir+dirChange, dir+"DES-"+dirChange)
    os.rename(dir+"QAS-"+dirChange, dir+dirChange)
 
while True:
    #Se determina que conexion se tiene asignada
    if os.path.exists(dir+'DES-'+dirProd):
        conexionActualPortal = 'QAS'

    if os.path.exists(dir+'QAS-'+dirProd):
        conexionActualPortal = 'DES'

    if os.path.exists(dir+'DES-'+dirMotor):
        conexionActualMotor = 'QAS'

    if os.path.exists(dir+'QAS-'+dirMotor):
        conexionActualMotor = 'DES'

    if os.path.exists(dir+'DES-'+dirConsulta):
        conexionActualConsultas = 'QAS'

    if os.path.exists(dir+'QAS-'+dirConsulta):
        conexionActualConsultas = 'DES'

    #Menu de seleccion
    print("Elige a que aplicacion le deseas cambiar la conexion\n")
    print('1 .- Portal: ', conexionActualPortal)
    print('2 .- Motor: ', conexionActualMotor)
    print('3 .- Consultas: ', conexionActualConsultas)
    print("\n\n0 .- Salir\n\n")

    #input de opcion seleccionada
    ConexionInput = int(input('¿Que conexion desea cambiar?: '))

    #Compara que conexion tiene asignada para realizar el cambio

    #Opcion uno para el portal
    if ConexionInput != 0:
        banderaReStart = True

    if ConexionInput == 1:
        print('Cambiando conexion del portal')
        if conexionActualPortal == 'DES':
            cambioQAS(dirProd)

        if conexionActualPortal == 'QAS':
            cambioDES(dirProd)

    #Opcion dos para el motor
    elif ConexionInput == 2:
        if conexionActualMotor == 'DES':
            cambioQAS(dirMotor)
        if conexionActualMotor == 'QAS':
            cambioDES(dirMotor)

    #Opcion tres para consultas
    elif ConexionInput == 3:
        if conexionActualConsultas == 'DES':
            cambioQAS(dirConsulta)
        if conexionActualConsultas == 'QAS':
            cambioDES(dirConsulta)

    elif ConexionInput == 0:
        print('\n\nQue tengas en buen día ;)')
        if banderaReStart:
            os.system(bin+'\stopServer '+server)
            #os.system(bin+'\startServer '+server) reinicia el servidor pero eclipse no lo detecta :,C
            #shell.AppActivate("firefox")
            #shell.SendKeys('^+R', 0)
        exit()
    #Error en caso de elegir opcion no disponible
    else:
            print('Opcion no valida. ')