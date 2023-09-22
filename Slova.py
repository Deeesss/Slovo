slovo = input("Zadej random slovo: ")
if len(slovo) <= 3:
    print("Kratke slovo")
elif len(slovo) <= 20:
    print("Dlhé slovo!")

else:
    print("Mega dlhe slovo")
