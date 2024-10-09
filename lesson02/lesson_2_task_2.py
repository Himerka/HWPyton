def is_year_leap(year):
  if year % 4 == 0:
    return True
  else:
    return False

year = int(input("Введите год: "))
is_leap = is_year_leap(year)
print(f"год {year}: {is_leap}")