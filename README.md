from datetime import datetime
try:
    number_cart = input('Введите номер вашей карты: ').strip()
    if number_cart.isdigit() and len(number_cart) == 16:
        print("Номер карты принят")
        date_activate = input('Введите срок действия карты (в формате MM/YYYY): '
        separator = date_activate.split('/')
        if len(separator) == 2:
            month, year = separator
            if month.isdigit() and year.isdigit() and len(month) == 2 and len(year) == 4:
                print(f"Месяц: {month}, Год: {year}")
            else:
                print("Неверный формат срока действия карты.")
        else:
            print("Неверный формат срока действия карты.")
    else:
        print("Неверно введен номер карты.")
        cvv_number = input('Введите Cvv код вашей карты (3 цифры)').strip)()
        if cvv_number.isdigit() and len(cvv_number) == 3:
            print('Ваш Сvv код принят')
except Exception as e:
    print(f"Произошла ошибка: {e}")
    finally
    print('Благодарим за предоставленные данные')

