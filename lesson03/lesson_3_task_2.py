from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14", "+79001234567"),
    Smartphone("Samsung", "Galaxy S21", "+79001234568"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79001234569"),
    Smartphone("Google", "Pixel 6", "+79001234570"),
    Smartphone("OnePlus", "9 Pro", "+79001234571"),
]

for smartphone in catalog:
    print(smartphone)