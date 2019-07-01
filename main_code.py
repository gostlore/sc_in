import moduless.ipinfojson
import namedModules.scanPort
import os
import subprocess

getInfoIp = moduless.ipinfojson.infoip
getInfoDomen = moduless.ipinfojson.infodomen
geteScanPort = namedModules.scanPort.list_all
geteScanPortmanually = namedModules.scanPort.range_list
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


print_set_modules = ("""
\t                 Список модулей
\t#------------------------------------------------#
\t| [1] --- Узнать информацию об IP                |  
\t| [2] --- Узнать информацию о сайте              |     
\t| [3] --- Сканер портов(стандартных портов)      |
\t| [4] --- Сканер портов(c 1-44444 port)          |
\t| [5] --- Узнать свой IP                         |
\t| [6| --- Сменить свой IP                        | 
\t| [7] --- Проверить IP на уязвимость |EternalBlue|
\t| [8] === Вывести список команд                  |
\t#------------------------------------------------#
                                              """)
info_scan_port = bcolors.YELLOW + """Скан по таким портам =>> 21, 22, 23, 25, 38, 43, 50, 51, 53, 55, 56, 57 80,
              109, 110, 115, 118, 119, 143,
             194, 220, 443, 445, 540, 585, 591, 1112, 1113, 1433, 1443, 3128, 3197,
             3306, 4000, 4444,  4333, 5100, 5432, 6669, 8000, 8080, 9014, 9200""" + bcolors.ENDC


sos = bcolors.YELLOW + print_set_modules + bcolors.ENDC
cos = ("""
\t                Список команд
\t#-----------------------------------------#
\t | [1] => exit/Выход из программы          |
\t | [2] => back/Вернуться назад.            |
\t | [3] => modules/Вывести список модулей   |
\t#-----------------------------------------#
""")
my_command = bcolors.BLUE + cos + bcolors.BLUE
ipasaaa = bcolors.RED + " [ERROR!!!] ===>>  Ip not found!" + bcolors.ENDC
domasaaa = bcolors.RED + " [ERROR!!!] ===>>  Domen not found!" + bcolors.ENDC
domasaaaIP = bcolors.RED + " [ERROR!!!] ====> Domen/IP not found!"  +  bcolors.ENDC

def all_set_modules ():
    all_modules = input("Выбрайте модуль =>> : ")
    if all_modules == "1":
        try:
            enter_ip = input(" [+]====> Введите IP : " ) # запрашиваем у пользователя ip
            cheack_ip = getInfoIp(enter_ip)
            print("-" * 60)

        except:
            print(ipasaaa)


    elif all_modules == "2":
        print("Узнаем информацию о сайте")
        try:
            print("Пример =>> youtube.com")
            enter_domenn = input("Введите домен => : ")
            push = getInfoDomen(enter_domenn)
            print("-" * 60)
        except:
            print(domasaaa)

    elif all_modules == "3":
        print("-"*55)
        print(info_scan_port)
        try:

            qweasd = bcolors.GREEN + "Пример ввода =>>> 83.34.343.2/youtube.com" + bcolors.ENDC
            print(qweasd)
            rea = input("Введите IP/domen =>> : ")
            push_rea = geteScanPort(rea)

        except:
            print(domasaaaIP)
    elif all_modules == "4":
        print("-"*55)
        try:
            bobo = input("Введите айпи,домен =>> :")
            re_bobo = geteScanPortmanually(bobo)
        except:
            print()

    elif all_modules == "5":
        print("-"*55)
        try:
            myComand = "wget " + "-qO- " + "eth0.me"
            myIpwho = os.popen( myComand ).read()
            print("Ваш IP =>>>", myIpwho)
        except:
            print("ERROR")

    elif all_modules == "6":
        print("-"*55)
        try:
            qwe_qweasd = subprocess.call(["torghost"])
            qwe_qweasdzxc = subprocess.call(["torghost", "switch"])
            print(qwe_qweasd)
            print(qwe_qweasdzxc)
            mmyComand = "wget " + "-qO- " + "eth0.me"
            myIpwhoo = os.popen(mmyComand).read()
            print("Ваш IP =>>>", myIpwhoo)
        except:
            print("ERROR")
    elif all_modules == "7":
        print("-"*55)
        try:
            enter_target_ip = input("Введите айпи который хотите проверить =>>> : ")
            mmmmyComand = "nmap " + "-p " + "445 " + "-Pn " + "--script " + "smb-vuln-ms17-010" + enter_target_ip
            vuln = os.popen(mmmmyComand).read()
        except:
            print("ERROR")

    elif all_modules == "8":
        print("-"*54)
        comand()

    comand()

def comand (): # функция направлена на исполнение выбранной пользователем команды
    print(my_command)
    comand = input("[$] --> ")

    if comand == "1": exit( "Close program... " )
    elif comand == "2": print(comand())
    elif comand == "3":

        print(sos)
        print(all_set_modules())
    else:

        print ( "[Error]: Comand not found!" )
        print ( comand () )


print(comand())


