
def name_us():
    print('Фамилия: '+surname)
    print ('Имя: '+name )
    print('Номер телефона: '+num)

surname = input('Введите Фамилию: ')
name = input('Введите Имя: ')
num = (input('Введите номер телефона: '))

book_phon = ('\n'+'Фамилия: ' + surname +','+ ' Имя: ' + name+',' + ' телефон- ' + num + '\n')
with open ('phon_file_one.txt', 'a', encoding='utf-8') as file_phone:
    file_phone.write(book_phon)


book_phon_1 = ('\n'+'Фамилия: ' + surname +'\n'+ 'Имя: ' + name+'\n' + 'телефон- ' + num + '\n')
with open ('phon_file_second.txt', 'a', encoding='utf-8') as file_phone_2:
    file_phone_2.write(book_phon_1)