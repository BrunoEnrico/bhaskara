from tkinter import *
from tkinter import messagebox
from math import sqrt

# configurações iniciais da tela
root = Tk()
root.geometry('430x300+500+200')
root.resizable(False, False)

# variáveis que são usadas em todo o código
global a, b, c, btnM

# função para tirar casas decimais de números inteiros
def arredonda(num):

    # defino o numero como float
    num = float(num)

    # se ele for um número redondo (1.0, 2.0) eu tiro a casa decimal e deixo como 1, 2, etc
    if num.is_integer() == True:
        num = int(num)

    # se não for eu arredondo para no máximo 2 casas decimais
    else:
        num = round(num, 2)
    return num

# função que faz o cálculo de bhaskara
def bhaskara():

    # variáveis necessárias
    global txta, txtb, txtc, lD, lX1, lX2, btn, btnM, a, b, c

    # confiro se há algum campo em branco
    if txta.get() == '' or txtb.get() == '' or txtc.get() == '':

        # se houver eu disparo um aviso
        messagebox.showwarning("Atenção!", "Campos em branco!!")

        # e limpo todos os campos
        txta.delete(0, 'end')
        txtb.delete(0, 'end')
        txtc.delete(0, 'end')

        # e coloco o foco na primeira caixa de texto
        txta.focus()

    else:

        # pego o valor de todas as caixas
        a = txta.get()
        b = txtb.get()
        c = txtc.get()

        # o python detecta '-' como texto então caso haja algum numero negativo eu tiro o sinal
        la = list(a)
        if a[0] == '-':
            a = la[1]
        lb = list(b)
        if b[0] == '-':
            b = lb[1]
        lc = list(c)
        if c[0] == '-':
            c = lc[1]

        # checagem se a pessoa digitou alguma letra
        if a.isdigit() == True and b.isdigit() == True and c.isdigit() == True:

            # se algum numero era negativo, eu transformo ele em negativo de novo
            if la[0] == '-':
                a = float(a) * -1
            if lb[0] == '-':
                b = float(b) * -1
            if lc[0] == '-':
                c = float(c) * -1

            # uso a função para arredondar
            a = arredonda(a)
            b = arredonda(b)
            c = arredonda(c)

            # calculo o delta
            delta = pow(b, 2) - (4 * a * c)
            delta = arredonda(delta)

            # se o delta for negativo, finalizo o cálculo e disparo o resultado
            if delta < 0:
                lD['text'] = 'Δ = ' + str(delta)
                lX1['text'] = 'Raiz inexistente!'
                lX1['fg'] = 'Red'

            # se não for
            else:

                # calculo o valor do x1
                x1 = ((b * -1) - sqrt(delta))/(2 * a)

                # uso a função para arredondar o x1
                x1 = arredonda(x1)

                # calculo o valor do x2
                x2 = ((b * -1) + sqrt(delta))/(2 * a)

                # uso a função para arredondar o x2
                x2 = arredonda(x2)

                # se o delta for inteiro eu disparo arredondado
                lD['text'] = 'Δ = ' + str(delta)
                lX1['text'] = 'x1 = ' + str(x1).replace('.', ',')
                lX1['fg'] = 'Black'
                lX2['text'] = 'x2 = ' + str(x2).replace('.', ',')

            # crio o botão "Mostrar Calculo"
            btnM = Button(text='Mostrar Calculo', width = 13, height = 2, command = mostraCalculo)
            btnM.place(x = 320, y = 240)

        # se a pessoa digitar alguma letra
        else:
            # disparo um aviso
            messagebox.showwarning("Atenção!", "Somente numeros!!")

            # e limpo todos os campos
            txta.delete(0, 'end')
            txtb.delete(0, 'end')
            txtc.delete(0, 'end')

            # e coloco o foco na primeira caixa de texto
            txta.focus()

