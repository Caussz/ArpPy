from turtle import *

def questions():
    global bg 
    bg = input("Qual cor voce deseja de fundo?\n>> ")
    global nmr 
    nmr = int(input("Quantas rotaçoes? (recomendado minimo 120)\n>> "))
    global cor1 
    cor1 = input("Qual cor voce deseja para o primeiro circulo?\n>> ")
    global cor2 
    cor2 = input("Qual cor voce deseja para o segundo circulo?\n>> ")
    global cor3 
    cor3= input("Qual cor voce deseja para o terceiro circulo?\n>> ")
    if bg == cor1:
        print('a cor de fundo não pode ser igual a cor do primeiro circulo...')
        escolha = int(input('Qual deles voce deseja alterar a cor?\n1 - Cor de fundo\n2 - cor do primeiro circulo\n>> '))
        if escolha == 1: 
            bg = input("Qual cor voce deseja de fundo?\n>> ")
        elif escolha == 2:
            cor1 = input("Qual cor voce deseja para o primeiro circulo?\n>> ")
        else:
            print('Opção invalida.')
    elif bg == cor2:
        print('a cor de fundo não pode ser igual a cor do primeiro circulo...')
        escolha = int(input('Qual deles voce deseja alterar a cor?\n1 - Cor de fundo\n2 - cor do segundo circulo\n>> '))
        if escolha == 1: 
            bg = input("Qual cor voce deseja de fundo?\n>> ")
        elif escolha == 2:
            cor2 = input("Qual cor voce deseja para o primeiro circulo?\n>> ")
        else:
            print('Opção invalida.')
    elif bg == cor3:
        print('a cor de fundo não pode ser igual a cor do primeiro circulo...')
        escolha = int(input('Qual deles voce deseja alterar a cor?\n1 - Cor de fundo\n2 - cor do terceiro circulo\n>> '))
        if escolha == 1: 
            bg = input("Qual cor voce deseja de fundo?\n>> ")
        elif escolha == 2:
            cor3 = input("Qual cor voce deseja para o primeiro circulo?\n>> ")
        else:
            print('Opção invalida.')


def questions2():
    bg = input("Qual cor voce deseja de fundo?\n>> ")
    global pen
    pen = input("Qual a cor das retas?")
    nmr = int(input("Quantas rotaçoes? (recomendado minimo 400)\n>> "))
    if pen == bg:
        escolha = input("A cor das retas devem ser diferents da cor de fundo...\nQual voce deseja alterar?\n1 - Cor de fundo\n2 - Cor das retas")
        if escolha == 1: 
            bg = input("Qual cor voce deseja de fundo?\n>> ")
        elif escolha == 2:
            pen = input("Qual cor voce deseja para as retas?\n>> ")
        else:
            print('Opção invalida.')



def espiral1():
   questions()
   bgcolor(bg)
   speed(0)
   hideturtle()
   for i in range(nmr):
       color(cor1)
       circle(i)
       color(cor2)
       circle(i*0.8)
       color(cor3)
       circle(i*0.5)
       right(3)
       forward(3)
   done()

def espiral2():
    questions2()
    bgcolor(bg)
    Turtle()
    speed(20)
    pencolor(pen)
    for i in range(nmr):
       forward(i)
       left(91)

