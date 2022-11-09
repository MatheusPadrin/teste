import random
pc = random.randint(0,10)
resp = 'Par' or 'Ímpar'
cont = 0
total = 0
r = ''
while True:
        num = int(input('Digite um valor: '))
        cont=cont+1
        total = pc + num
        pc = random.randint(0, 10)
        par = str(input('Par ou ímpar [P/I]? '))
        if r not in 'PI':
            print(f'\033[31m\nDigite Impar ou Par. [P/I]\n\033[0;0m')
        else:
            print(f'Você escolheu: \033[35m{num}\033[0;0m\nComputador escolheu: \033[35m{pc}\033[0;0m\n\nTotal: \033[32m{total}\033[0;0m')
        if par == 'I':
            if total %2 >= 1:
                print('Você ganhou (ÍMPA),Vamos novamente....')
            else:
                print('Você perdeu (IMPÁ)')
                break
        elif par == 'P':
            if total %2==0:
                print(f'Você ganhou ')
            else:
                print('\033[31mVocê Perdeu.\033[0;0m')
                break
print(f'Você teve \033[32m{cont-1}\033[0;0m vitorias.')

