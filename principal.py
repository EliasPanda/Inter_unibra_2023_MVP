"""
------------------------------------------------------------------------------------
------------------------------------------------------------------------------------

PROJETO DO INTERDISCIPLINAR DE 2023.1 DA TURMA DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - ADS2NAB (2022.2)
FACULDADE: UNIBRA (CENTRO UNIVERSITÁRIO BRASILEIRO)
GRUPO DE DESENVOLVIMENTO POO: JONATHAN, HENRIQUE, ELIAS, VICTOR
ORIENTADORA: ALINE FARIAS


>> PARA FUNCIONAMENTO DO CÓDIGO É NECESSÁRIO INSTALAR ALGUNS PACKAGES DO PYTHON

1 - Ter o Python da versão 3.10 ou superior
2 - Instalar na máquina local, (não rodar no replit ou compilador online)

-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------

>> INSTALANDO PACKAGES

1 - pip install tkinter
2 - pip install customtkinter
3 - pip install webbrowser


-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------

>> É doce, mas não é mole não !!!

"""

import webbrowser
import tkinter as tk
from criptoarq import *
from interface import *
import customtkinter

Venda = registroVenda()
Compra = registroCompra()
Usuarios = bancoDeUsuarios()
Estoque = estoqueTotal() 
   
#---------------------------------FUNÇAO JANELA DE TRANSAÇOES-----------------------------------


#---------------------------LAYOUT JANELA DE LOGIN--------------------------------
#LOGIN GERAL
window = customtkinter.CTk(fg_color='#87CEFA') 

largura = 320
altura = 250

largura_tela = window.winfo_screenwidth()
altura_tela = window.winfo_screenheight()
posX = largura_tela / 2 - largura / 2
posY = altura_tela / 2 - altura  / 2
window.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))

#window = tk.Tk()
window.title("Unibra | ADS | Controle de Estoque")
window.geometry("320x250")
window.configure(background='#87CEFA') #BACKGROUND LOGIN
window.resizable(width=False, height=False)

#TEMA
tema = customtkinter.CTkLabel(window, text_color='black', text='ESTOQUE DA FATIMA')
tema.place(x=110,y=12)
#tema = tk.Label(text = "ESTOQUE DA DONA TONHA")
#tema["bg"] = "#87CEFA"

#USUARIO
titulo = tk.Label(text="Usuário:")
titulo.place(x=50, y=50)
titulo["bg"] = "#87CEFA" #MUDANDO A COR DO BOTÃO TÍTULO

entrada1 = customtkinter.CTkEntry(window, fg_color='white', text_color='black')
entrada1.place(x=105, y=46)
#entrada1 = tk.Entry()


#SENHA
senha = tk.Label(text="Senha:")
senha.place(x=50,y=85)
senha["bg"] = "#87CEFA" #MUDANDO A COR DO BOTÃO TÍTULO

entrada2 = customtkinter.CTkEntry(window, fg_color='white', text_color='black', show='*')
#entrada2 = tk.Entry(show='*')
entrada2.place(x=105, y=80)

#RODAPÉ
credito = customtkinter.CTkLabel(window,text_color='black' ,text='"Unibra 2023.1 | ADS2NAB "')
credito.place(x=88,y=200)
#credito = tk.Label(text = "Unibra 2023.1 | ADS2NAB ")
#credito["bg"] = "#FFD700"

#BOTÃO ENTRAR
botao1 = customtkinter.CTkButton(window, fg_color='green' ,text = " » ENTRAR « ", command = lambda: acesso(entrada1,entrada2,aviso,window)).place(x = 18, y=155)

#botao1 = tk.Button(text = " » ENTRAR « ", command = lambda: acesso(entrada1,entrada2,aviso,window))
#botao1.place(x = 90, y=155)
#botao1["bg"] = "green"

#BOTÃO SAIR
botao2 = customtkinter.CTkButton(window,fg_color='red' ,text = " » SAIR « ", command = window.destroy)
botao2.place(x = 160, y=155)

#botao2 = tk.Button(text=" » SAIR « ", command = window.destroy)
#botao2.place(x=190,y=155)
#botao2["bg"] = "#FA8072"




#AVISO SENHA INCORRETA
aviso = tk.Label(text="")
aviso.place(x=85,y=110)
aviso["bg"] = "#87CEFA"

#Y = up/down
#X = left/right

window.mainloop()

