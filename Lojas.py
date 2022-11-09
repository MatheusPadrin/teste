#VER OS PREÇOS DOS PRODUTOS MAIS BARATO, TOTAL DAS COMPRAS E COMPRAS ACIMA DE 1000
print(f'{"LOJAS AMIGO DO BACANA":=^40}')
s = c = menor = sp =  0
maisbarato = ''
from time import sleep
while True:
    nome = str(input('Qual nome do produto? '))
    produto = int(input('Preço: R$'))
    adc = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    sp += produto
    c += 1
    if produto >= 1000:
        s +=1
    if c == 1:
        menor = produto
        maisbarato = nome
    else:
        if produto < menor:
            menor = produto
            maisbarato = nome
    if adc in 'Nn':
        print('FECHANDO O PROGRAMA...')
        sleep(2)
        break
print(f'O produto mais barato foi {maisbarato} que custa {menor}')
print(F'Temos {s} produtos acima de 1000')
print(f'O total de sua compra é de R${sp} reais')