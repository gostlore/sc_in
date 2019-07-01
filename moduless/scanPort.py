# -*- coding:utf -8 -*-
import socket
from multiprocessing import Pool
import time



def range_list():

    color_red = colored("[!] ", 'red')
    color_yellow = colored("[!] ", 'yellow')
    color_green = colored("[+] ", 'green')
    print("Введите диапазон портов ОТ и ДО: ")
    LP = []
    host = input( + "ENTER YOUR HOST--> ")
    ot = int(input("От какого порта начинать сканирование : "))
    do = int(input("До какого порта сканировать : "))
    LP = list(range(ot, do))
    A = LP
    port = A
    for i in port:
        try:
            scan = socket.socket()
            scan.settimeout(0.1)
            scan.connect((host, i))
            print(bcolors.GREEN + "Port -- ", i, " -- [OPEN]")
        except:
            pass

def list_all():
    color_a = (bcolors.GREEN + "[+] " + bcolors.ENDC)
    color_b = (bcolors.RED + "[!] " + bcolors.ENDC)
    color_c = (bcolors.YELLOW + "[!] " + bcolors.ENDC)
    host = input(color_a + "Host --> ")
    print("\n")
    LP = list(range(1, 166))
    A = LP
    port = A
    for i in port:
        try:
            scan = socket.socket()
            scan.settimeout(0.1)
            scan.connect((host, i))
            print(bcolors.GREEN + "Port -- ", i, " -- [OPEN]" + bcolors.ENDC)
        except:
            pass


def manu_entera():

    menu = (""" -----------------------------------------------------------------
    -\t[1] ----- сканировать отделный порт                            -    
    -\t[2] ----- сканировать все возможные порты                      -
    -\t[3] ----- задать свой диапазон портов, для сканирвоание        -
    -\t[4] ----- Помощь 
     -----------------------------------------------------------------
    """)
    print(menu)
    main_menu = input("terminal#: ")
    if main_menu == "1":
        one_port()
    elif main_menu == "2":
        list_all()
    elif main_menu == "3":
        range_list()
    elif main_menu == "4":
        HELP()
    else:
        print(colored("Параметр введен не правильно!", 'red'))
