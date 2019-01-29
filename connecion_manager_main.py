# -*- coding: utf-8 *-*

# imports
import os
import configparser
import sys
import traceback
    
# import win32com.client

import source.conexiones as conexiones_
import source.conexiones_gui as conexiones_gui

aplications_list = []
connections_list = []
banderaReStart = False

instrucciones = '''
    -MENU,-menu         --Show menu
    -a,-A <aplication>  --firs command for selecct aplication
    -c-C <connection>   --second comand for sellect conection
    -gui                --display gui 

    Exemple ".py -a motor -c QAS"

    --help               --Show help'''
try:
    # configparser for get configurations
    cur_path = os.path.dirname(os.path.abspath(__file__))

    Config = configparser.ConfigParser()
    Config.read(cur_path + '/configs/config.ini')

    print(cur_path)

    # Information of server and location cennctions
    server_location = Config['server']['server_location']
    server_name = Config['server']['server_name']
    was_location = Config['server']['was_location']

    connections_list = Config['connections']

    # direcctories of aplications
    for app_list in Config['applications']:
        aplications_list.append(conexiones_.aplicacion(
                                app_list, Config['applications'][app_list], was_location,
                                connections_list[app_list]))

    if len(sys.argv) > 1:
        if sys.argv[1] == '-menu' or sys.argv[1] == '-MENU':
            print("Estas entrando al menu")
            conexiones_.showMenu(aplications_list, server_name, server_location)

        elif sys.argv[1] == '-gui' or sys.argv[1] == '-GUI':
            conexiones_gui.showGui(aplications_list, server_name, server_location)
        else:
            if conexiones_.config_with_command(sys.argv, aplications_list, server_name, server_location):
                exit()
            else:
                print(instrucciones)
    else:
        print(instrucciones)
except Exception as e:
    print(traceback.print_exc())
    print("""\n\nSorry the configuration is bad please read the confiuration 
    in the file README.md or is a problem with the code please report franevarez@gmail.com\n""")
