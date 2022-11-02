from time import sleep
n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
print('Escolha uma das opções abaixo:')
print('[1] Somar os números \n[2] multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair')
choice =int(input('Qual opção você deseja? '))
while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
    choice =int(input('Opção inválida, as opções são de 1 a 5! '))
while choice == 4:
    n1 = float(input('Digite o 1º valor: '))
    n2 = float(input('Digite o 2º valor: '))
if choice == 1:
    print(f'A soma dos números são {n1+n2}')
elif choice == 2:
    print(f'Os valores {n1} x {n2} multiplicados são {n1*n2} ')
elif choice == 3:
 if n1 > n2:
     print(f'{n1} é o número maior')
 if n2 > n1:
     print(f'{n2} é o número maior')
if choice == 5:
    print('SAINDO...')
    sleep(2)
    print('Você saiu!')
