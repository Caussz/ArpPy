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

def ironman():
    piece1=[[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],[(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]]
    piece2=[[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210)],[(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]]
    piece3=[[(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],[(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240), (60, -220), (0, -220)]]
    hideturtle()
    bgcolor('red')
    setup(500,600)
    title("Ironman")
    piece1Goto=(0,120)
    piece2Goto=(0,-30)
    piece3Goto=(0,-220)
    speed(2)
    def draw_piece(piece,pieceGoto):
        penup()
        goto(pieceGoto)
        pendown()
        color('yellow')
        begin_fill()
        for i in range(len(piece[0])):
            x,y=piece[0][i]
            goto(x,y)

        for i in range(len(piece[1])): 
            x,y=piece[1][i]
            goto(x,y)
        end_fill()
draw_piece(piece1,piece1Goto)
draw_piece(piece2,piece2Goto)
draw_piece(piece3,piece3Goto)
