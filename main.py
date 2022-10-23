from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

my_dict = {}
my_list = []
new_dict = {}
new_list = []

for row in contacts_list:

    fullname = ' '.join(row[0:3]).split()  # ФИО
    organization = ''.join(row[3])  # организция
    position = ''.join(row[4])  # Должность
    phone = re.sub(
        r'(\+7|8)(\s+)?(\()?(\d{3})(\))?[-\s+]?(\d{3})[-\s+]?(\d{2})[-\s+]?(\d{2})?([^а-яА-яa-zA-Z,\n])?(\()?(доб.)?\s?(\d+)?(\))?',
        r'+7(\4)\6-\7-\8 \11\12', row[5])
    email = ''.join(row[6])  # Почта

    if len(fullname) == 3:  # Проверка наличия отчества (если есть, то добавляем)
        lastname = fullname[0]
        firstname = fullname[1]
        surname = fullname[2]
    if len(fullname) == 2:  # Проверка наличия отчества (при отсутсвии отчества не добавляем)
        lastname = fullname[0]
        firstname = fullname[1]
    if len(fullname) == 1:
        lastname = fullname[0]
    else:
        pass

    if lastname not in my_dict.values():  # Проверка на дубликаты по совпадению
        my_dict = ({
            'lastname': lastname,
            'firstname': firstname,
            'surname': surname,
            'organization': organization,
            'position': position,
            'phone': phone,
            'email': email,
        })

        my_list.append(
            my_dict.values()
        )
    else:
        pass


with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(my_list)