def main():
    print('Concurso de Beleza\n---------------------')

    nome = ''
    candidata_mais_alta = ''
    candidata_mais_baixa = ''
    altura_mais_alta = float('-inf')
    altura_mais_baixa = float('inf')

    candidata_mais_magra = ''
    candidata_mais_gorda = ''
    peso_mais_magra = float('inf')
    peso_mais_gorda = float('-inf')

    while nome != 'FIM':
        nome = input('Digite o Nome da Candidata (ou \'FIM\' para encerrar): ').upper()

        if nome != 'FIM':
            altura = float(input('Digite a Altura da Candidata: '))
            peso = float(input('Digite o Peso da Candidata: '))

            if altura > altura_mais_alta:
                altura_mais_alta = altura
                candidata_mais_alta = nome

            if altura < altura_mais_baixa:
                altura_mais_baixa = altura
                candidata_mais_baixa = nome

            if peso < peso_mais_magra:
                peso_mais_magra = peso
                candidata_mais_magra = nome

            if peso > peso_mais_gorda:
                peso_mais_gorda = peso
                candidata_mais_gorda = nome

    print('=== RESULTADOS ===')
    print(f'Candidata Mais Alta : {candidata_mais_alta}, Altura : {altura_mais_alta}')
    print(f'Candidata Mais Baixa : {candidata_mais_baixa}, Altura : {altura_mais_baixa}')
    print(f'Candidata Mais Magra : {candidata_mais_magra}, Peso : {peso_mais_magra}')
    print(f'Candidata Mais Gorda : {candidata_mais_gorda}, Peso : {peso_mais_gorda}')

main()

