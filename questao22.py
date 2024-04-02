def main():
  print('Divisão e Resto sem Quociente\n-------------------------')
  num1 = int(input('Digite o 1º Número : '))
  num2 = int(input('Digite o 2º Número : '))
  
  quociente = 0
  resto = num1
  
  while resto >= num2:
      resto -= num2
      quociente += 1
  
  print('Quociente:', quociente)
  print('Resto:', resto)

main()

