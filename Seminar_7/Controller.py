
from asyncore import write
from os import name




print( "Главное Меню") 
print( "1. Показать  контакты из первого списка") 
print( "2. Показать  контакты из второго списка") 
print( "3. Добавление нового контакта")
choice = int(input("Введите свой выбор: ")) 
while choice <0 or choice > 3:
    choice = int(input("Введите свой выбор: "))
  

if choice == 1:
    with open ('phon_file_one.txt', 'r+', encoding='utf-8') as file_phone:
        file=file_phone.read()
        print(file)
if choice == 2:
    with open ('phon_file_second.txt', 'r+', encoding='utf-8') as file_phone_2:
        file=file_phone_2.read()
        print(file)

if choice == 3:
    import main
    



    











# with open ('phon_file_one.txt', 'r', encoding='utf-8') as file_phone:
#     file=file_phone.readable()
#     print(file)
# main.surname_us()
# print(main.surname)
# main.name_us()
# print (main.name)
# main.num_tel()
# print(main.num)


    