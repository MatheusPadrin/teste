soma = cont = t = 0
while True:
    tab = int(input('Digite o valor da tabuada que você deseja: '))
    for c in range (1, 11):
        print(f'Aqui está a tabuada de {tab} ---> {tab} x {c} = {tab*c}')
    if c == 10:
          break
