all_cards=int(input("Введите кол-во видеокард всего: "))
old_list=[]
new_list=[]
card=0
for i in range(1,all_cards):
    card=int(input(f"{i} карта: "))
    old_list.append(card)
print(f"Старый список: {old_list}")
x=max(old_list)
for i in old_list:
    if i != x:
        new_list.append(i)
print(f"Старый список: {new_list}")