# função para mostrar o calculo na íntegra
def mostraCalculo():

    # variável para controle se o botão foi apertado ou não
    global aux

    # variáveis necessárias
    global btnM, a, b, c

    # se a tela de cálculo estiver fechada
    if aux == 0:

        # maximizo o tamanho da tela
        root.geometry('720x300')

        # mudo a variável para mostrar que ela está aberta
        aux = 1

        # mudo o texto do botão
        btnM["text"] = "Ocultar Calculo"

        # crio uma label para mostrar a formula com os numeros inseridos
        l = Label(font=('Arial', '12'))
        l['text'] = 'Δ = ' + str(b) + '² - 4 . ' + str(a) + ' . ' + str(c)
        l.place(x = 550, y = 20)

        # calculo o delta
        delta = -4 * a * c

        # crio uma label para mostrar a primeira parte do calculo
        l = Label(font=('Arial', '12'))

        # se o resultado do -4 * a * c for negativo, eu separo mais as letras
        if delta > 0:
            l['text'] = 'Δ = ' + str(pow(b,2)) + ' + ' + str(delta)
        else:
            delta = delta * -1
            l['text'] = 'Δ = ' + str(pow(b, 2)) + ' - ' + str(delta)
            delta = delta * -1
        l.place(x = 550, y = 40)

        # crio uma label para mostrar a segunda parte do calculo
        l = Label(font=('Arial', '12'))

        # calculo a segunda parte
        delta = pow(b,2) + delta

        # mostro o valor de delta na label
        l['text'] = 'Δ = ' + str(delta)
        l.place(x = 550, y = 60)

        # crio uma label para o próximo passo
        l = Label(font=('Arial', '12'))

        # se delta for negativo eu já mostro e finalizo o calculo
        if delta < 0:
            l['text'] = 'Raiz inexistente!!'
            l['fg'] = 'Red'
            l.place(x = 550, y = 100)

        # caso não for eu mostro como será o cálculo de x1
        else:

            # se b for negativo eu separo com parênteses
            if b < 0:
                l['text'] = 'x1 = (-(' + str(b) + ') - √' + str(delta) + ') / 2 . ' + str(a)
            else:
                l['text'] = 'x1 = (-' + str(b) + ' - √' + str(delta) + ') / 2 . ' + str(a)
            l.place(x = 550, y = 100)

            # crio outra label para mostrar a próxima linha do cálculo
            l = Label(font=('Arial', '12'))

            # calculo cada parte
            xa = (b * -1)
            xb = sqrt(delta)
            xc = 2 * a

            # arredondo cada valor com a função
            xa = arredonda(xa)
            xb = arredonda(xb)
            xc = arredonda(xc)

            # coloco tudo na label
            l["text"] = 'x1 = ' + str(xa) + ' - ' + str(xb) + ' / ' + str(xc)
            l.place(x = 550, y = 120)

            # instancio mais uma label
            l = Label(font=('Arial', '12'))

            # calculo a parte final da bhaskara em duas variaveis
            xa = ((b * -1) - sqrt(delta))
            xb = 2 * a

            # arredondo os dois valores
            xa = arredonda(xa)
            xb = arredonda(xb)

            # jogo tudo na label novamente
            l['text'] = 'x1 = ' + str(xa) + ' / ' + str(xb)
            l.place(x = 550, y = 140)

            # crio uma label para o resultado de x1
            l = Label(font=('Arial', '12'))

            # faço a divisão dos valores
            x1 = xa / xb

            # arredondo com a função
            x1 = arredonda(x1)

            # coloco o resultado na label
            l['text'] = 'x1 = ' + str(x1)
            l.place(x=550, y=160)

            # crio uma label para o x2
            l = Label(font=('Arial', '12'))

            # se for negativo eu também separo com parênteses
            if b < 0:
                l['text'] = 'x2 = (-(' + str(b) + ') + √' + str(delta) + ') / 2 . ' + str(a)
            else:
                l['text'] = 'x2 = (-' + str(b) + ' + √' + str(delta) + ' )/ 2 . ' + str(a)
            l.place(x = 550, y = 200)

            # crio mais uma label para mostrar o valor do x2
            l = Label(font=('Arial', '12'))

            # calculo os valores
            xa = b * -1
            xb = sqrt(delta)
            xc = 2 * a

            # arredondo com a função
            xa = arredonda(xa)
            xb = arredonda(xb)
            xc = arredonda(xc)

            # jogo os valores na label para mostrar o calculo do x2
            l['text'] = 'x2 = ' + str(xa) + ' + ' + str(xb) + ' / ' + str(xc)
            l.place(x=550, y=220)

            # mais uma label para mostrar o calculo simplificado
            l = Label(font=('Arial', '12'))

            # calculo os valores
            xa = ((b * -1) + sqrt(delta))
            xb = 2 * a

            # arredondo com a função
            xa = arredonda(xa)
            xb = arredonda(xb)

            # e jogo na label
            l['text'] = 'x2 = ' + str(xa) + ' / ' + str(xb)
            l.place(x=550, y=240)

            # crio a ultima label para mostrar o valor final do x2
            l = Label(font=('Arial', '12'))

            # calculo o x2
            x2 = xa / xb

            # arredondo com o x2
            x2 = arredonda(x2)

            # jogo o valor final do x2 na label
            l['text'] = 'x2 = ' + str(x2)
            l.place(x=550, y=260)

    else:

        # caso a tela já esteja aberta, eu fecho
        btnM["text"] = "Mostrar Calculo"
        root.geometry('430x300+500+200')
        aux = 0

