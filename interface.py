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

import tkinter as tk
from tkinter import ttk
import webbrowser
import customtkinter

dicVenda = {}
dicCompra = {}
dicUsuario = {}
listaVenda = []
listaCompra = []
dicEstoque = {}



def registroVenda():
    return dicVenda


def registroCompra():
    return dicCompra


def bancoDeUsuarios():
    return dicUsuario


def estoqueTotal():
    return dicEstoque


def criaJanelaTransacao():




    # ----------------------FUNCIONAMENTO DA JANELA TRANSAÇAO-----------------------------
    # VENDAS
    def registraTransacaoVenda():
        chaveVenda = produtoEntrada.get()
        quantidadeVenda = quantidadeEntrada.get()
        precoVenda = precoEntrada.get()
        tuplaVenda = (quantidadeVenda, precoVenda)
        if chaveVenda in dicVenda and chaveVenda in dicEstoque:
            listaVenda = dicVenda[chaveVenda]
            listaVenda.append(tuplaVenda)
            # ---------------------->>> ESCREVER NO ARQUIVO
            dicVenda[chaveVenda] = listaVenda
        else:
            if chaveVenda in dicEstoque:
                listaVenda = []
                listaVenda.append(tuplaVenda)
                dicVenda[chaveVenda] = listaVenda
        if chaveVenda in dicEstoque:
            dicEstoque[chaveVenda] += -int(tuplaVenda[0])
            if dicEstoque[chaveVenda] <= 0:
                dicEstoque.pop(chaveVenda)

        else:
            dicEstoque[chaveVenda] = -int(tuplaVenda[0])
            if dicEstoque[chaveVenda] < 0:
                dicEstoque.pop(chaveVenda)

        print(dicEstoque)
        print(dicVenda)

    # COMPRAS
    def registraTransacaoCompra():
        chaveCompra = produtoEntrada.get()
        quantidadeCompra = quantidadeEntrada.get()
        precoCompra = precoEntrada.get()
        tuplaCompra = (quantidadeCompra, precoCompra)
        if chaveCompra in dicCompra:
            listaCompra = dicCompra[chaveCompra]
            listaCompra.append(tuplaCompra)
            # ---------------------->>> ESCREVER NO ARQUIVO
            dicCompra[chaveCompra] = listaCompra
        else:
            listaCompra = []
            listaCompra.append(tuplaCompra)
            dicCompra[chaveCompra] = listaCompra
        if chaveCompra in dicEstoque:
            dicEstoque[chaveCompra] += int(tuplaCompra[0])

        else:
            dicEstoque[chaveCompra] = int(tuplaCompra[0])

        print(dicCompra)
        print(dicEstoque)

    # -----------------LAYOUT JANELA TRANSAÇAO--------------------
    
    janelaTransacao = customtkinter.CTk(fg_color='#87CEFA')
    
    largura = 400
    altura = 200

    largura_tela = janelaTransacao.winfo_screenwidth()
    altura_tela = janelaTransacao.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura  / 2
    janelaTransacao.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
    
    janelaTransacao.title("Registrar Transação")
    janelaTransacao.geometry("400x200+525+270")
    janelaTransacao.resizable(width=False, height=False)

    # --------------------LAYOUT DOS BOTOES--------------------------
    produto = customtkinter.CTkLabel(janelaTransacao, fg_color='#87CEFA' , text_color='black' ,text="Produto:")
    produto.place(x=60, y=20)

    produtoEntrada = customtkinter.CTkEntry(janelaTransacao,fg_color='white', text_color='black')
    produtoEntrada.place(x=200, y=20)

    produtoQuantidade = customtkinter.CTkLabel(janelaTransacao, fg_color='#87CEFA' , text_color='black' ,text="Quantidade:")
    produtoQuantidade.place(x=60, y=50)

    quantidadeEntrada = customtkinter.CTkEntry(janelaTransacao,fg_color='white', text_color='black')
    quantidadeEntrada.place(x=200, y=50)

    produtoPreco = customtkinter.CTkLabel(janelaTransacao, fg_color='#87CEFA' , text_color='black' ,text="Preço:")
    produtoPreco.place(x=60, y=80)

    precoEntrada = customtkinter.CTkEntry(janelaTransacao,fg_color='white', text_color='black')
    precoEntrada.place(x=200, y=80)

    botaoVenda = customtkinter.CTkButton(janelaTransacao,fg_color='blue' , text="Registrar Venda",
                           command=registraTransacaoVenda)
    botaoVenda.place(x=55, y=130)
    #botaoVenda["bg"] = "red"

    botaoCompra = customtkinter.CTkButton(janelaTransacao,fg_color='green' ,text="Registrar Compra",
                            command=registraTransacaoCompra)
    botaoCompra.place(x=205, y=130)
    #botaoCompra["bg"] = "green"

    botaoCancela = customtkinter.CTkButton(janelaTransacao, fg_color='red' ,text="Cancelar", 
                            command=janelaTransacao.destroy)
    botaoCancela.place(x=126, y=160)
    #botaoCancela["bg"] = "#FFE4B5"

    janelaTransacao.mainloop()

