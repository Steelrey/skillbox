# TODO здесь писать код
num=int(input ("Введите число: "))
sum_num=0
num_digits=0
while num>0:
    sum_num+=num%10
    num_digits+=1
    num//3=10
difference=sum_num-num_digits
print("Сумма чисел: ", sum_num)
print("Количество цифр в числе: ",num_digits)
print("Разность суммы и количества цифр: ", difference)

# TODO: код упал:
    num//3=10
    ^^^^^^
