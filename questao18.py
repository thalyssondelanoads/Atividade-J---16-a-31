def main():
  print('Crescimento Populacional\n--------------------------')
  print('''Cidade A : 3,5% ao Ano
  Cidade B : 1,35% ao Ano''')
  
  populaçao_a = int(input('Digite a População da Cidade A : '))
  populaçao_b = int(input('Digite a População da Cidade B : '))
  
  anos = 0
  while populaçao_a <= populaçao_b:
    anos += 1
    populaçao_a *= (1 + 0.035)
    populaçao_b *= (1 + 0.0135)
  
  print(f'Serão Necessários {anos} Anos para a Cidade A Ultrapassar a População da Cidade B')

main()