#-------------------------------FUNÇÃO JANELA HISTÓRICO DE TRANSAÇÃO---------------------------------
def criaJanelaHistorico():
    # cria janela
    janelaHistorico = tk.Tk()
    
    largura = 400
    altura = 400

    largura_tela = janelaHistorico.winfo_screenwidth()
    altura_tela = janelaHistorico.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura  / 2
    janelaHistorico.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
    
    janelaHistorico.title("Histórico de Transação")
    #janelaHistorico.geometry("400x400+525+0")
    janelaHistorico["bg"] = "#87CEFA"
    janelaHistorico.resizable(width=False, height=False)

    #-----------------------------Criação de um Notebook(elemento ttk)--------------------------------
    hist = ttk.Notebook(janelaHistorico)
    hist.place(x=0, y=0, width=400, height=400)
    tb1 = tk.Frame(hist)
    tb1["bg"] = "#87CEFA"

    hist.add(tb1, text='Compras')
    tb2 = tk.Frame(hist)
    hist.add(tb2, text='Vendas')
    tb2["bg"] = "#87CEFA"

     #criando aba 3
    tb3 = tk.Frame(hist)
    hist.add(tb3, text='Estoque')
    tb3["bg"] = "#87CEFA"
    
    # cria colunas estoque
    produto_label = customtkinter.CTkLabel(tb3,fg_color='#87CEFA', text_color='black', text="Produto")
    produto_label.grid(row=0, column=0, padx=10, pady=10)

    quantidade_label = customtkinter.CTkLabel(tb3,fg_color='#87CEFA', text_color='black', text="Qtd")
    quantidade_label.grid(row=0, column=1, padx=10, pady=10)


    validade_label = customtkinter.CTkLabel(tb3,fg_color='#87CEFA', text_color='black', text="validade")
    validade_label.grid(row=0, column=3, padx=10, pady=10)

    #row = 1
    #for produto, estocagem in dicEstoque.items():
        #for dadose in estocagem:
            #produto_label = tk.Label(tb3, text=produto)
            #produto_label.grid(row=row, column=0, padx=10, pady=10)

            #quantidade_label = tk.Label(tb3, text=dadose[0])
            #quantidade_label.grid(row=row, column=1, padx=10, pady=10)

            #preco_label = tk.Label(tb3, text=dadose[1])
            #preco_label.grid(row=row, column=2, padx=10, pady=10)

            #validade_label = tk.Label(tb3, text=dadose[2])
            #validade_label.grid(row=row, column=3, padx=10, pady=10)

            #row += 1

    # cria colunas compras
    produto_label = customtkinter.CTkLabel(tb1,fg_color='#87CEFA', text_color='black' ,text="Produto")
    produto_label.grid(row=0, column=0, padx=10, pady=10)

    quantidade_label = customtkinter.CTkLabel(tb1,fg_color='#87CEFA', text_color='black', text="Qtd")
    quantidade_label.grid(row=0, column=1, padx=10, pady=10)

    preco_label = customtkinter.CTkLabel(tb1,fg_color='#87CEFA', text_color='black', text="Preço")
    preco_label.grid(row=0, column=2, padx=10, pady=10)

    botaoCancela =customtkinter.CTkButton(janelaHistorico,fg_color='red',text="Voltar",width=80 , height=40, command=janelaHistorico.destroy)
    botaoCancela.place(x=300, y=30)
    #botaoCancela["bg"] = "#FFE4B5"

    row = 1
    for produto, compras in dicCompra.items():
        for dadosc in compras:
            produto_label = tk.Label(tb1, text=produto)
            produto_label.grid(row=row, column=0, padx=10, pady=10)

            quantidade_label = tk.Label(tb1, text=dadosc[0])
            quantidade_label.grid(row=row, column=1, padx=10, pady=10)

            preco_label = tk.Label(tb1, text=dadosc[1])
            preco_label.grid(row=row, column=2, padx=10, pady=10)

            row += 1
    # cria colunas vendas
    produto_label = customtkinter.CTkLabel(tb2,fg_color='#87CEFA',text_color='black' , text="Produto")
    produto_label.grid(row=0, column=0, padx=10, pady=10)

    quantidade_label = customtkinter.CTkLabel(tb2,fg_color='#87CEFA',text_color='black' , text="Qtd")
    quantidade_label.grid(row=0, column=1, padx=10, pady=10)

    preco_label = customtkinter.CTkLabel(tb2,fg_color='#87CEFA',text_color='black' ,text="Preço")
    preco_label.grid(row=0, column=2, padx=10, pady=10)

    row = 1
    for produto, vendas in dicVenda.items():
        for dadosv in vendas:
            produto_label = tk.Label(tb2, text=produto)
            produto_label.grid(row=row, column=0, padx=10, pady=10)

            quantidade_label = tk.Label(tb2, text=dadosv[0])
            quantidade_label.grid(row=row, column=1, padx=10, pady=10)

            preco_label = tk.Label(tb2, text=dadosv[1])
            preco_label.grid(row=row, column=2, padx=10, pady=10)

            row += 1

    janelaHistorico.mainloop()

