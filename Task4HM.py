# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)

user_quarter = int(input('Enter number of coordinate plane quarter: '))

if (user_quarter == 1):
    print('| Quarter =', user_quarter, '| X = (0, ∞)', '| Y = (0, ∞)', '|')
elif (user_quarter == 2):
    print('| Quarter =', user_quarter, '| X = (0, - ∞)', '| Y = (0, ∞)', '|')
elif (user_quarter == 3):
    print('| Quarter =', user_quarter, '| X = (0, - ∞)', '| Y = (0, - ∞)', '|')
elif (user_quarter == 4):
    print('| Quarter =', user_quarter, '| X = (0, ∞)', '| Y = (0, - ∞)', '|')
else:
    print('Incorrect data input')
