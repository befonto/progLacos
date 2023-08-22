'''
Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar, mostre-o; não sendo, passe para o próximo passo.
'''

cont = 0

while (cont <= 20):
    a = cont % 2
    if (a == 1):
        print(f"{cont} é um número ímpar.")
    else:
        print(f"{cont} não é um número ímpar.")

    cont = cont + 1