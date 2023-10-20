import pywhatkit
import random

# Telefon numaralarını ve isimleri dosyalardan oku
with open("phoneno.txt", "r", encoding="UTF-8") as f:
    phone_numbers = [line.strip() for line in f]

with open("namefile.txt", "r",encoding="UTF-8") as f:
    names = [line.strip() for line in f]

with open("cumamesaj.txt", "r",encoding="UTF-8") as f:
    msg = f.readlines()    


#strip kodu bir dizedeki baştaki ve sondaki boşlukları (ve diğer boşluk karakterlerini) kaldırır. Bu, her satırdaki gereksiz boşlukları temizlemek için kullanılır.

hour = int(input("Göndermek istediğiniz saati girin: "))
minute = int(input("Göndermek istediğiniz dakikayı girin: "))
hours = int(hour)
min = int(minute)
wait_time = 10  # Mesaj gönderdikten sonra bekleme süresi (saniye)
i = 0

while i<4:
    random.shuffle(msg)
    typeMessage = random.choice(msg)        
    phone_number = phone_numbers[i % len(phone_numbers)] #döngünün karışmaması için listeden telefon numarası seçerken sıra ekliyoruz i değişkeni ile
    name = names[i % len(names)] #döngünün karışmaması için listeden isim seçerken sıra ekliyoruz i değişkeni ile
    
    message = f"Sayın {name},{typeMessage}.Bu mesaj Halit Arzupınar tarafından python kodu ile gönderilmiştir"

    print(f"{i}. mesaj gönderiliyor: {message} ({phone_number})")

    pywhatkit.sendwhatmsg(phone_no=phone_number, message=message, time_hour=hours, time_min=min, wait_time=wait_time )

    min +=1
    if min >= 60:
        min = 0
        hours += 1
        if hours >= 24:
            hours = 0
    i+=1        
      # Dakikayı arttır ve saat/dakika sınırlarına dikkat et        
      
      