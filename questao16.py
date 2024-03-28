def main():
  print('Pagamento de Juros\nJuros de 0.85% ao Dia\n------------------')
  
  valor_emprestimo = float(input('Digite o Valor do Empréstimo : '))
  pagamento_diario = float(input('Digite o Valor do Pagamento Diário : '))
  
  dias = 0
  while valor_emprestimo > 0:
    dias += 1
    valor_emprestimo -= pagamento_diario
    valor_emprestimo *= 1.0085
  print(f'Você Pagará o Empréstimo em {dias} Dias')

main()
