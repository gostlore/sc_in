# -*- coding:utf -8 -*-
import socket
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'


def range_list( host ):
    port = list(range(1, 44444))
    for i in port:
        try:
            scan = socket.socket()
            scan.settimeout(0.1)
            scan.connect((host, i))
            print(bcolors.GREEN + "Port -- ", i, " -- [OPEN]")
        except:
            pass

def list_all( host ):
    color_a = (bcolors.GREEN + "[+] " + bcolors.ENDC)
    color_b = (bcolors.RED + "[!] " + bcolors.ENDC)
    color_c = (bcolors.YELLOW + "[!] " + bcolors.ENDC)
    print("\n")
    print( host )
    ports = [21, 22, 23, 25, 38, 43, 50, 51, 53, 55, 56, 57, 80, 109, 110, 115, 118, 119, 143,
             194, 220, 443, 445, 540, 585, 591, 1112, 1113, 1433, 1443, 3128, 3197,
             3306, 4000, 4444,  4333, 5100, 5432, 6669, 8000, 8080, 9014, 9200]

    for i in ports:
        try:
            scan = socket.socket()
            scan.settimeout(0.1)
            scan.connect((host, i))
            print(bcolors.GREEN + "Port -- ", i, " -- [OPEN]" + bcolors.ENDC)
        except:
            pass