# ------------------------------FUNÇAO JANELA GERENCIAMENTO DE USUARIO-------------------------------
def criaJanelaGerenciamento():
    # ---------------------------FUNCIONAMENTO GERENCIAMENTO DE USUARIO -----------------------------
    def gerenciaUsuario():
        chaveNome = entradaNomeUsuario.get()
        cpf = entradaCpf.get()
        telefone = entradaTelefone.get()
        senha = entradaSenha.get()
        nivel = entradaNivel.get()
        tuplaUsuario = (senha, nivel, telefone, cpf)
        if chaveNome in dicUsuario:
            # ---------------------->>> ESCREVER NO ARQUIVO
            dicUsuario[chaveNome] = tuplaUsuario
        else:
            listaUsuario = []
            listaUsuario.append(tuplaUsuario)
            dicUsuario[chaveNome] = listaUsuario
        print(dicUsuario)

    # ---------------------------------FUNCIONAMENTO PESQUISA DE USUARIO----------------------------
    def pesquisaUsuario():
        pesquisaNome = pesquisaEntrada.get()
        if pesquisaNome in dicUsuario:
            resultadoNome["text"] = "Nome:", pesquisaNome
            resultadoCpf["text"] = "CPF:", dicUsuario[pesquisaNome][0][3]
            resultadoTelefone["text"] = "Telefone:", dicUsuario[pesquisaNome][0][2]
            resultadoNivel["text"] = "Nível:", dicUsuario[pesquisaNome][0][1]
        else:
            resultadoNome["text"] = ""
            resultadoCpf["text"] = "ERRO: Usuário não cadastrado no sistema"
            resultadoTelefone["text"] = ""
            resultadoNivel["text"] = ""

    # ------------------------------FUNCIONAMENTO BOTAO EXCLUIR------------------------------------
    def excluirUsuario():
        excluiNome = pesquisaEntrada.get()
        if excluiNome in dicUsuario:
            dicUsuario.pop(excluiNome)
            print(dicUsuario)
            resultadoNome["text"] = ""
            resultadoCpf["text"] = ""
            resultadoTelefone["text"] = ""
            resultadoNivel["text"] = ""
            resultadoExclusao["text"] = "USUÁRIO EXCLUÍDO COM SUCESSO!"
        else:
            resultadoNome["text"] = ""
            resultadoCpf["text"] = ""
            resultadoTelefone["text"] = ""
            resultadoNivel["text"] = ""
            resultadoExclusao["text"] = "IMPOSSÍVEL EXCLUIR"

    # --------------------------LAYOUT JANELA GERENCIAMENTO----------------------------

    
    janelaGerenciamento = tk.Tk()
    
    largura = 530
    altura = 420

    largura_tela = janelaGerenciamento.winfo_screenwidth()
    altura_tela = janelaGerenciamento.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura  / 2
    janelaGerenciamento.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
    
    janelaGerenciamento["bg"] = "#87CEFA"
    #janelaGerenciamento.geometry("530x420+525+0") 
    janelaGerenciamento.title("Gerenciamento de Usuário")
    janelaGerenciamento.resizable(width=False, height=False)

    # --------------------------BOTOES ADICIONAR USUARIO------------------------------
    nomeUsuario = customtkinter.CTkLabel(janelaGerenciamento, fg_color='#87CEFA', text_color='black', text="Nome do usuário:")
    nomeUsuario.place(x=20, y=20)
    #nomeUsuario["bg"] = "#87CEFA"

    entradaNomeUsuario = customtkinter.CTkEntry(janelaGerenciamento,fg_color='white', text_color='black' ,width=280, height=20)
    entradaNomeUsuario.place(x=150, y=20)

    cpfUsuario = customtkinter.CTkLabel(janelaGerenciamento,fg_color='#87CEFA',text_color='black' , text="CPF do usuário:")
    cpfUsuario.place(x=20, y=50)
    #cpfUsuario["bg"] = "#87CEFA"

    entradaCpf = customtkinter.CTkEntry(janelaGerenciamento,fg_color='white', text_color='black' ,width=280, height=20)
    entradaCpf.place(x=150, y=50)

    telefoneUsuario = customtkinter.CTkLabel(janelaGerenciamento,fg_color='#87CEFA',text_color='black' , text="Telefone do usuário:")
    telefoneUsuario.place(x=20, y=80)
    #telefoneUsuario["bg"] = "#87CEFA"

    entradaTelefone = customtkinter.CTkEntry(janelaGerenciamento,fg_color='white', text_color='black' ,width=280, height=20)
    entradaTelefone.place(x=150, y=80)

    senhaUsuario = customtkinter.CTkLabel(janelaGerenciamento,fg_color='#87CEFA',text_color='black' , text="Senha do usuário:")
    senhaUsuario.place(x=20, y=110)
    #senhaUsuario["bg"] = "#87CEFA"

    entradaSenha = customtkinter.CTkEntry(janelaGerenciamento,fg_color='white', text_color='black' ,width=280, height=20)
    entradaSenha.place(x=150, y=110)

    nivelUsuario = customtkinter.CTkLabel(janelaGerenciamento,fg_color='#87CEFA',text_color='black' , text="Digite o nível de acesso:\n\nNível 1:Acesso mínimo | Nível 2:Acesso intermediário | Nível 3: Acesso máximo")
    nivelUsuario.place(x=20, y=145)
    #nivelUsuario["bg"] = "#87CEFA"

    entradaNivel = customtkinter.CTkEntry(janelaGerenciamento,fg_color='white', text_color='black' , width=50, height=20)
    entradaNivel.place(x=340, y=140)

    botaoAddUsuario = customtkinter.CTkButton(janelaGerenciamento,fg_color='orange' ,text="Atualizar usuário", command=gerenciaUsuario)
    botaoAddUsuario.place(x=200, y=200)

    # -----------------------------------BOTOES PESQUISAR USUARIO-----------------------------------
    nomePesquisa = customtkinter.CTkLabel(janelaGerenciamento,fg_color='#87CEFA',text_color='black' , text="Nome:")
    nomePesquisa.place(x=20, y=270)
    #nomePesquisa["bg"] = "#87CEFA"

    pesquisaEntrada = customtkinter.CTkEntry(janelaGerenciamento,fg_color='white', text_color='black' ,width=280, height=20)
    pesquisaEntrada.place(x=70, y=270)
    ##pesquisaEntrada["bg"] = "#87CEFA"

    botaoPesquisar = customtkinter.CTkButton(janelaGerenciamento,fg_color='green' ,text="Pesquisar", command=pesquisaUsuario)
    botaoPesquisar.place(x=370, y=267)
    # ----------------------------------RESULTADO DA PESQUISA---------------------------------------
    resultadoNome = tk.Label(janelaGerenciamento, text="")
    resultadoNome.place(x=70, y=300)
    resultadoNome["bg"] = "#87CEFA"
    
    resultadoCpf = tk.Label(janelaGerenciamento, text="")
    resultadoCpf.place(x=70, y=320)
    resultadoCpf["bg"] = "#87CEFA"
    
    resultadoTelefone = tk.Label(janelaGerenciamento, text="")
    resultadoTelefone.place(x=70, y=340)
    resultadoTelefone["bg"] = "#87CEFA"

    resultadoNivel = tk.Label(janelaGerenciamento, text="")
    resultadoNivel.place(x=70, y=360)
    resultadoNivel["bg"] = "#87CEFA"
    # ------------------------------BOTAO PARA EXCLUIR USUARIO---------------------------------------
    botaoExcluir = customtkinter.CTkButton(janelaGerenciamento,fg_color="red" ,text="Excluir\nUsuário",command=excluirUsuario)
    botaoExcluir.place(x=370, y=320)
    botaoVoltar = customtkinter.CTkButton(janelaGerenciamento,fg_color='blue' ,text="Voltar", command=janelaGerenciamento.destroy)
    botaoVoltar.place(x=370, y=370)



    # -----------------------------RESULTADO DA AÇAO EXCLUIR---------------------------------------
    resultadoExclusao = tk.Label(janelaGerenciamento, text="")
    resultadoExclusao.place(x=160, y=400)
    resultadoExclusao["bg"] = "#87CEFA"

