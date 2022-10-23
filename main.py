#from pprint import pprint
import csv
import re


class PhoneBook():

  def __init__(self, file_name):
    self.file_name = file_name
    self.contact_list = self.read()
    self.phone_list = self.find_phone()
    self.create_list = self.create_list()
    self.result_list = self.merge_list()

  def read(self):
    with open(self.file_name, encoding="utf-8") as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)
    return contacts_list

  def find_phone(self):
    phone_list = []
    for contact in self.contact_list:
      contact[5] = re.sub(r'(\+7|8)(\s+)?(\()?(\d{3})(\))?[-\s+]?(\d{3})[-\s+]?(\d{2})[-\s+]?(\d{2})?([^а-яА-яa-zA-Z,\n])?(\()?(доб.)?\s?(\d+)?(\))?', r'+7(\4)\6-\7-\8 \11\12', contact[5])
      phone_list.append(contact)
    return phone_list

  def create_list(self):

    my_list = []
    my_dict = {
      "lastname": '', "firstname": '', 'surname': '', 'organization': '', 'position': '', 'phone': '', 'email': ''
    }

    for contact in self.phone_list:

      if len(contact[1].split()) >= 2:
        my_dict['lastname'] = contact[0]
        my_dict['firstname'] = contact[1].split()[0]
        my_dict['surname'] = contact[1].split()[1]
      elif len(contact[0].split()) == 1:
        my_dict['lastname'] = contact[0]
        my_dict['firstname'] = contact[1]
        my_dict['surname'] = contact[2]
      elif len(contact[0].split()) >= 2:
        my_dict['lastname'] = contact[0].split()[0]
        my_dict['firstname'] = contact[0].split()[1]
        try:
          my_dict['surname'] = contact[0].split()[2]
        except:
          my_dict['surname'] = contact[1]

      my_dict['organization'] = contact[3]
      my_dict['position'] = contact[4]
      my_dict['phone'] = contact[5]
      my_dict['email'] = contact[6]

      my_list.append(list(my_dict.values()))

      my_dict = {
        "lastname": '', "firstname": '', 'surname': '', 'organization': '', 'position': '', 'phone': '', 'email': '',
      }

    return my_list

  def merge_list(self):
    # Честно найдено в интернете. Поиск - одно из самых важных умений (с)
    final_list = self.create_list
    N = len(self.create_list) + 1
    del_index = []
    for i in range(N - 1):
      for search in range(i + 1, N - 1):
        if final_list[i][0] == final_list[search][0] and final_list[i][1] == final_list[search][1]:
          for value in range(7):
            if final_list[i][value] == '':
              final_list[i][value] = final_list[search][value]
          del_index.append(search)
    for i in reversed(del_index):
      del final_list[i]
    return final_list

  def write(self):
    with open("phonebook.csv", "w", encoding="utf-8") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(self.result_list)


file_name = "phonebook_raw.csv"
phone = PhoneBook(file_name)
phone.write()