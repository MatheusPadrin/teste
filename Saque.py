print(f'{"BANCO CÂMARA":=^40}')
saque = int(input('Qual o valor que você deseja sacar? R$'))
céd = 50
totcéd = 0
total = saque
while True:
        if total >= céd:
                total -=céd
                totcéd+=1
        else:
                print(f'Total de {totcéd} cédulas de {céd}')
                if céd == 50:
                        céd=20
                elif céd == 20:
                        céd=10
                elif céd == 10:
                        céd = 1
                        totcéd=0
                if total == 0:
                        break