def main():
  print('Multiplicação sem Operador\n-----------------')
  print('Escreva os 2 Números que Deseja Multiplicar')
  n1 = int(input('Primeiro Número: '))
  n2 = int(input('Segundo Número: '))

  contador = 0
  resultado = 0
  while contador < n2:
    contador += 1
    resultado += n1
  print(f'O Resultado é {resultado}')

main()
