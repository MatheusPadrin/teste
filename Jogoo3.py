from random import randint
pc = randint (0, 10)
tentativas = 1
jogador = int(input('Escolha um número de 0 a 10: '))
print(f'O número que eu pensei foi: {pc}')
while jogador != pc:
    tentativas += 1
    print('Você errou')
    if pc < jogador:
        pc = int(input('Pensei em um número maior. Tente novamente:!'))
    elif pc > jogador:
        pc = int(input('Pensei em um número menor, Tente novamente:!'))
print(f'Parabéns!! VOCÊ ACERTOU EM {tentativas} TENTATIVAS.')