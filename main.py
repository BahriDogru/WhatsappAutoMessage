import pywhatkit
import random

phone_number ="+905019031903"
when = input("Mesajı göndermek istediğiniz saat ve dakika(örnek:19:03): ")
hour, munite = when.split(":")

with open("MassegeFile.txt", "r", encoding="UTF-8") as f:
    msg = f.readlines()
    random.shuffle(msg)
    message = random.choice(msg)

pywhatkit.sendwhatmsg(phone_no=phone_number,message=message,time_hour=int(hour),time_min=int(munite),wait_time=10)