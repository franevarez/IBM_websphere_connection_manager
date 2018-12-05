# -*- coding: utf-8 *-*

#imports
import os
import configparser
import sys

import win32com.client

import source.conexiones as SC

instrucciones = '''
    -MENU,-menu         --Show menu
    -a,-A <aplication>  --firs command for selecct aplication
    -c-C <connection>   --second comand for sellect conection
    -gui                --display gui 

    Exemple ".py -a motor -c QAS"

    --help               --Show help'''

#configparser for get configurations
Config = configparser.ConfigParser()
Config.read('configs/config.ini')

#Information of server and location cennctions
server_location = Config['server']['server_location']
server_name = Config['server']['server_name']
was_location = Config['server']['was_location']

#direcctories of aplications
dirProd = Config['applications']['portal_location']
dirMotor = Config['applications']['motor_location']
dirConsulta = Config['applications']['consultas_location']

banderaReStart = False

portal = SC.aplicacion(dirProd, was_location)
motor = SC.aplicacion(dirMotor, was_location)
consultas = SC.aplicacion(dirConsulta, was_location)

if len(sys.argv) > 1:
    if sys.argv[1] == '-menu' or sys.argv[1] == '-MENU':
        print("Estas entrando al menu")
        SC.showMenu(
            portal, motor, consultas, server_name, server_location)

    elif sys.argv[1] == '-gui' or sys.argv[1] == '-GUI':
        pass
    else:
        if SC.config_with_command(
           sys.argv, portal, motor, consultas):
           exit()

        else:
            print(instrucciones)
else:
    print(instrucciones)
