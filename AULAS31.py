import random
e= 0
x= 30*'='
while True:
    a=random.randint(0,10)
    b=int(input('Digite um numero: '))
    c= b+a
    d= ''
    e=e+1
    d= str(input('Impar ou Par? [P/I]')).strip().upper()[0]
    if d not in 'PI':
        print(f'\033[31m{x}\nDigite Impar ou Par. [P/I]\n{x}\033[0;0m')
    else:
        print(f'Você escolheu: \033[35m{b}\033[0;0m\nComputador escolheu: \033[35m{a}\033[0;0m\n{x}\nTotal: \033[32m{c}\033[0;0m\n{x}')
    if d=='I':   # ÍMPAR
        if c%2>=1:
            print(f'\033[36mVocê Ganhou! (Impar)\033[0;0m\n{x}')
        else:
            print('\033[31mVocê Perdeu.\033[0;0m')
            break
    elif d=='P': # PAR
        if c%2==0:
            print(f'\033[36mVocê Ganhou! (Par)\033[0;0m\n{x}')
        else:
            print('\033[31mVocê Perdeu.\033[0;0m')
            break
print(f'Você teve \033[32m{e-1}\033[0;0m vitorias.')