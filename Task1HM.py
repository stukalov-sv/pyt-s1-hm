# Напишите программу, которая принимает на вход цифру,
# обозначающую дни недели, и проверяет, является ли этот день выходным

print("Enter number day of a week: ")
day_nujmber = int(input())
if ((day_nujmber == 6) or (day_nujmber == 7)):
    print("yes, it's holyday")
elif (day_nujmber > 0 and day_nujmber < 6):
    print("no, it's weekday")
else:
    print('Incorrect data input')
