print('Viagem de Carro\n---------------------')

distancia_total = 600 
combustivel_inicial = 50 
distancia_percorrida = 0
consumo_total = 0

while distancia_percorrida < distancia_total and consumo_total < combustivel_inicial:
    distancia_medicao = int(input('Distância Percorrida Desde a Última Medição (Km): '))
    consumo_medicao = int(input('Quantidade de Litros Consumidos para Percorrer a Distância Indicada: '))

    distancia_percorrida += distancia_medicao
    consumo_total += consumo_medicao

if distancia_percorrida >= distancia_total:
    print('O Carro Chegou ao seu Destino.')
elif consumo_total == combustivel_inicial:
    print('O Carro Parou Antes de Chegar por Falta de Combustível.')
else:
    print('O Carro não Chegou ao Destino e ainda Possui Combustível.')

if consumo_total > 0:
    consumo_por_litro = distancia_percorrida / consumo_total
    print(f'O Consumo do Carro foi de {consumo_por_litro:.2f} Km/l.')
else:
    print('Não foi possível calcular o consumo pois não houve consumo de combustível.')
