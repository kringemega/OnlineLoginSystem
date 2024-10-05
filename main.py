
import subprocess, requests, time, os
import sys


hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('your pasta')

try:
    if hwid in r.text:
        pass
    else:
        print('Ошибка, данных hwid не был найден в базе данных')
        print(f'HWID: {hwid}')
        time.sleep(5)
        os._exit()
except:
    print('Ошибка, не удаётся соединится с базой данных')
    time.sleep(5)
    os._exit()
logr = input("Enter login:")
login = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('your pasta')

try:
    if logr in r.text:
        pass
    else:
        print('Ошибка, данных login не был найден в базе данных')
        time.sleep(5)
        os._exit()
except:
    print('Ошибка, не удаётся соединится с базой данных')
    time.sleep(5)
    os._exit()


passw = input("Enter password:")


login = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('your pasta')

try:
    if passw in r.text:
        pass
    else:
        print('Ошибка, данных password не был найден в базе данных')
        time.sleep(5)
        os._exit()
except:
    print('Ошибка, не удаётся соединится с базой данных')
    time.sleep(5)
    os._exit()
animation = "◇*◇*◇"

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("Авторизация успешна")
text = "Добро пожаловать"
time.sleep(1)
for _ in range(3):
    print(text, logr, "!", end="")
    time.sleep(0.5)
    print("\r", end="")
    time.sleep(0.5)
input("")
