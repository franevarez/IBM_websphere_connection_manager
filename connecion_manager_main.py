# -*- coding: utf-8 *-*

#imports
import os
import configparser
import sys

import win32com.client

import source.conexiones as SC


aplications_list = []
banderaReStart = False

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
for app_list in Config['applications']:
    aplications_list.append(SC.aplicacion(
        app_list, Config['applications'][app_list], was_location))

if len(sys.argv) > 1:
    if sys.argv[1] == '-menu' or sys.argv[1] == '-MENU':
        print("Estas entrando al menu")
        SC.showMenu(aplications_list, server_name, server_location)

    elif sys.argv[1] == '-gui' or sys.argv[1] == '-GUI':
        pass
    else:
        if SC.config_with_command(
           sys.argv, aplications_list):
           exit()
        else:
            print(instrucciones)
else:
    print(instrucciones)
