r = 'S'
soma = 0
cont = 0
while r == 'S':
    num = float(input('Digite um número pra saber a media, o maior e o menor: '))
    r = str(input('Quer continuar [S/N]? '))
    if cont == 0:
        maior = num
        menor = num
    cont += 1
    soma += num
    media = soma / cont
    if r == 'S':
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'A media dos {cont} números é {media}')
print(f'O Maior número é {maior}')
print(f'O menor número é {menor}')
