n = s = c = 0
while True:
    n = float(input('Digite um valor [999 interrompe o programa]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores é de {s} ')