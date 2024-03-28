def main():
    print('Análise de Dados\n---------------------')
    print("""Sexo:

    Masculino [ 1 ] 
    Feminino [ 2 ]

Estado Civil:

    Casado [ 1 ]
    Solteiro [ 2 ]
    Divorciado [ 3 ]
    Viúvo [ 4 ]""")

    contador_pessoas = 0
    soma_idade_mulheres = 0
    soma_idade_homens = 0
    quantidade_homens_solteiros = 0
    quantidade_mulheres_solteiras = 0
    quantidade_mulheres_divorciadas_acima_de_30 = 0
    quantidade_homens = 0
    quantidade_mulheres = 0

    while contador_pessoas < 100:
        contador_pessoas += 1
        sexo = int(input('Digite seu Sexo ( 1 ou 2) : '))

        while sexo != 1 and sexo != 2:
            sexo = int(input('INVÁLIDO, Digite seu Sexo ( 1 ou 2) : '))

        idade = int(input('Digite sua Idade : '))
        estado_civil = int(input('Digite seu Estado Civil (1, 2, 3 ou 4) : '))

        while estado_civil != 1 and estado_civil != 2 and estado_civil != 3 and estado_civil != 4:
            estado_civil = int(input('INVÁLIDO, Digite seu Estado Civil (1, 2, 3 ou 4) : '))
        print('________')

        if sexo == 2:
            soma_idade_mulheres += idade
            quantidade_mulheres += 1
        if sexo == 1:
            soma_idade_homens += idade
            quantidade_homens += 1
        if sexo == 1 and estado_civil == 2:
            quantidade_homens_solteiros += 1
        if sexo == 2 and estado_civil == 2:
            quantidade_mulheres_solteiras += 1
        if sexo == 2 and idade > 30:
            quantidade_mulheres_divorciadas_acima_de_30 += 1

    media_idade_homens = soma_idade_homens / quantidade_homens
    media_idade_mulheres = soma_idade_mulheres / quantidade_mulheres
    percentual_homens_solteiros = (quantidade_homens_solteiros / quantidade_homens)*100
    percentual_mulheres_solteiras = (quantidade_mulheres_solteiras / quantidade_mulheres)*100

    print(f"""      ====== RELATÓRIO ======

    Méda de Idade dos Homens : {media_idade_homens:.1f}
    Média de Idade das Mulheres : {media_idade_mulheres:.1f}
    Percentual Homens Solteiros : {percentual_homens_solteiros:.1f}%
    Percentual Mulheres Solteiras : {percentual_mulheres_solteiras:.1f}%
    Quantidade Mulheres Divorciadas com mais de 30 Anos : {quantidade_mulheres_divorciadas_acima_de_30}""")

main()
