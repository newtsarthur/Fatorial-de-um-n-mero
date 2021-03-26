#fatorial de um número com python
from time import sleep 
print("\n")
number = int(input("Digite o valor do número que você deseja achar o fatorial: "))
i = number
d = 1
print(f'{number}! = ', end=' ')
while i > 0:
    print(i, end=' ')
    print('x' if i > 1 else '=', end=' ')
    d *= i
    i -= 1
sleep(1)
print(d)
sleep(1)
print(f'O fatorial de {number} é: {d}')
print("\n")