# -----------------------------FUNÇAO CRIA JANELA PESQUISAR PRODUTO---------------------------------


def criaJanelaPesquisaProduto():

    # ---------------------------FUNCIONAMENTO BOTOES PESQUISA PRODUTO-------------------------------
    def pesquisaProduto():
        pesquisaProdutoNome = entradaNomeProduto.get()
        if pesquisaProdutoNome in dicEstoque:
            produtoResultadoNome["text"] = "Nome:", pesquisaProdutoNome
            produtoResultadoQuantidade["text"] = "Qtd em estoque:", dicEstoque[pesquisaProdutoNome]
            janelaPesquisaProduto.geometry("415x140+525+270")
        else:
            produtoResultadoNome["text"] = pesquisaProdutoNome, "em falta!"
            produtoResultadoQuantidade["text"] = ""

    # -------------------------------LAYOUT JANELA PESQUISA PRODUTO---------------------------------
    janelaPesquisaProduto = tk.Tk()
    
    largura = 415
    altura = 100

    largura_tela = janelaPesquisaProduto.winfo_screenwidth()
    altura_tela = janelaPesquisaProduto.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura  / 2
    janelaPesquisaProduto.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
    
    #janelaPesquisaProduto.geometry("415x100+525+270")
    janelaPesquisaProduto.title("Pesquisa Produto")
    janelaPesquisaProduto["bg"] = "#87CEFA"
    janelaPesquisaProduto.resizable(width=False, height=False)

    # -----------------------------LAYOUT BOTOES PESQUISA PRODUTO-----------------------------------
    nomeProduto = tk.Label(janelaPesquisaProduto, text="Nome do produto:")
    nomeProduto.place(x=20, y=20)
    nomeProduto["bg"] = "#87CEFA"

    entradaNomeProduto = customtkinter.CTkEntry(janelaPesquisaProduto,fg_color="white", text_color='black')
    entradaNomeProduto.place(x=140, y=20)

    botaoProcurar = customtkinter.CTkButton(janelaPesquisaProduto,fg_color='green' ,text="Pesquisar", command=pesquisaProduto)
    botaoProcurar.place(x=60, y=52)



    botaoVoltar =customtkinter.CTkButton(janelaPesquisaProduto,text="Voltar", command=janelaPesquisaProduto.destroy)
    botaoVoltar.place(x=220, y=52)
    

    produtoResultadoNome = tk.Label(janelaPesquisaProduto, text="")
    produtoResultadoNome.place(x=140, y=80)
    produtoResultadoNome["bg"] = "#87CEFA"

    produtoResultadoQuantidade = tk.Label(janelaPesquisaProduto, text="")
    produtoResultadoQuantidade.place(x=125, y=100)
    produtoResultadoQuantidade["bg"] = "#87CEFA"

