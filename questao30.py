def main():
    print('Descontos da Loja\n------------------')
    print("""Até 10 Unidedades: Preço Total
    11 a 20 Unidades : Desconto de 10%
    21 a 50 Unidades : Desconto de 20%
    Acima de 50 Unidades : Desconto de 25%""")

    nome_produto = ''
    preço_compra = 0
    quantidade_total = 0

    while nome_produto != 'FIM':
        nome_produto = str(input('Digite o Nome do Produto : ')).upper()

        if nome_produto == 'FIM':
            print('FINALIZADO')
        else:
          preço = float(input('Digite o Preço do Produto : '))
          quantidade = int(input('Digite a Quantidade Adquirida : '))
          quantidade_total += quantidade
          quantidade_e_preço = preço * quantidade
          preço_compra += quantidade_e_preço
          print('________')
  
          if quantidade_total <= 10:
              valor_final = preço_compra
              desconto = 0 #0%
          elif quantidade_total <= 20:
              valor_final = preço_compra - (preço_compra * 0.1)
              desconto = 10 #10%
          elif quantidade_total <= 50:
              valor_final = preço_compra - (preço_compra * 0.2)
              desconto = 20 #20%
          else:
              valor_final = preço_compra - (preço_compra * 0.25)
              desconto = 25 #25%

    print(f"""
    Quantidade de Produtos : {quantidade_total}
    Desconto : {desconto}%
    Valor de Compra : R${preço_compra:.2f}
    Valor com Desconto : R${valor_final:.2f}""")

main()
