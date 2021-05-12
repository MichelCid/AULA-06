# Exercício Treino 1 - Escreva uma função que recebe dois parâmetros (números) e imprime o
# menor dos dois. Se eles forem iguais, imprima que são valores idênticos.

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 < num2:
  print(f'{num1}')
else:
  if num1 == num2:
    print("Valores idênticos!")
  else:
    print(f'{num2}')