from datetime import datetime, timedelta,date
try:
        date_birthday = datetime(year=2024,month=7,day=31)
        now_date = datetime.now()
        days_delta=(date_birthday-now_date).days
        if days_delta>0:
            print(f'До вечеринки гари осталось {days_delta} дней')
        else:
            print(f'У Гари сегодня день рождения')
except ValueError as e:
    print(f'Некоректный ввод даты рождения Гари {days_delta}')
finally:
    print(f'Завершениe даты рождения Гари')



