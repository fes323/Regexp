from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

pattern_email = r'[A-Za-z]*?\d*?\@?[A-Za-z]*(.ru|.com)'

my_dict = {}
my_list = []

for row in contacts_list:

  fullname = ' '.join(row[0:3]).split() #ФИО
  organization = ''.join(row[3]) #организция
  position = ''.join(row[4]) #Должность
  phone = ''.join(row[5]) #Телефон
  email = ''.join(row[6]) #Почта

  if len(fullname) == 3: #Проверка наличия отчества (если есть, то добавляем)
    lastname = fullname[0]
    firstname = fullname[1]
    surname = fullname[2]
  if len(fullname) == 2: #Проверка наличия отчества (при отсутсвии отчества не добавляем)
    lastname = fullname[0]
    firstname = fullname[1]
  else:
    pass

  if lastname and firstname not in my_dict.values(): #Проверка на дубликаты по совпадению ФАМИЛИЯ-ИМЯ
    my_dict = ({
      'lastname': lastname,
      'firstname': firstname,
      'surname': surname,
      'organization': organization,
      'position': position,
      'phone': phone,
      'email': email,
    })
    my_list.append(my_dict.values()) #Добавляем в список значения словаря т.к. словарь не записывается нормально в phonebook.csv
  else:
    pass

pattern_phone = r'(\+7|8)\s*\(?\d+\)?([-\s]*\d+)*\s?\(?\w*\s?\.?\s?\d+\)?'

phone_list = []
for iteration in contacts_list:
  pattern_phone = re.findall(r'(\+7|8)\s*\(?\d+\)?([-\s]*\d+)*\s?\(?\w*\s?\.?\s?\d+\)?', (iteration[5]))
  pprint(pattern_phone)

pprint(phone_list)

#pprint(my_list)


with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(my_list)