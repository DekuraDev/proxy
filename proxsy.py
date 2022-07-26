import os,sys,json,requests,time,platform


### Headers ###

api_key = "cee1b8717ad9967aac3b655ecb55bca6"

header = {
    "useragent": "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0",
    "content-Type": "application/json"
}


### url ###

url = f"http://api.scraperapi.com?api_key={api_key}&url=http://httpbin.org/ip"


### Clear system ###

if ("windows" in sys.platform.lower()):
    clear = os.system("cls")
else:
    clear = os.system("clear")


### Main ###

try:
    response = requests.get(url,headers=header).json()
except requests.exceptions.ConnectionError:
    print(" maaf kesalahan jaringan")
    exit()
clear
print("""    ____           __                          
   / __ \  ___    / /__  __  __   _____  ____ _
  / / / / / _ \  / //_/ / / / /  / ___/ / __ `/
 / /_/ / /  __/ / ,<   / /_/ /  / /    / /_/ / 
/_____/  \___/ /_/|_|  \__,_/  /_/     \__,_/ Dev
""")
input("\n run sc? ")
print("\n tunggu sebentar...")
time.sleep(1.5)
print(f" proxsy: {response['origin']}")
time.sleep(1.5)
print(" save as files? y/t")
pil = input(" y/t: ")
if pil in [""," ","y","Y"]:
    with open("proxs.txt","w") as simpan:
        simpan.write(response["origin"])
    print(" file save as proxs.txt")
    exit()
else:
    print(" anda telah keluar program!")
    exit()