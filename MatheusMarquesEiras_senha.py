from tkinter import *
from random import *

# Desenha as partes do layout
# Desenha a linha de cima
def linha_cima():
    # Variaveis que fazem os quadrados se moverem da esquerda para direita
    primeiroX = 0
    segundoX = 25

    # Lopp que move os quadrados
    for quadrado in range(1,33):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgJanela.create_rectangle(primeiroX, 0, segundoX, 25, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgJanela.create_rectangle(primeiroX, 0, segundoX, 25, fill='white', outline='white')

        # Move os quadrados 25 pixels
        primeiroX += 25
        segundoX += 25

# Desenha a linha da direita
def linha_direita():
    # Variaveis que movem os quadrados de cima para baixo
    primeiroY = 25
    segundoY = 50

    # Loop que movem os quadrados
    for quadrado in range(1,23):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgJanela.create_rectangle(775, primeiroY, 800, segundoY, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgJanela.create_rectangle(775, primeiroY, 800, segundoY, fill='white', outline='white')
        
        # Move os quadrados 25 pixels
        primeiroY += 25
        segundoY += 25

# Desenha a linha de baixo
def linha_baixo():
    # Variaveis que movem os quadrados da direita para esquerda
    primeiroX = 800
    segundoX = 775

    # Loop que movem os quadrados
    for quadrado in range(1,33):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgJanela.create_rectangle(primeiroX, 575, segundoX, 600, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgJanela.create_rectangle(primeiroX, 575, segundoX, 600, fill='white', outline='white')
        
        # Move os quadrados 25 pixels
        primeiroX -= 25
        segundoX -= 25

# Desenha a linha da esquerda
def linha_esquerda():
    # Variaveis que movem os quadrados de baixo pra cima
    primeiroY = 550
    segundoY = 575

    # Loop que movem os quadrados
    for quadrado in range(1,23):
        # Pinta quadrados impares com a cor preta
        if quadrado % 2 != 0:
            confgJanela.create_rectangle(0, primeiroY, 25, segundoY, fill='black', outline='black')
        # Pinta os quadrados pares de branco
        else:
            confgJanela.create_rectangle(0, primeiroY, 25, segundoY, fill='white', outline='white')
        
        # Move os quadrados 25 pixels
        primeiroY -= 25
        segundoY -= 25

# Desenha o menu inicial
def menu_inicial():
    label_menu()
    botoes_menu()

# Desenha o label  do menu inocial 
def label_menu():
    # Variavel global usada
    global labelMenuIncial

    # Desenha o label "Menu incial" e o posiciona
    labelMenuIncial = Label(confgJanela, text="Menu incial", width=42, height=5)
    labelMenuIncial.place(x=250,y=50)

# Desenha os botões do menu incial
def botoes_menu():
    # Variaveis globais usadas
    global botaoNovoJogo
    global botaoInformacao
    global botaoSair

    # Desenha o botao novo jogo que chama a função novo_jogo e o posiciona
    botaoNovoJogo = Button(confgJanela,text="Novo jogo",width=20,height=3,command=novo_jogo)
    botaoNovoJogo.place(x=325,y=150)

    # Desenha o botão informação que chaam a função informacao e o posiciona
    botaoInformacao = Button(confgJanela,text="Informação",width=20,height=3,command=informacao)
    botaoInformacao.place(x=325,y=225)

    # Desenha o botão sair que chama a função sair_jogo e o posiciona
    botaoSair = Button(confgJanela,text="Sair",width=20,height=3,command=sair_jogo)
    botaoSair.place(x=325,y=300)

# Deleta o menu inicial
def deleta_menu():
    # Variaveis globais usadas
    global labelMenuIncial
    global botaoNovoJogo
    global botaoInformacao
    global botaoSair

    labelMenuIncial.destroy()
    botaoNovoJogo.destroy()
    botaoInformacao.destroy()
    botaoSair.destroy()

# Elabora um novo jogo
def novo_jogo():
    deleta_menu()
    elabora_jogo()

# Desenha todos os elemnetos do jogo em sí
def elabora_jogo():
    seleciona_cores_misteriosas()
    define_tentativa()
    desenha_conteiner_tentativas()
    desenha_matriz_tentativas()
    desenha_quadrados_dicas()
    desenha_matriz_dicas()
    desenha_botoes_selecionar_cores()
    desenha_matriz_cores_escolhidas()
    desenha_botoes_limpar_cores()
    desenha_botao_verificar()
    desenha_botao_voltar()

# Sorteia a sequencia de cores misteriosas
def seleciona_cores_misteriosas():
    # Variavel usada
    global listaCoresMisteriosas

    # Define a lista de cores que podem ser sorteadas
    listaCoresDisponiveis = ["red","green","purple","pink","blue","orange"]

    # Loop para sortear 4 cores diferentes
    for i in range(0,4):
        selecionada = choices(listaCoresDisponiveis)[0] # Seleciona aleatoriamente uma cor da lista
        listaCoresMisteriosas.append(selecionada) # Adiciona essa cor a uma outra lista chamada de lista cores misteriosas
        listaCoresDisponiveis.remove(selecionada) # remove da lista cores disponiveis a cor que foi selecionada para ela não se repetir na lista

# Define o numero de tentativas padrao para todo o inicio de jogo
def define_tentativa():
    # Variaveis globais usadas
    global tentativa_atual
    global listaTentativa 

    # Tentativa atual do usuario em todo começo de jogo
    tentativa_atual = 0

    # Gera uma lista composta somente por None para ser usada na hora do usurio escolher uma cor
    listaTentativa = [None,None,None,None]

# limpa a lista cores misteriosas para não ter problemas de memoria
def limpa_lista_cores_misteriosas():
    # Variavel global usada
    global listaCoresMisteriosas

    # Limpa lista cores misteriosas
    listaCoresMisteriosas = []
    
# Desenha o conteiner que ira conter as tentativas do usuario
def desenha_conteiner_tentativas():
    # Variavel global usada
    global conteinerTentativa

    # Desenha o conteiner que ir guardar as tentativas e as dicas
    conteinerTentativa = confgJanela.create_rectangle(25,25,325,575,fill="cyan")

# deleta conteiner tentativas
def deleta_conteiner_tentativas():
    # Variavel global usada
    global conteinerTentativa

    confgJanela.delete(conteinerTentativa)

def desenha_matriz_tentativas():
    # Variavel global usada
    global matrizTentativas

    # define a matriz tentativas
    matrizTentativas = []
    # criando os retângulos e adicionando à matriz
    for i in range(1,11):
        # Define a lita da linha atual
        linha = []
        for j in range(1,5):
            # Faz quatro quadrados de cor cinza da esquerda para direita e os adiciona a lista linha
            rect = confgJanela.create_rectangle(j*50, i*50, j*50+25, i*50+25, fill="grey")
            linha.append(rect)
        # Adicina cada linha a matriz tentativas
        matrizTentativas.append(linha)

# Deleta toda a matriz tentativa
def deleta_matriz_tentativas():
    # variavel global usada
    global matrizTentativas

    # Loop para deletar todos os elementos da metriz
    for i in range(0,10):
        for j in range(0,4):
            confgJanela.delete(matrizTentativas[i][j])

# Gera quadrados que irão conter osquadrados menores das dicas
def desenha_quadrados_dicas():
    # variavel global usada
    global quadradosConteiners

    # Lista para  guardar cada quadrdo conteiner dicas
    quadradosConteiners = []

    # Variaveis que movem os quadrados de cima para baixo
    primeiroYAmarelo = 40
    segundoYAmarelo = 80

    # Loop que faz os quadrados serem desenhados de cima para baixo
    for i in range(0,10):
        # Faz os quadrados cyan
        conteinerDicas = confgJanela.create_rectangle(260,primeiroYAmarelo,300,segundoYAmarelo,fill="cyan")
        # Adiciona na lista os conteiners dicas
        quadradosConteiners.append(conteinerDicas)
        # Move os quadrados 50 pixels
        primeiroYAmarelo += 50
        segundoYAmarelo += 50

# deleta cada quadrado conteiner dica 
def deleta_quadrados_dicas():
    global quadradosConteiners

    for i in range(0,10):
        confgJanela.delete(quadradosConteiners[i])

# Desnha a matriz de quadrados de dicas para o usuario
def desenha_matriz_dicas():
    # Variavel globla que sera usada
    global matrizDicas

    # Define matriz dicas
    matrizDicas = []

    # Variaveis que movem os quadrados das dicas de baixo para cima agurpando em quarteirões
    primeiroXDica = 265
    segundaVezXPrimeiro = primeiroXDica
    primeiroYDica = 45 
    segundaVezYPrimeiro = 65

    segundoXDica = 275
    segundaVezXSegundo = segundoXDica
    segundoYDica = 55
    segundaVezYSegundo = 75

    # Loop para merar os quadrados menores qe iráo fornecer dicas ao usuario
    for i in range(1,11):
        # Define uma lista para a linha atual
        linha = []

        # Loop para gerar quatro quadrados para dar icas a tentativa atual do usuario
        for j in range(1,5):
            # Se o quadrado passar de dois ele volta alinhado com os de cima dele
            if j >= 3:
                retangulo = confgJanela.create_rectangle(segundaVezXPrimeiro,segundaVezYPrimeiro,segundaVezXSegundo,segundaVezYSegundo,fill="grey")
                # Adiciona o retangulo a lista linha
                linha.append(retangulo)
                segundaVezXPrimeiro += 20
                segundaVezXSegundo += 20
            # Se o quadrados não passarem de dois ele é desenhado da esquerda para direita
            else:
                retangulo = confgJanela.create_rectangle(primeiroXDica,primeiroYDica,segundoXDica,segundoYDica,fill="grey")
                # Adiciona o retangulo a lista linha
                linha.append(retangulo)
                primeiroXDica += 20
                segundoXDica += 20

        # Adiciona a linha a matriz dicas
        matrizDicas.append(linha)
        # Obtem o primeiro x inicail primeiro
        primeiroXDica = 265
        # volta para o primeiro x primeiro
        segundaVezXPrimeiro = primeiroXDica

        primeiroYDica +=50
        segundaVezYPrimeiro += 50

        # Obtem o primeiro x inicail primeiro
        segundoXDica = 275
        # volta para o primeiro x primeiro
        segundaVezXSegundo = segundoXDica

        segundoYDica += 50
        segundaVezYSegundo += 50

# Deleta a matriz dicas
def deleta_matriz_dicas():
    global matrizDicas

    for i in range(0,10):
        for j in range(0,4):
            confgJanela.delete(matrizDicas[i][j])

# desenha botões para selecionar cores
def desenha_botoes_selecionar_cores():
    # Variaveis globais que serao usadas
    global botaoVermelho
    global botaoVerde
    global botaoRoxo
    global botaoRosa
    global botaoAzul
    global botaoLaranja

    # Desenha o botão vermelho que chama a função coloca_vermelho e o posiciona
    botaoVermelho = Button(confgJanela,bg="red", width=5,height=2,command=coloca_vermelho)
    botaoVermelho.place(x=350,y=50)

    # Desenha o botão verde que chama a função coloca_verde e o posiciona
    botaoVerde = Button(confgJanela,bg="green", width=5,height=2,command=coloca_verde)
    botaoVerde.place(x=418,y=50)

    # Desenha o botão roxo que chama a função coloca_roxo e o posiciona
    botaoRoxo = Button(confgJanela,bg="purple", width=5,height=2,command=coloca_roxo)
    botaoRoxo.place(x=486,y=50)

    # Desenha o botão rosa que chama a função coloca_rosa e o posiciona
    botaoRosa = Button(confgJanela,bg="pink", width=5,height=2,command=coloca_rosa)
    botaoRosa.place(x=554,y=50)

    # Desenha o botão azul que chama a função coloca_azul e o posiciona
    botaoAzul = Button(confgJanela,bg="blue", width=5,height=2,command=coloca_azul)
    botaoAzul.place(x=622,y=50)

    # Desenha o botão laranja que chama a função coloca_laranja e o posiciona
    botaoLaranja = Button(confgJanela,bg="orange", width=5,height=2,command=coloca_laranja)
    botaoLaranja.place(x=690,y=50)

# Coloca a cor vermelha
def coloca_vermelho():
    # Variaveis globais usadas
    global listaTentativa
    global matrizCoresEscolhidas

    # Verifica se a cor não esta na lista tentativas
    if "red" not in listaTentativa:
        # Loop para passar em cada item da lista
        for i in range(0,4):
            # Verifica se o valor do item não é None
            if listaTentativa[i] is None:
                # Adiciona a cor a lista tentativa
                listaTentativa[i] = "red"
                # Muda a cor da matriz cores escolhidas com a cor que foi escolhida em determinado item
                confgJanela.itemconfig(matrizCoresEscolhidas[i], fill="red")
                # Sai do loop depois de achar um valor None e substitui-lo pela cor da lista tentativa
                break

# Coloca a cor verde
def coloca_verde():
    # Variaveis globais usadas
    global listaTentativa
    global matrizCoresEscolhidas

    # Verifica se a cor não esta na lista tentativas
    if "green" not in listaTentativa:
        # Loop para passar em cada item da lista
        for i in range(0,4):
            # Verifica se o valor do item não é None
            if listaTentativa[i] is None:
                # Adiciona a cor a lista tentativa
                listaTentativa[i] = "green"
                # Muda a cor da matriz cores escolhidas com a cor que foi escolhida em determinado item
                confgJanela.itemconfig(matrizCoresEscolhidas[i], fill="green")
                # Sai do loop depois de achar um valor None e substitui-lo pela cor da lista tentativa
                break

# Coloca a cor roxa
def coloca_roxo():
    # Variaveis globais usadas
    global listaTentativa
    global matrizCoresEscolhidas

    # Verifica se a cor não esta na lista tentativas
    if "purple" not in listaTentativa:
        # Loop para passar em cada item da lista
        for i in range(0,4):
            # Verifica se o valor do item não é None
            if listaTentativa[i] is None:
                # Adiciona a cor a lista tentativa
                listaTentativa[i] = "purple"
                # Muda a cor da matriz cores escolhidas com a cor que foi escolhida em determinado item
                confgJanela.itemconfig(matrizCoresEscolhidas[i], fill="purple")
                # Sai do loop depois de achar um valor None e substitui-lo pela cor da lista tentativa
                break

# Coloca a cor rosa
def coloca_rosa():
    # Variaveis globais usadas
    global listaTentativa
    global matrizCoresEscolhidas

    # Verifica se a cor não esta na lista tentativas
    if "pink" not in listaTentativa:
        # Loop para passar em cada item da lista
        for i in range(0,4):
            # Verifica se o valor do item não é None
            if listaTentativa[i] is None:
                # Adiciona a cor a lista tentativa
                listaTentativa[i] = "pink"
                # Muda a cor da matriz cores escolhidas com a cor que foi escolhida em determinado item
                confgJanela.itemconfig(matrizCoresEscolhidas[i], fill="pink")
                # Sai do loop depois de achar um valor None e substitui-lo pela cor da lista tentativa
                break

# Coloca a cor azul
def coloca_azul():
    # Variaveis globais usadas
    global listaTentativa
    global matrizCoresEscolhidas

    # Verifica se a cor não esta na lista tentativas
    if "blue" not in listaTentativa:
        # Loop para passar em cada item da lista
        for i in range(0,4):
            # Verifica se o valor do item não é None
            if listaTentativa[i] is None:
                # Adiciona a cor a lista tentativa
                listaTentativa[i] = "blue"
                # Muda a cor da matriz cores escolhidas com a cor que foi escolhida em determinado item
                confgJanela.itemconfig(matrizCoresEscolhidas[i], fill="blue")
                # Sai do loop depois de achar um valor None e substitui-lo pela cor da lista tentativa
                break

# Coloca a cor laranja
def coloca_laranja():
    # Variaveis globais usadas
    global listaTentativa
    global matrizCoresEscolhidas

    # Verifica se a cor não esta na lista tentativas
    if "orange" not in listaTentativa:
        # Loop para passar em cada item da lista
        for i in range(0,4):
            # Verifica se o valor do item não é None
            if listaTentativa[i] is None:
                # Adiciona a cor a lista tentativa
                listaTentativa[i] = "orange"
                # Muda a cor da matriz cores escolhidas com a cor que foi escolhida em determinado item
                confgJanela.itemconfig(matrizCoresEscolhidas[i], fill="orange")
                # Sai do loop depois de achar um valor None e substitui-lo pela cor da lista tentativa
                break

# deleta os botões para selecionar cores
def deleta_botoes_selecionar_cores():
    # Variaveis globais usadas
    global botaoVermelho
    global botaoVerde
    global botaoRoxo
    global botaoRosa
    global botaoAzul
    global botaoLaranja

    botaoVermelho.destroy()
    botaoVerde.destroy()
    botaoRoxo.destroy()
    botaoRosa.destroy()
    botaoAzul.destroy()
    botaoLaranja.destroy()

# Matriz dos cores escolhidas
def desenha_matriz_cores_escolhidas():
    # Variavel global usada
    global matrizCoresEscolhidas

    # Define a lista matriz cores escolhidas que o usuario selecionou
    matrizCoresEscolhidas = []
    # Variaveis que permitem os quadrados serem desenhados da esquerda para direita
    primeiroXEscolha = 375
    segundoXEscolha = 425

    # Loop para desenhar os quadrados 
    for i in range(0,4):
        # Desenha o quadrado cor escolhida
        corEscolhida = confgJanela.create_rectangle(primeiroXEscolha,150,segundoXEscolha,200,fill="grey")
        # Adiciona o quadrado cor escolhida a lista matriz cores escolhidas
        matrizCoresEscolhidas.append(corEscolhida)

        # Move os quadrados em 100 pixels
        primeiroXEscolha += 100
        segundoXEscolha += 100

# Desleta a matriz cores escoolhidas
def deleta_matriz_cores_escolhidas():
    global matrizCoresEscolhidas

    for i in range(0,4):
        confgJanela.delete(matrizCoresEscolhidas[i])

# Desenha botões limpar cores
def desenha_botoes_limpar_cores():
    # Variaveis globais usadas
    global primeiroBotaoLimpar
    global segundoBotaoLimpar
    global terceiroBotaoLimpar
    global quartoBotaoLimpar

    # Desenha o botão que chama a função que limpa sua respectiva cor acima dele e o posiciona
    primeiroBotaoLimpar = Button(confgJanela,text="limpar",width=5,height=1,command=limpa_primeiro)
    primeiroBotaoLimpar.place(x=377.5,y=215)

    # Desenha o botão que chama a função que limpa sua respectiva cor acima dele e o posiciona
    segundoBotaoLimpar = Button(confgJanela,text="limpar",width=5,height=1,command=limpa_segundo)
    segundoBotaoLimpar.place(x=477.5,y=215)

    # Desenha o botão que chama a função que limpa sua respectiva cor acima dele e o posiciona
    terceiroBotaoLimpar = Button(confgJanela,text="limpar",width=5,height=1,command=limpa_terceiro)
    terceiroBotaoLimpar.place(x=577.5,y=215)

    # Desenha o botão que chama a função que limpa sua respectiva cor acima dele e o posiciona
    quartoBotaoLimpar = Button(confgJanela,text="limpar",width=5,height=1,command=limpa_quarto)
    quartoBotaoLimpar.place(x=677.5,y=215)

# Limpa o primeiro quadrado
def limpa_primeiro():
    # Variaveis globais usadas
    global listaTentativa
    global matrizCoresEscolhidas

    # Atribui None a lista tentativas e pinta o o qudrado especifico da matriz cores escolhidas de cinza
    listaTentativa[0] = None
    confgJanela.itemconfig(matrizCoresEscolhidas[0],fill="grey")

# Limpa o segundo quadrado
def limpa_segundo():
    # Variaveis globais usadas
    global listaTentativa
    global matrizCoresEscolhidas

    # Atribui None a lista tentativas e pinta o o qudrado especifico da matriz cores escolhidas de cinza
    listaTentativa[1] = None
    confgJanela.itemconfig(matrizCoresEscolhidas[1],fill="grey")

# Limpa o terceiro quadrado
def limpa_terceiro():
    # Variaveis globais usadas
    global listaTentativa
    global matrizCoresEscolhidas

    # Atribui None a lista tentativas e pinta o o qudrado especifico da matriz cores escolhidas de cinza
    listaTentativa[2] = None
    confgJanela.itemconfig(matrizCoresEscolhidas[2],fill="grey")

# Limpa o quarto quadrado
def limpa_quarto():
    # Variaveis globais usadas
    global listaTentativa
    global matrizCoresEscolhidas

    # Atribui None a lista tentativas e pinta o o qudrado especifico da matriz cores escolhidas de cinza
    listaTentativa[3] = None
    confgJanela.itemconfig(matrizCoresEscolhidas[3],fill="grey")

# Limpa todos os quadrados
def limpa_quadrados():
    limpa_primeiro()
    limpa_segundo()
    limpa_terceiro()
    limpa_quarto()

# Deleta os botões limpar cores
def deleta_botoes_limpar_cores():
    # Variaveis globais usadas
    global primeiroBotaoLimpar
    global segundoBotaoLimpar
    global terceiroBotaoLimpar
    global quartoBotaoLimpar

    primeiroBotaoLimpar.destroy()
    segundoBotaoLimpar.destroy()
    terceiroBotaoLimpar.destroy()
    quartoBotaoLimpar.destroy()

# Desenha botão verificar
def desenha_botao_verificar():
    # Variavel global usada
    global botaoVerificar

    # Desenha o botão verificar que chama a função verificar e o posiciona
    botaoVerificar = Button(confgJanela,text="verificar",width=13,height=2,command=verificar)
    botaoVerificar.place(x=500,y=275)

# Faz a verificação da resposta 
def verificar():
    # Variaveis globais usadas
    global listaTentativa
    global listaCoresMisteriosas
    global labelAviso
    global tentativa_atual
    global matrizDicas
    global matrizTentativas

    # Variavel responsavel por permitir analizar quadrado a quadrado
    quadradoAtual = 0

    # Se o label aviso estiver na tela ele é destruido na proxima verificação
    if labelAviso is not None:
        labelAviso.destroy()

    # Se um dos itens da lista tentativa não for preenchido é mostrado um aviso na tela 
    if None in listaTentativa:
        # Deseha o aviso e o posiciona
        labelAviso = Label(confgJanela,text="Você não preencheu um ou mais espaço(s)",width=21,height=2,wraplength=125)
        labelAviso.place(x=475,y=100)
    # Se todos os itens forem preenchidos então continua a verificação
    else:
        # Preenche cada um dos quadrados da matriz tentativas com as cores que o usuario selecionou
        for i in range(0,4):
            corEscolhida = listaTentativa[i]
            confgJanela.itemconfig(matrizTentativas[tentativa_atual][i],fill=corEscolhida)
        # Se o usuario acertou a sequencia ele ganha
        if listaTentativa == listaCoresMisteriosas:
            ganhou()
        # Se ele não acertou então são fornecidos dicas a ele 
        else:
            # Percorre cada um dos itens da lista tentativa 
            for i in range(0,4):
                # Se ele acertou a cor o quadrado é pintado de branco
                if listaTentativa[i] in listaCoresMisteriosas:
                    confgJanela.itemconfig(matrizDicas[tentativa_atual][quadradoAtual],fill="white")
                    # Se ele acertou a posição tambem o quadrado é pintado de preto
                    if listaTentativa[i] == listaCoresMisteriosas[i]:
                        confgJanela.itemconfig(matrizDicas[tentativa_atual][quadradoAtual],fill="black")
                    quadradoAtual+= 1

            # Limpa todos os quadrados
            limpa_quadrados()
            # Aumenta as tentativs
            tentativa_atual += 1
            # Se ele gastar todas as tentativas ele perde
            if tentativa_atual == 10:
                perdeu()

# Função chamada quando o usuario ganha 
def ganhou():
    deleta_jogo()
    texto_ganhou()
    desenha_cores_misteriosas()
    botoes_volta_jogar_ganhou()

# Desenha o texto quando o usuario ganhou
def texto_ganhou():
    # Variavel global usada
    global textoGanhou

    # Desenha o texto quando o usuario ganhou e o posiciona
    textoGanhou = Label(confgJanela, text="Você ganhou a sequencia era: ", width=42, height=5)
    textoGanhou.place(x=250,y=50)

# Desenha o botão para voltar ao menu incial
def botoes_volta_jogar_ganhou():
    # Variaveis globais usadas
    global botaoSairJogoFinal
    global botaoVoltaMenuGanhou

    # Desenha o botão jogar novamente que chama a função ganhou_retorna_comeco e o posiciona
    botaoVoltaMenuGanhou = Button(confgJanela, text="Jogar novamente", width=13, height=2,command=ganhou_retorna_comeco)
    botaoVoltaMenuGanhou.place(x=425, y=225)

    # Desenha o botão sair do jogo qua chama a função sair_jogo e a posiciona
    botaoSairJogoFinal = Button(confgJanela, text="Sair do jogo", width=13, height=2, command=sair_jogo)
    botaoSairJogoFinal.place(x=275, y=225)

# retorna ao menu principal 
def ganhou_retorna_comeco():
    # Variaveis globais usadas
    global textoGanhou
    global botaoSairJogoFinal
    global botaoVoltaMenuGanhou

    textoGanhou.destroy()
    botaoSairJogoFinal.destroy()
    botaoVoltaMenuGanhou.destroy()
    limpa_lista_cores_misteriosas()
    deleta_matriz_cor_revelada()
    menu_inicial()

# Função chamada quando o usuario perde
def perdeu():
    deleta_jogo()
    texto_perdeu()
    desenha_cores_misteriosas()
    botoes_volta_jogar_perdeu()

# Desenha o texto perdeu
def texto_perdeu():
    # Variavel globla usada
    global textoPerdeu

    # Desenha o texto quando o usuario perdeu e o posiciona
    textoPerdeu = Label(confgJanela,text="Você perdeu a sequencia era: ",width=42, height=5)
    textoPerdeu.place(x=250,y=50)

# Desenha as cores misteriosas selecionas 
def desenha_cores_misteriosas():
    # Variaveis globais usadas
    global matrizCorRevelada
    global listaCoresMisteriosas

    # Variaveis que desenham os quadrados da esquerda para direita
    primeiroXRevela = 225
    segundoXRevela = 275
    
    # Loop para desenhar os quadrados com a sequencia sorteada
    for i in range(0,4):
        # Obtem a cor do item
        cor = listaCoresMisteriosas[i]
        # Desenha o quadrado
        corRevelada = confgJanela.create_rectangle(primeiroXRevela,150,segundoXRevela,200,fill=cor)
        # Adiciona a matriz cor revelada a cor revelada
        matrizCorRevelada.append(corRevelada)
        # Move os quadrados da esquerda para direita
        primeiroXRevela += 100
        segundoXRevela += 100

# Deleta a matriz cor revelada
def deleta_matriz_cor_revelada():
    # Variavel global usada
    global matrizCorRevelada

    for i in range(0,4):
        confgJanela.delete(matrizCorRevelada[i])

# Desenha os botoes jogar novmente e sair do jogo
def botoes_volta_jogar_perdeu():
    # Variaveis globis usadas
    global botaoSairJogoFinal
    global botaoVoltaMenuPerdeu

    # Desenha o botao jogar novemente que chama a função perdeu_retorna_comeco e o posiciona 
    botaoVoltaMenuPerdeu = Button(confgJanela, text="Jogar novamente", width=13, height=2, command=perdeu_retorna_comeco)
    botaoVoltaMenuPerdeu.place(x=425, y=225)

    # Desenha o botao sair do jogo que chama a função sair_jogo e o posiciona 
    botaoSairJogoFinal = Button(confgJanela, text="Sair do jogo", width=13, height=2, command=sair_jogo)
    botaoSairJogoFinal.place(x=275, y=225)

# Volta para o menu inicial
def perdeu_retorna_comeco():
    # Variaveis globis usadas
    global textoPerdeu
    global botaoSairJogoFinal
    global botaoVoltaMenuPerdeu

    textoPerdeu.destroy()
    botaoSairJogoFinal.destroy()
    botaoVoltaMenuPerdeu.destroy()
    limpa_lista_cores_misteriosas()
    deleta_matriz_cor_revelada()
    menu_inicial()

# Deleta o aviso
def deleta_aviso_():
    if labelAviso is not None:
        labelAviso.destroy()

# Deleta o botao verificar
def deleta_botao_verificar():
    global botaoVerificar

    botaoVerificar.destroy()

# Desenha botão voltar
def desenha_botao_voltar():
    # Variavel global usada
    global botaoVoltar

    # Desenha o botão voltar que chama a função voltar_menu_inicial
    botaoVoltar = Button(confgJanela,text="voltar",width=20,height=5,command=voltar_menu_inicial)
    botaoVoltar.place(x=475,y=400)

# Volta para o menu inicial
def voltar_menu_inicial():
    deleta_jogo()
    menu_inicial()

# Deleta o botão voltar
def deleta_botao_voltar():
    # Variavel global usada
    global botaoVoltar

    botaoVoltar.destroy()

# Deleta todo o jogo
def deleta_jogo():
    deleta_conteiner_tentativas()
    deleta_matriz_tentativas()
    deleta_quadrados_dicas()
    deleta_matriz_dicas()
    deleta_botoes_selecionar_cores()
    deleta_aviso_()
    deleta_matriz_cores_escolhidas()
    deleta_botoes_limpar_cores()
    deleta_botao_verificar()
    deleta_botao_voltar()

# Desenha a informação
def informacao():
    deleta_menu()
    desenha_informacao()

# Desenha todo o menu informação
def desenha_informacao():
    desenha_menu_informacao()
    desenha_label_informacao()
    botao_info_volta()

def desenha_menu_informacao():
    # Variavel global usada
    global labelMenuInformacao

    # Desenha o label informação e o posiciona
    labelMenuInformacao = Label(confgJanela, text="Informação", width=42, height=5)
    labelMenuInformacao.place(x=250,y=50)

# Desenha o label das informaçoes do jogo e quem fez o seguinte progrma
def desenha_label_informacao():
    # Variavel global usada
    global labelInformacao

    # Desenha o texto sobre o jogo e quem fez o seguinte programa e o posiciona
    labelInformacao = Label(confgJanela, text="\tO Jogo da senha é um jogo de estratégia em que o jogador deve adivinhar uma combinação secreta de cores em um número limitado de tentativas. O jogo apresenta um painel de cores disponíveis e um painel de feedback para indicar quantas cores foram adivinhadas corretamente e quantas estão na posição correta. Com base nessas informações, o jogador deve ajustar sua estratégia para tentar descobrir a combinação secreta dentro do limite de tentativas. O jogo é uma versão digital do jogo de tabuleiro clássico e oferece uma maneira divertida de testar a habilidade de dedução e pensamento estratégico do jogador.\n\n\tEste programa foi feito por Matheus Marques Eiras no ano de 2023. Cursando em Bacharelado Ciência da Computação - IFPR campus Pinhais.", width=56, height=19,wraplength=350)
    labelInformacao.place(x=200,y=150)

# Botão que volta para  o menu incial
def botao_info_volta():
    # Variavel global usada
    global botaoInfoVolta

    # Desenha o botão voltar que chama a função volta_menu_inicial e o posiciona
    botaoInfoVolta = Button(confgJanela, text="Voltar", width=13, height=3,command=volta_menu_inicial)
    botaoInfoVolta.place(x=350,y=500)

# Volta o menu inicial
def volta_menu_inicial():
    deleta_informacao()
    menu_inicial()

# Deleta o menu informação
def deleta_informacao():
    # Variaveis globais usadas
    global labelMenuInformacao
    global labelInformacao
    global botaoInfoVolta

    labelMenuInformacao.destroy()
    labelInformacao.destroy()
    botaoInfoVolta.destroy()

# Sai do jogo
def sair_jogo():
    janela.quit()

# Desenha o menu do jogo
def desenha_menu():
    linha_cima()
    linha_direita()
    linha_baixo()
    linha_esquerda()
    menu_inicial()


if __name__ == "__main__":
    # Variaveis globais usadas
    # Menu inicial
    labelMenuIncial = None
    botaoNovoJogo = None
    botaoInformacao = None
    botaoSair = None

    # Informação
    labelMenuInformacao = None
    labelInformacao = None
    botaoInfoVolta = None

    # Durante o jogo
    listaCoresMisteriosas = []
    tentativa_atual = None
    listaTentativa = []
    labelAviso = None
    conteinerTentativa = None
    matrizTentativas = None
    quadradosConteiners = None
    matrizDicas = None
    botaoVermelho = None
    botaoVerde = None
    botaoRoxo = None
    botaoRosa = None
    botaoAzul = None
    botaoLaranja = None
    matrizCoresEscolhidas = None
    primeiroBotaoLimpar = None
    segundoBotaoLimpar = None
    terceiroBotaoLimpar = None
    quartoBotaoLimpar = None
    botaoVerificar = None
    botaoVoltar = None

    # Usuario ganhou
    textoGanhou = None
    botaoSairJogoFinal = None
    botaoVoltaMenuGanhou = None
    botaoSairJogoFinal = None
    botaoVoltaMenuGanhou = None

    # Usuário perde
    textoPerdeu = None
    matrizCorRevelada = []
    botaoSairJogoFinal =None
    botaoVoltaMenuPerdeu =None
    botaoSairJogoFinal = None
    botaoVoltaMenuPerdeu = None

    # Define a janela do jogo
    janela = Tk()

    # Configurações da janela

    # Define o tiulo da janela onde o jogo da forca ira se passar
    janela.title("Jogo da senha")
    #tamanho da janela
    janela.geometry("800x600")

    confgJanela = Canvas(janela, width=800, height=600, bg="cyan")


    # Define o layout do jogo
    desenha_menu()

    confgJanela.pack()
    janela.mainloop()