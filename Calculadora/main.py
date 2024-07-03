# FRONT-END

# ETAPA 1: Crie e importar as bibliotecas necessárias para dentro do script criado.
# Importando tkinter

from tkinter import *
from tkinter import ttk

# Cores:

cor1 = "#1e1f1e" #Black
cor2 = "#feffff" #White
cor3 = "#38576b" #Blue carregando
cor4 = "#ECEFF1" #Cinzenta
cor5 = "#FFAB40" #Orange

#ETAPA 2: Crie uma janela e faz configurações básicas da janela.
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)


# Criação de Frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)


# Variável todos os valores
todos_valores = ''

#Criando Label
valor_texto = ''

# BACK-END

#Criando Função
def entrar_valores(event): 
    
    global todos_valores
    todos_valores = todos_valores + str(event)

    # Passando o valor para a tela
    valor_texto.set(todos_valores)

    # Passando valores para tela:
    valor_texto.set(todos_valores)


# Função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))


def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")



# Criando Label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font='Ivy 18', bg=cor2)
app_label.place(x=0, y=0)



#ETAPA 3: Divida a janela em dois quadros e faça algumas configurações neles.
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


# ETAPA4: Criando Botões

b_one = Button(frame_corpo, command= limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_one.place(x=0, y=0)

b_two = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_two.place(x=118, y=0)

b_three = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_three.place(x=177, y=0)

b_four = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_four.place(x=0, y=52)

b_five = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_five.place(x=59, y=52)

b_six = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_six.place(x=118, y=52)

b_seven = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_seven.place(x=177, y=52)





b_heigh = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_heigh.place(x=0, y=104)

b_nine = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_nine.place(x=59, y=104)

b_ten = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_ten.place(x=118, y=104)

b_eleven= Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_eleven.place(x=177, y=104)

#____
b_twelve = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_twelve.place(x=0, y=156)

b_thirteen = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_thirteen.place(x=59, y=156)

b_fourteen = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_fourteen.place(x=118, y=156)

b_fiveteen = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_fiveteen.place(x=177, y=156)



b_sixteen = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_sixteen.place(x=0, y=208)

b_seventeen = Button(frame_corpo, command=lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_seventeen.place(x=118, y=208)

b_heighteen = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_heighteen.place(x=177, y=208)


janela.mainloop()