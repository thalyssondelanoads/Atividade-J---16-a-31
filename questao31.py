def obter_digito(numero, posicao):
    return numero // 10**posicao % 10

def decimal_para_romano(digito, unidade, cinco, dez):
    if digito == 0:
        return ''
    elif digito <= 3:
        return unidade * digito
    elif digito == 4:
        return unidade + cinco
    elif digito == 5:
        return cinco
    elif digito <= 8:
        return cinco + (unidade * (digito - 5))
    else:
        return unidade + dez

def main():
    print('Numeração Romana\n---------------------')
    numero_decimal = int(input('Digite um Número Decimal Até 3 Dígitos: '))

    dezena = obter_digito(numero_decimal, 1)
    unidade = obter_digito(numero_decimal, 0)

    numero_romano = decimal_para_romano(dezena, 'X', 'L', 'C') + \
                    decimal_para_romano(unidade, 'I', 'V', 'X')

    print('Número Decimal em Numeração Romana:', numero_romano)

main()

