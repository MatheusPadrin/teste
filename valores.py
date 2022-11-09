num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
    cont +=1
print(f'{soma} Aí está a soma dos números. ')


