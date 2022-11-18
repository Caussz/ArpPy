import os 
from time import sleep
import sys
from turtle import *
from draw import func
from colorama import Fore

os.system('cls')
nome = input(Fore.YELLOW + 'Digite seu nome:\n>> ')

def menu():
    print(Fore.GREEN +  f'Ola {nome}!\nVoce esta ultilizando a versão 0.2 do projeto ArpPy.\nPara saber mais e ler os termos de uso, digite "33"')
    opcao = int(input(Fore.BLUE + 'qual dessas opçoes deseja executar?\n\n1 - Espiral\n2 - Personagens\n3 - Aleatorios\n0 - sair\n>> '))
    
    match opcao:
        case 1:
             print(f'Modelos de espiral:\n\n1 - Espiral circular\n2 - Espiral estrela')
             espiral = int(input(f'{nome}, qual modelo de espiral voce deseja executar?\n>> '))
             if espiral == 1:
                func.espiral1()    
             elif espiral == 2:
                  func.espiral2()
             else:
               print('Desculpe, mas essa opção não esta disponivel :/')
        case 2:
            personagem = input('Escolha um dos personagens listados abaixo...\n1- Ironman\n2 - Spiderman\n3 - Robert Downey JR\n4 - Andrew Garfield')
        case 3:
            print('teste')
        case 4:
            print('teste')
        case 0:
            print('teste0')


def clear():
    os.system('cls')

def spin():
    animation = ['[▒▒▒▒▒▒▒▒▒▒]','[█▒▒▒▒▒▒▒▒▒]','[██▒▒▒▒▒▒▒▒]','[███▒▒▒▒▒▒▒]','[████▒▒▒▒▒▒]','[█████▒▒▒▒▒]','[██████▒▒▒▒]','[███████▒▒▒]','[████████▒▒]','[█████████▒]','[██████████]']
    for i in range(len(animation)):
        sleep(0.3)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    clear()

spin()
while True:
    menu()
