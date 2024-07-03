from tkinter import *
from tkinter import ttk

co0 = '#ffffff' # branco
co1 = '#8b0000' # DarkRed
co2 = '#1c1c1c' # grey11
co3 = '#cc0099' # rosa
co4 = '#00008b' # DarkBlue
co5 = '#9999ff' # roxo claro
co6 = '#0000ff' # azul
root=Tk()
root.geometry("295x230")
root.title("calculadora IMC")
root.config(bg=co0)

# ------------------------- TELA PARTE 1------------------------------------
Frame_cima = Frame(root, width=295, height=59, bg=co5, pady= 0, padx=0, relief='flat')
Frame_cima.grid(row=0 , column=0 , sticky=NSEW)

# -------------------------- TELA PARTE 2 -----------------------------------

Frame_baixo = Frame(root, width=295, height=180, bg=co5, pady= 0, padx=0, relief='flat')
Frame_baixo.grid(row=1 , column=0 , sticky=NSEW)

# -------------------------- CONF FRAME CIMA  -----------------------------------

app_nome = Label(Frame_cima, text='calculadora IMC', width=23, height=1 , padx=0, relief='flat', anchor='center', font=('ivy 16 bold'), bg=co0, fg=co2)
app_nome.place(x=0, y=0)

app_linha = Label(Frame_cima, width=400, height=1 , padx=0, relief='flat', anchor='center', font=('ivy 1'), bg=co6, fg=co6)
app_linha.place(x=0, y=35)

#------------------------------funcao calculos -------------------------

def calcular():
    
    peso = float(e_peso.get())
    altura = float(e_altura.get())
    
    imc = peso / (altura ** 2)
   
    
    l_resultado['text'] = "({:.{}f})".format(imc, 1)
    
    if imc < 16:
     l_resultado_texto['text'] ='voce esta muito a baixo do peso normal!'
   
    elif imc < 18.5:
     l_resultado_texto['text'] ='voce esta a baixo do peso normal!'
   
    elif 18.6 <= imc < 24.9:
     l_resultado_texto['text'] ='voce esta com o peso normal!'
   
    elif 25 <= imc < 29.9:
     l_resultado_texto['text'] ='voce esta a cima do peso normal grau I leve!'
   
    elif 30.0 <= imc < 34.9:
     l_resultado_texto['text'] ='voce esta obeso grau II severa !'
   
    elif imc >= 40:
     l_resultado_texto['text'] ='voce esta com obesidade grau III morbida!'


     


# -------------------------- CONF FRAME baixo  -----------------------------------


l_peso = Label(Frame_baixo, text='Digite o seu peso', height=1 , padx=0, relief='flat', anchor='center', font=('ivy 10 bold'), bg=co0, fg=co2)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(Frame_baixo, width=5, relief='solid', font=('ivy 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)


l_altura = Label(Frame_baixo, text='Digite a sua altura', height=1 , padx=0, relief='flat', anchor='center', font=('ivy 10 bold'), bg=co0, fg=co2)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_altura = Entry(Frame_baixo, width=5, relief='solid', font=('ivy 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)


l_resultado = Label(Frame_baixo, text='----', width=5, height=1 , padx=6,pady=12, relief='groove', anchor='center', font=('ivy 20 bold'), bg=co4, fg=co0)
l_resultado.place(x=180, y=10)


l_resultado_texto = Label(Frame_baixo, text='', width=37, height=1 , padx=0,pady=12, relief='flat', anchor='center', font=('ivy 10 bold'), bg=co0, fg=co1)
l_resultado_texto.place(x=0, y=75)


b_calcular = Button(Frame_baixo, command=calcular, text='calcular',width=34, height=1,overrelief=SOLID, relief='raised', anchor='center', font=('ivy 10 bold'), bg=co4, fg=co0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=55, padx=5, columnspan=30)




root.mainloop()