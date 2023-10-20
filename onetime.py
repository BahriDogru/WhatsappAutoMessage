import pywhatkit
import random

# Telefon numaralarını ve isimleri dosyalardan oku


with open("GünaydınMesajları.txt", "r",encoding="UTF-8") as f:
    msg = f.readlines()
    random.shuffle(msg)
    typeMessage = random.choice(msg)        


#strip kodu bir dizedeki baştaki ve sondaki boşlukları (ve diğer boşluk karakterlerini) kaldırır. Bu, her satırdaki gereksiz boşlukları temizlemek için kullanılır.
phone_number = input("Göndermek istediğiniz telefon numarasını girin: ")
hour = int(input("Göndermek istediğiniz saati girin: "))
minute = int(input("Göndermek istediğiniz dakikayı girin: "))
hours = int(hour)
min = int(minute)
wait_time = 10  # Mesaj gönderdikten sonra bekleme süresi (saniye)
i = 0

message = f"{typeMessage}.Bu mesaj Halit Arzupınar tarafından python kodu ile gönderilmiştir"

print(f"{i}. mesaj gönderiliyor: {message} ({phone_number})")

pywhatkit.sendwhatmsg(phone_no=phone_number, message=message, time_hour=hours, time_min=min, wait_time=wait_time )


      
      