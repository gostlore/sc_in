#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import socket
import urllib.request
import json
import subprocess

def infodomen( domen_dome ):
    print("-" * 44)
    print("Получаем информацию о домене")
    checkip = socket.gethostbyname(domen_dome)
    rl_IP = domen_dome
    print(rl_IP)
    info_1 = "http://htmlweb.ru/analiz/api.php?whois&url=" + rl_IP + "&json"
    try:
        sub_info1 = urllib.request.urlopen(info_1)
    except:
        print("\n[!] - IP not found! - [!]\n")
    load_info = json.load(sub_info1)

    print("-" * 75)
    a = ("IP этого домена ", checkip)
    a1 = ("Кто это: ", load_info["whois"])
    a2 = ("Протокол домена ", load_info["schema"])
    a3 = ("domain: ", load_info["domain"])
    a4 = ("zone: ", load_info["zone"])
    a5 = ("Сколько сайту лет: ", load_info["age"])
    print(a)
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)


def infoip( sm_ip ):
    print("-" * 44)
    print("Получаем информацию об IP ")
    info_ip = "http://free.ipwhois.io/json/" + sm_ip
    try:
        tryopn = urllib.request.urlopen( info_ip )
    except:
        print("\t Некорректные данные")
    load_info = json.load(tryopn)
    print("-"*55)
    print("IP: ", load_info["ip"])
    print("Страна: ", load_info["country"])
    print("country_code ", load_info["country_code"])
    print("country_capital: ", load_info["country_capital"])
    print("region: ", load_info["country_phone"])
    print("city: ", load_info["city"])
    print("org: ", load_info["org"])
    print("isp ", load_info["isp"])
    print("timezone: ", load_info["timezone"])
    print("region: ", load_info["country_phone"])
    print("city: ", load_info["city"])
    print("-"*50)
    print("Выводим информацию с whois")
    print("-"*55)
    a = subprocess.run(["whois", sm_ip])
    print(a)



1
