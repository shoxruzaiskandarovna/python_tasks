import datetime as dt

hozir = dt.datetime.now()
print(hozir)
#sanani ajratib olish
print(hozir.date())
#vaqtni ajratb olish
print(hozir.time)
print(hozir.hour)
print(hozir.minute)
print(hozir.second)

bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")
ertaga = dt.date(2025, 10, 5)
print(f"Eratngi sana: {ertaga}")

vaqtKeyin = dt.time(23,45,00)
print(vaqtKeyin)

bugun = dt.date.today()
new_year = dt.date(2025,12,31)
farq = new_year-bugun
print(f"yangi yilga: {farq} kun qoldi")

#vaqtni millisequndsz chiqaramz
vaqt = hozir.strftime("%H:%M:%S")
print(f"hozir soat: {vaqt}")
#sana kun oy yil korinirshd achqaramz
sana = hozir.strftime("%d-%m-%y")
print(f"Bugun sana: {sana}")
sana_vaqt = hozir.strftime("%d/%m/%y, %H:%M")
print(sana_vaqt)

import re
from uzwords import words

andoza = "^т...р$"

matches = []
for word in words:
    if re.match(andoza,word):
        matches.append(word)
print(matches)

matn=""" mksdmckwsajkdnwijnqpaofjpdokmvlaksdmfi232jedpOQWDFPAWNGPJGNVP4RHP1Q2S4DKXCRN 
 sevinchKarimboyeva123@gmail.com
 wejd0QYHPieecpqkjxkqbqwd o;djhq38jxhnh"""
andoza="[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
email=re.findall(andoza,matn)
print(email)


#kuchlik parolni tekshirish
#Quyidaki andoza ham ihateregah.io sahifasidan olindi
msg="Yangi parol kiriting:"
msg+='(kamida 8 belgidan iborat,kamida 1 ta lotin bosh harf, 1ta kichik harf)'
msg+='1 ta son va 1 ta maxsus belgi bolishi kerak'

while True:
    password=input(msg)
    if re.match(andoza,password):
        print("Maxfi so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z qabul qilinmadi")