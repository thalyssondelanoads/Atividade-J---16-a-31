def main():
  print('Investimento Bancário\n--------------------')
  continuar = 'S'
  
  while continuar.upper() == 'S':
      saldo_inicial = 0
      investimento_mensal = float(input('Informe o Valor a ser Investido por Mês: '))
      taxa_juros_mensal = float(input('Informe a Taxa de Juros Mensal (em %): '))
  
      saldo = saldo_inicial
      meses = 0
      while meses < 12:
          saldo += investimento_mensal
          saldo *= 1 + (taxa_juros_mensal / 100)
          meses += 1
  
      print('Saldo do Investimento após 1 ano:', round(saldo, 2))
  
      continuar = input('Deseja Processar Mais um Ano (S/N)? ')
      if continuar.upper() == 'N':
        print('Programa Finalizado')

main()
