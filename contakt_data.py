'''Задача №49.
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''

contact_data = {
    'first_name': None,
    'second_name': None,
    'phone_number': None
}

def ask_data():
    f_name = input("Введите имя: ")
    s_name = input("Введите фамилию: ")
    phone = input("Введите номер: ")
    contact = {'first_name': f_name,
               'second_name': s_name,
               'phone_number': phone}
    return contact
def add_new_contact(contact):
    with open('phonebook.txt', 'a') as file:
        for value in contact.values():
            file.write(value)
        file.write('\n')
    return True




# add_new_contact(contact)


# print(contact)

def main():
    isStop = 1
    while isStop != 0:
        print(
            f'Выберите, что хотите сделать: \n1 посмотреть\n2 добавить\n3 сохранить\n4 открыть\n5 копировать\n6 выход')
        isStop = int(input('>'))
        if isStop == 2:
            add_new_contact()
main()
