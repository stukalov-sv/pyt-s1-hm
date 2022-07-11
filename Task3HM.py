# Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится)

user_point_x = int(input('Enter non-zero point coordinate X: '))
user_point_y = int(input('Enter non-zero point coordinate Y: '))

if (user_point_x > 0 and user_point_y > 0):
    print('| X =', user_point_x, '| Y =', user_point_y, '| ->', 1, '|')
elif (user_point_x > 0 and user_point_y < 0):
    print('| X =', user_point_x, '| Y =', user_point_y, '| ->', 4, '|')
elif (user_point_x < 0 and user_point_y < 0):
    print('| X =', user_point_x, '| Y =', user_point_y, '| ->', 3, '|')
elif (user_point_x < 0 and user_point_y > 0):
    print('| X =', user_point_x, '| Y =', user_point_y, '| ->', 2, '|')
else:
    print('Incorrect data input')
