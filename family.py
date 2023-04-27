# # Список
family_1 =["Dasha", "Jenea", "Danila", "Dana", "Anton"]
print(family_1)

# # множества
family_2 = {"Dasha", "Jenea", "Danila", "Dana", "Dasha", "Anton"}
print(family_2)

# Словарь ключ:значение
family_3 = {"Wife":"Dasha" , "Brother1":"Danila", "Brother2":"Anton", "Me":"Jenea", "Sister":"Dana", }
# print(family_3["wife"])
for k, v in family_3.items():
    print(k + " - " + v)
