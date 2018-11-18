
import time
from bs4 import BeautifulSoup
import requests
import os

url = 'https://www.islom.uz/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
path = ''


namaazNames = soup.select('div.p_v')
namaazNames = [namaazName.text for namaazName in namaazNames]
namaazTimes = soup.select('div.p_clock')
namaazTimes = [namaazTime.text for namaazTime in namaazTimes]
del namaazNames[1]
del namaazTimes[1]

Bomdot = namaazTimes[0]											#
Peshin = namaazTimes[1]											#
Asr = namaazTimes[2]											#
Shom = namaazTimes[3]											#
Xufton = namaazTimes[4]											#
																#
Namoz_vaqtlari = (" Bomdot vaqti: {0}\n Peshin vaqti: {1}\n Asr vaqti: {2}\n Shom vaqti: {3}\n Xufton vaqti: {4}".format(Bomdot, Peshin, Asr, Shom, Xufton))
																#
																#
print(Namoz_vaqtlari)   

currentTime = time.strftime('%H:%M')   
localtime = time.localtime(time.time())

print(localtime[4])

#(localtime[3]) bu soat hour
#(localtime[4]) bu minut
# if localtime[3] > 9 :
#     if localtime[3] > Peshin[0]) and localtime[4] > Peshin and localtime[3] < Asr{} :
#         print("Hozir Peshin Vaqti \nAsr vaqti yaqinlashib kelmoqda[]".format(Asr))
#     if localtime[3] 



# if localtime[3] < 9 :
#     print(voaleykum)
print(Peshin[2,5])

# for namaazName, namaazTime in zip(namaazNames, namaazTimes):
#     with open(path + namaazName + '.txt', 'w') as file:
#         file.write(namaazTime)

# with open("Тонг.txt", "r") as my_new_handle:
#     for the_line in my_new_handle:

#         print("Bomdot",the_line)
#         Bomdot = (the_line)

# with open("Пешин.txt", "r") as my_new_handle:
#     for the_line in my_new_handle:

#         print("Пешин:",the_line)
#         Peshin = (the_line)
# with open("Аср.txt", "r") as my_new_handle:
#     for the_line in my_new_handle:

#         print("Аср:",the_line)
#         Asr = (the_line)

# with open("Шом.txt", "r") as my_new_handle:
#     for the_line in my_new_handle:

#         print("Шом:",the_line)
#         Shom = (the_line)

# with open("Хуфтон.txt", "r") as my_new_handle:
#     for the_line in my_new_handle:

#         print("Хуфтон:",the_line)
#         Xufton = (the_line)