# TODO здесь писать код
years = int(input("Введите первый год: "))
years_2 = int(input("введите второй год: "))
print("Года от,", years, "до", years_2, "тремя одинаковыми цифрами")
for i in range(years,years_2, 1):
    a,b,c,d = i // 1000, i // 100 % 10, i // 10 % 10, i % 10
    if a == b == c or b == c == d or c == d == a or a == b == d:
        print(a * 1000 + b * 100 + c * 10 + d)