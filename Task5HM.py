# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве

first_pnt_x = int(input('Enter first point coordinate X: '))
first_pnt_y = int(input('Enter first point coordinate Y: '))

sec_pnt_x = int(input('Enter second point coordinate X: '))
sec_pnt_y = int(input('Enter second point coordinate Y: '))

result = float(((pow(first_pnt_x - sec_pnt_x, 2) + pow(first_pnt_y - sec_pnt_y, 2)) ** 0.5))
result = int(result * 100) / 100
print('A (', first_pnt_x, ',', first_pnt_y, ');', 'B (', sec_pnt_x, ',', sec_pnt_y, ')', '->', result)
