films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
number=int(input("Сколько фильмов хотите добавить? "))
like_list=[]
for i in range(number):
    new_film = input("Введите название фильма: ")
    if new_film in films:
        print("Фильм добавлен в Избранное")
    while new_film not in films:
        new_film = input(f"Ошибка: фильма {new_film} у нас нет :( \nВыберете другой фильм: ")

    like_list.append(new_film)
print(like_list)

