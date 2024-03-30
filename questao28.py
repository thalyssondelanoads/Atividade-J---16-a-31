def main():
  from random import randint
  
  print('Jogo da Adivinhação\n_______')
  n = int(input('Até qual Número deseja Sortear?: '))
  
  p = ''
  tentativas1 = 0
  result = randint(1,n)
  print('Bem Vindo Jogador')
  while not p == result:
      tentativas1 += 1
      p = int(input('Qual seu Palpite: '))
      if p > result:
          print('Menos.. Tente Novamente')
      elif p < result:
          print('Mais.. Tente Novamente')
      else:
          print(f'Vc Acertou!!!\nNúmero de Tentativas: {tentativas1}!')

main()
