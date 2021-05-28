import math
cat1 = float(input('Informe o valor do primeiro cateto: '))
cat2 = float(input('Informe o valor do segundo cateto: '))
hip = math.hypot (cat1, cat2)
print(f'O valor da hipotenusa é {hip:.2f}')
