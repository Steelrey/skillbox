num=int(input("Количество контейнеров:"))
cont_list=[]
for i in range(num):
    cont=int(input("Введите вес контейнера: "))
    while cont>200:
        cont=int(input("Слишком тяжелый контейнер - введите другой вес: "))
    cont_list.append(cont)
new_cont=int(input("Введите вес нового контейнера: "))
cont_list.append(new_cont)
cont_list.sort()
number=0
x=0
for i in cont_list:
    number+=1
    if i==new_cont:
        x=number
print("Номер, который получит новый контейнер: ", x)
print(cont_list)
