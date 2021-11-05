import socket
import sys
from datetime import datetime
import subprocess, platform
#โอ้คุณอยากเรียนรู้วิธีการเขียนมันหรอคุณสามารถสอบถามผมได้ที่เฟสบุ๊ค https://www.facebook.com/messages/t/104704474962816
#บางทีผมอาจช่วยคุณได้

def clear():
    if platform.system() == "Windows":
        subprocess.Popen("cls",
                         shell=True).communicate()
    else:  # Linux and Mac
        print("\033c", end="")

clear()
print("enter web URL")
print("example Target : example.com")
target = input("Target : ") #เป้าหมายของเราที่จะสแกนport
IP = socket.gethostbyname(str(target)) #มีไว้สำหรับหา IP ของเป้าหมายของเรา
clear()
print("")
print("")
print("")
print("IP of target is " + str(IP))
print("")
print("scan port")
print("Please wait.....")

timestart = datetime.now() #ตัวจับเวลาตัวแรก

try: #สแกน Port
    for p in range(1, 9999): #ให้สแกนจากเลข 1 - 9999
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((IP, p))
        if res == 0:
            if str(p) == "21":
                print("Connect in port " + str(p) + " FTP") #ให้แสดง port ที่แสกนได้
            elif str(p) == "22":
                print("Connect in port " + str(p) + " SSH")
            elif str(p) == "23":
                print("Connect in port " + str(p) + " telnet")
            elif str(p) == "25":
                print("Connect in port " + str(p) + " smtp")
            elif str(p) == "53":
                print("Connect in port " + str(p) + " dns")
            elif str(p) == "80":
                print("Connect in port " + str(p) + " http")
            elif str(p) == "443":
                print("Connect in port " + str(p) + " https")
            elif str(p) == "5060":
                print("Connect in port " + str(p) + " SIP")
            elif str(p) == "135":
                print("Connect in port " + str(p) + " zero day")
            elif str(p) == "3306":
                print("Connect in port " + str(p) + " MySQL")
            else:
                print("Connect in port " + str(p) + " unknow")

        sock.close()

except Exception:
    print("error")
    sys.exit()

timestop = datetime.now() #ตัวจับเวลาอันที่2
time = timestop - timestart #ตัวจับเวลามันจะจับแบบนับถอยหลังจาก12ชม.ฉนันให้เราเอาเวลาที่เริ่มจับตอนแรกมาลบกับตัวที่เสร็จจะได้เวลาที่เราใช้ไป

print("Scan completed in " + str(time)) #ตัวแสดงเวลาที่ใช้ไปในการสแกน(จริงๆมันไม่ได้จำเป็นหรอก)
