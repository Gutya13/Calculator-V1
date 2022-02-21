'''Приветствие'''

name = input("Enter your name: ")
print ("Hallo " + name + " !\nThis is a calulator V1 :)")

#Обучение
print ("\n\nActions :\n+\n-\n*\n/\n^\n$\n")
print ("For example: \n5\n+\n5\n=10")

#Основной код: ввод данных
a = input("Number one: ")
symvol = input("Action: ")
if symvol != "+" or "-" or "/" or "^" or "$" or "*":
    while symvol != "+" or "-" or "/" or "^" or "$" or "*":
        if symvol == "+" or "-" or "/" or "^" or "$" or "*":
            break
        print("FAILED!!! Enter again: ")
        symvol = input()
        continue
if symvol == "$":
    b = 0
elif symvol == "+" or "-" or "/" or "^" or "$" or "*":
    b = input("Number two: ")


#Действия
a=int(a)
b=int(b)
result = 0
if symvol == "+":
    result = a+b
elif symvol == "-":
    result = a-b
elif symvol == "*":
    result = a*b
elif symvol == "/":
    result = a/b
elif symvol == "^":
    result = a^b
elif symvol == "$":
    result = sqrt(a)



print ("= " + str(result))






