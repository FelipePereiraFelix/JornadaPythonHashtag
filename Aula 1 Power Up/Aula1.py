#Passo 1: Abrir o sistema da empresa
#abrir opera gx
import pyautogui
import time
import pandas


#adicionar intervalo de tempo para poder entrar no site
pyautogui.PAUSE = 0.5
#apertar tecla win
pyautogui.press("win")

#digitar texto do opera
#Escolhi por fazer colocar no Opera pois foi o mais funcional para mim
pyautogui.write("opera")
pyautogui.press("enter")

#entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#pedir para o computador esperar 3 segundos para proxima parte
time.sleep(3)

#Passo 2: Fazer login
pyautogui.click(x=698, y=392)
pyautogui.write("meuemail@gmail.com")
pyautogui.press("tab")

#Senha
pyautogui.write("alanzokacabecudo")

#Enter na página
pyautogui.press("tab")
pyautogui.press("enter")

#Passo 3: Importar a base de dados do produto
#Variavel
tabela = pandas.read_csv("produtos.csv")
print(tabela)

#Para vizualizar tabela print(tabela)
time.sleep(2)

#Passo 4: Cadastrar um produto
#Vamos percorrer as linhas aqui

for linha in tabela.index:
    pyautogui.click(x=685, y=284) #Clica no primeiro campo

    #Codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #Preco Unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #Obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
     pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
#numero positivo para cima e numero negativo para baixo 
#Qual o problema nessa desgraça


#Passo 5 repetir o processo 4 até acabar os processos so que para isso você deverá reformular todo código da parte 4
#Passo 5 resolvido