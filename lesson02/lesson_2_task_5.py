def month_to_season(month):
    if 3 <= month <= 5:
        return 'Весна'
    elif 6 <= month <= 8:
        return 'Лето'
    elif 9 <= month <= 11:
        return 'Осень'
    elif month == 12 or 1 <= month <= 2: # Два условия для зимы
        return 'Зима'
    else:
        return 'Некорректный месяц'

month = 4 # Тест для января
season = month_to_season(month)
print(f'Месяц {month} соответствует сезону {season}')