# ----------------------------------CHECAR ESTOQUE ----------------------------------------#
def criaJanelaEstoque():
    janelaEstoque = tk.Tk()
    
    largura = 400
    altura = 200

    largura_tela = janelaEstoque.winfo_screenwidth()
    altura_tela = janelaEstoque.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura  / 2
    janelaEstoque.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
    
    #janelaEstoque.title("Total de Estoque")
    #janelaEstoque.geometry("400x200")
    janelaEstoque.resizable(width=False, height=False)
    janelaEstoque.mainloop()

# ------------------------------------FUNÇAO TELA ADMIN--------------------------------------
def telaAdmin(x):
    # --------------------LAYOUT JANELA ADMIN----------------------
    x.destroy()
    janela = customtkinter.CTk(fg_color='#87CEFA')
    
    largura = 400
    altura = 350

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    posX = largura_tela / 2 - largura / 2
    posY = altura_tela / 2 - altura  / 2
    janela.geometry("%dx%d+%d+%d"%(largura, altura, posX, posY))
    
    #janela.geometry("400x350") #400x350
    janela.title("Controle de Estoque - Unibra (Administrador)")
    janela.resizable(width=False, height=False)

    # ----------------------LAYOUT DOS BOTOES--------------------------
    botaoTransacao = customtkinter.CTkButton(janela,width=360, height=50,text="Registrar Transação", command=criaJanelaTransacao)
    botaoTransacao.place(x=20, y=20)
    
    #botaoTransacao["bg"] = "#B0E0E6"


    botaoCadastro = customtkinter.CTkButton(janela, text="Gerenciamento de Usuário", width=360, height=50, command=criaJanelaGerenciamento)
    botaoCadastro.place(x=20, y=80)
    #botaoCadastro["bg"] = "#B0E0E6"



    botaoPesquisa = customtkinter.CTkButton(janela, text="Pesquisar Produto", width=360, height=50, command=criaJanelaPesquisaProduto)
    botaoPesquisa.place(x=20, y=140)
    #botaoPesquisa["bg"] = "#B0E0E6"


    botaoHistorico = customtkinter.CTkButton(janela, text="Histórico de Transações", width=360, height=50, command=criaJanelaHistorico)
    botaoHistorico.place(x=20, y=200)
    #botaoHistorico["bg"] = "#B0E0E6"



    botaoHistoria = customtkinter.CTkButton(janela, text="Conheça nossos Produtos", width=360, height=50, command = lambda: webbrowser.open('index.html'))
    botaoHistoria.place(x=20, y=260)
    #botaoHistoria["bg"] = "#FFC0CB"



   # botaoEstoque = customtkinter.CTkButton(janela, text="Checar Estoque", width=360, height=50, command=criaJanelaEstoque)
    #botaoEstoque.place(x=20, y=320)
    #botaoEstoque["bg"] = "#B0E0E6"

    janela.mainloop()

# ----------------------------------FUNÇAO DE LOGIN---------------------------------


def acesso(p1, p2, p3, p4):

    usuario = p1.get()
    password = p2.get()
    aviso = p3
    if usuario == "unibra" and password == "unibra":
        telaAdmin(p4)
    elif usuario == "admin2" and password == "admin2":
        criaJanelaGerenciamento()
    else:
        aviso["text"] = "Usuário ou senha incorretos"