#Criar um programa que desafia o usuário a adivinhar um número gerado aletoriamente pelo computador.
#O programa deve gerar um número de 1 a 100.
#O usuário terá um número limitado de tentativas para adivinhar o número. (por exemplo, 10 tentativas).
# A cada tentativa, o progrma deve informar se o número escolhido pelo usuário é maior ou menor que o número gerado.
#Quando o usuário acerta o número ou esgota as tentativas, o programa termina e exibe uma mensagem.

import random

palpite =""
num =""

def gerar():
    num=random.randint(0,100)
    
def chute():
    palpite = float(input("Digite seu palpite: "))
    
gerar()
chute()

for i in range(1,5): 
    chute()
    if num == palpite:
        print("Você acertou!")
    else:
        print("Digite outro numero!")
    

    