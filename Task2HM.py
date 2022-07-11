# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предика

for X in True, False:
    for Y in True, False:
        for Z in True, False:
            first_equation = not(X or Y or Z)
            second_equation = not X and not Y and not Z
            print('| X =', X, '| Y =', Y, '| Z =', Z, '|', first_equation == second_equation)
