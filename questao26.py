def main():
  print('Opinião sobre um Filme\n----------------------')
  print("""Avaliações:
  Ótimo [ 1 ]
  Bom [ 2 ]
  Regular [ 3 ]
  Péssimo [ 4 ]""")

  idade = 0
  soma_idades_otimo = 0
  soma_opçao_regular = 0
  soma_bom = 0
  qtd_pessoas = 0
  qtd_pessoas_geral = 0
  while idade != -1:
    idade = int(input('Digite sua Idade : '))
    if idade == -1:
      print('Programa Finalizado')
    else:
      opiniao = int(input('Digite o Código da sua Avaliação : '))
      if opiniao == 1:
        soma_idades_otimo += idade
        qtd_pessoas += 1
      if opiniao == 3:
        soma_opçao_regular += 1
      if opiniao  == 2:
        soma_bom += 1
      qtd_pessoas_geral += 1
  
    media_idades_otimo = soma_idades_otimo / qtd_pessoas
  
  print(f"""====== RELATÓRIO FINAL ======
    Média de Idade das Pessoas que Responderam Ótimo : {media_idades_otimo}
    Quantidade de Pesoas que Responderam Regular : {soma_opçao_regular}
    Porcentagem de Pessoas que Responderam Bom : {soma_bom / qtd_pessoas_geral * 100:.1f} %""")
  
main()
