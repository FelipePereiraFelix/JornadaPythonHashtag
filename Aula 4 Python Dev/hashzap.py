# O que iremos aprender hoje é como fazer um site e um Chat através do Python
# Os passos são os seguintes: 

# Tela Inicial
 # Titulo -> Hashzap
 # Botao -> Iniciar Chat
   # quando clicar no botao ->
   # Abrir um popup\modal\alerta
     # Titulo -> Bem vindo ao hashzap
     # Caixa de Texto -> Escreva seu nome no chat
     # Botao -> Entrar no chat
     # quando clicar no botao
     # sumir com o titulo
     # sumir com o campo de enviar mensagem -> Digite sua...
       # carregar o chat
       # carregar o campo de enviar mensagem -> Digite sua...
       # botao Enviar
         #quando clicar no botao enviar
         # enviar a mensagem
         # limpar a caixa de mensagem

# Ferramentas que utilizaremos na aula de hoje é o Flet
# Devemos instalar o Flet 
# Porque de usar o Flet, porque ele serve para fazer o site, ele servira para fazer tanto o Front quanto o Back End
# Como sempre faremos para instalar -> pip install flet (Abra um novo terminal e digite isto)

# Flet
# A partir daqui o código começa
# Importe o Flet
# Passo 1: Criar uma função principal para rodar seu aplicativo
import flet as ft 

def main(pagina):
    # Colocar o que está função vai fazer 
    # Titulo 
    titulo = ft.Text("Hashzap")
    pagina.ad(titulo)

# Eu percebi que este código não está completo, e foi usado com Flask e não Flet o da apostila, então deixarei este para outro dia