# função para limpar todos os valores
def limpar():

    # variáveis necessárias
    global a, b, c, lX1, lX2, lD, btn, aux

    # limpo todas as caixas de texto
    txta.delete(0, 'end')
    txtb.delete(0, 'end')
    txtc.delete(0, 'end')

    # ponho o foco na primeira caixa
    txta.focus()

    # limpo todas as label
    lD['text'] = ''
    lX1['text'] = ''
    lX2['text'] = ''

    # se houver o botão de mostrar cálculo eu tiro
    try:
        btnM.destroy()
    except:
        pass

    # se a tela estiver aberta eu fecho
    if aux == 1:
        root.geometry('430x300+500+200')
        aux = 0

# instancio a variável com valor 0, que é fechado
aux = 0

# crio as label de título e exemplo
l = Label(text='Calculo de Bhaskara', font=('Arial', '12')).pack()
l = Label(text='Exemplo: ax² + bx + c = 0', font=('Arial', '14')).pack()

# as label de fórmula
l = Label(text = 'Fórmulas: ', font=('Arial', '12')).place(x = 20, y = 60)
l = Label(text = 'Δ = b² - 4 . a . c', font=('Arial', '12')).place(x = 100, y = 60)
l = Label(text = 'x = −b ± √Δ / 2.a', font=('Arial', '12')).place(x = 100, y = 80)

# label das text a, b e c
l = Label(text='a:', font=('Arial', '12')).place(x = 28, y = 126)
l = Label(text='b:', font=('Arial', '12')).place(x = 128, y = 126)
l = Label(text='c:', font=('Arial', '12')).place(x = 228, y = 126)

# label Resultado
l = Label(text='Resultado: ', font=('Arial', '12')).place(x = 20, y = 180)

# label Delta
lD = Label(text = '', font=('Arial', '12'))
lD.place(x = 120, y = 180)

# label x1
lX1 = Label(text = '', font=('Arial', '12'))
lX1.place(x = 120, y = 220)

# label x2
lX2 = Label(text = '', font=('Arial', '12'))
lX2.place(x = 120, y = 250)

# textbox A
txta = Entry(width=8)
txta.place(x = 50, y = 130)

# textbox B
txtb = Entry(width=8)
txtb.place(x = 150, y = 130)

# textbox C
txtc = Entry(width=8)
txtc.place(x = 250, y = 130)

# botão calculas
btn = Button(text='Calcular', width = 13, height = 2, command = bhaskara)
btn.place(x = 320, y = 120)

# botão limpar
btnLimpa = Button(text='Limpar', width = 13, height = 2, command = limpar).place(x = 320, y = 180)

root.mainloop()