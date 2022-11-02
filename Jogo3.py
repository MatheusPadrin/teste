from random import randint
pc = randint(0, 10)
tentativas = 1
jogador = int(input('Dê o seu palpite: '))
print(f'Pensei no número {pc}')
while jogador != pc:
  tentativas += 1
  print('Você errou! ')
  if jogador < pc:
    jogador = int(input('Pensei em um numero maior. Tente de novo: '))
  elif jogador > pc:
    jogador = int(input('Pensei em um numero menor. Tente novamente: '))
print(f'Parabéns, você acertou em {tentativas} tentativas!')