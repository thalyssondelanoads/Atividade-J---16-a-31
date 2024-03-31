def main():
  print('Frigorífico\n---------------------')

  identificacao_boi = -1
  boi_mais_magro = boi_mais_gordo = 0
  peso_mais_magro = float('inf')
  peso_mais_gordo = float('-inf')

  while identificacao_boi != 0:
      identificacao_boi = int(input('Digite o número de identificação do boi (0 para encerrar): '))

      if identificacao_boi != 0:
          peso_boi = float(input('Digite o peso do boi: '))

          if peso_boi < peso_mais_magro:
              peso_mais_magro = peso_boi
              boi_mais_magro = identificacao_boi

          if peso_boi > peso_mais_gordo:
              peso_mais_gordo = peso_boi
              boi_mais_gordo = identificacao_boi

  if boi_mais_magro != 0:
      print('Boi mais magro - Número de Identificação:', boi_mais_magro, ',Peso:', peso_mais_magro)
  if boi_mais_gordo != 0:
      print('Boi mais gordo - Número de Identificação:', boi_mais_gordo, ',Peso:', peso_mais_gordo)

main()

