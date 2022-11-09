c = s = 0
r = 'S'
homem = 0
totmulher20 = 0
maiordeidade = 0
from time import sleep
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    c += 1
    sexo =str(input('SEXO [M/F]')).strip().upper()[0]
    cad = str(input('Deseja cadastrar mais alguem? [S/N]')).strip().upper()[0]
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    if idade  >= 18:
        maiordeidade += 1
    if sexo in 'Mm':
        homem += 1
    if cad in 'Nn':
        r = 'N'
        break
print('AGUARDE...')
sleep(2)
print(f' {homem} homens foram cadastrados ')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
print(f'No total são {maiordeidade} maiores de idade!')

