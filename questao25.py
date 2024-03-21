def porcentagem_canais(numero_canal,canal_2,canal_4,canal_5,canal_7,canal_10):
  total_pessoas = canal_2 + canal_4 + canal_5 + canal_7 + canal_10
  porcentagem_canal_2 = (canal_2/total_pessoas)*100
  porcentagem_canal_4 = (canal_4/total_pessoas)*100
  porcentagem_canal_5 = (canal_5/total_pessoas)*100
  porcentagem_canal_7 = (canal_7/total_pessoas)*100
  porcentagem_canal_10 = (canal_10/total_pessoas)*100

  print(f"""======= RELATÓRIO DE AUDIÊNCIA =======
  Canal 2 : {porcentagem_canal_2:.1f} %
  Canal4 : {porcentagem_canal_4:.1f} %
  Canal 5 : {porcentagem_canal_5:.1f} %
  Canal 7 : {porcentagem_canal_7:.1f} %
  Canal 10 : {porcentagem_canal_10:.1f} %""")

def main():
  print('Pesquisa de Audiência\n---------------------')
  print("""Opcões:
  Canal 2
  Canal 4
  Canal 5
  Canal 7
  Canal 10""")

  numero_canal = 1
  canal_2 = 0
  canal_4 = 0
  canal_5 = 0
  canal_7 = 0
  canal_10 = 0
  while numero_canal != 0:
    numero_canal = int(input('Informe o Número do Canal : '))
    if numero_canal == 0:
      break
    pessoas_assistindo = int(input('Informe a Quantidade de Pessoas Assistindo TV : '))
    
    if numero_canal == 2:
      canal_2 += pessoas_assistindo
    elif numero_canal == 4:
      canal_4 += pessoas_assistindo
    elif numero_canal == 5:
      canal_5 += pessoas_assistindo
    elif numero_canal == 7:
      canal_7 += pessoas_assistindo
    elif numero_canal == 10:
      canal_10 += pessoas_assistindo

  porcentagem_total = porcentagem_canais(numero_canal,canal_2,canal_4,canal_5,canal_7,canal_10)

main()  
