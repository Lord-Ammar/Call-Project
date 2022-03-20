import os,time
from colorama import Fore,init

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK

load = '█'
count = 0

try:
	for t in range(31):
	    time.sleep(1)
	    print(f'\r\033[1;97mProcess \033[1;93m(\033[1;92m {t} \033[1;93m) \n', end='', flush=True)
	    count += 1
	    if count == 1:
	    	count = 0
	    	load += '█'
except KeyboardInterrupt:
	print ("")
	print ("Program Dihentikan")
