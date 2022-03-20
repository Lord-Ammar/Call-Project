try:
	import os,sys,time,requests,json
	from colorama import Back,Fore,init
except ModuleNotFound:
	print("Install Module Dulu Ngab ! !")
	time.sleep(2)
	os.system("xdg-open https://bit.ly/AmmarExecuted")

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
ip = requests.get('https://api.ipify.org').text
server = ("https://id.jagreward.com")
load = '█'
count = 0

def anim():
	for t in range(10):
	    time.sleep(1)
	    print(f'\rLoading ( {t} ) ', end='', flush=True)
	    count += 1
	    if count == 1:
	    	count = 0
	    	load += '█'

def animasi():
      for i in "123456789123456789":
              print(f'\rStarting ({i}) ',end="",flush=True)
              time.sleep(1)

os.system("xdg-open https://bit.ly/AmmarExecuted")
os.system("clear")
print ("\033[1;97m─────\033[1;93m▀▄▀\033[1;97m─────\033[1;93m▄\033[1;97m─────\033[1;93m▄")
print ("\033[1;97m──\033[1;93m▄███████▄\033[1;97m──\033[1;93m▀██▄██▀ \033[1;97m[\033[1;0m\033[1;41mSpam Call Tools By AmmarBN\033[1;0m\033[1;97m]")
print ("\033[1;93m▄█████▀█████▄\033[1;97m──\033[1;93m▄█\033[1;96m╔═╗\033[1;97m┌─┐┬  ┬    \033[1;95m╔═╗\033[1;97m┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐")
print ("\033[1;93m███████▀████████▀\033[1;96m║  \033[1;97m├─┤│  │    \033[1;95m╠═╝\033[1;97m├┬┘│ │ │├┤ │   │")
print ("\033[1;97m─\033[1;93m▄▄▄▄▄▄███████▀\033[1;97m──\033[1;96m╚═╝\033[1;97m┴ ┴┴─┘┴─┘  \033[1;95m╩  \033[1;97m┴└─└─┘└┘└─┘└─┘ ┴")
print ("╭––––––╮\033[1;97m[\033[1;95m•\033[1;97m] Ip Address:\033[1;92m "+ip)
print ("\033[1;97m├  \033[1;92m••\033[1;97m  ┤\033[1;97m[\033[1;95m•\033[1;97m] Total User:\033[1;92m 1")
print ("\033[1;97m╰––––––╯\033[1;97m[\033[1;95m•\033[1;97m] Server:\033[1;92m "+server)

try:
	print("")
	print (Fore.WHITE+"["+Fore.RED+"!"+Fore.WHITE+"] Limit: 3x 15 menit\n"+Fore.WHITE+"["+Fore.RED+"!"+Fore.WHITE+"] Example:"+Fore.GREEN+"8xx\n"+Fore.WHITE+"["+Fore.RED+"!"+Fore.WHITE+"] Delay: 30 detik\n")
	nomor = input("\033[1;97m[\033[1;96m~\033[1;97m] Nomor:\033[1;92m ")
	jumlah = int(input("\033[1;97m[\033[1;96m~\033[1;97m] Jumlah:\033[1;92m "))
except KeyboardInterrupt:
	print (Fore.WHITE+"["+Fore.RED+"•"+Fore.WHITE+"] Program Dihentikan")
except ValueError:
	exit (Fore.WHITE+"Isi Yang Bener "+Fore.RED+"! !"+Fore.WHITE)

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}


try:
	for i in range(jumlah):
	    send = requests.post(url+nomor, headers=ua, data=dat)
	    print(Fore.WHITE+"[\033[1;93m•"+Fore.WHITE+"] Status -► ",(send.json()["message"]))
	    os.system("python load.py")
	print (Fore.WHITE+"Spam Selesai "+Fore.GREEN+"✓")

except NameError: 
	print (Fore.WHITE+"["+Fore.RED+"•"+Fore.WHITE+"] Program Dihentikan")
except KeyboardInterrupt:
	print (Fore.WHITE+"["+Fore.RED+"•"+Fore.WHITE+"] Program Dihentikan")
