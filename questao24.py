def main():
  print('Progressão Geométrica\n------------')
  a0 = int(input('Digite o Início da Progressão : '))
  razao = int(input('Digite a Razão Da progressão : '))
  n = int(input('Digite a Quantidade de Termos :  '))

  contador = 0
  print(a0)
  while contador <= n:
    a0 *= razao
    contador += 1 
    print(a0)

main()
