# Iremos criar um site, que tenha um botão e um chat
# Os passo serão diferentes do que seria feito no Flet, mas não tem problema


# Começando pelas ferramentas: 
# Flask - pip install flask 
# Socketio - pip install python-socketio/pip install flask-socketio 
# Simple WebSocket - pip install simple-websocket

# Caso necessite de documentação de cada um: 
# • Flask - https://flask.palletsprojects.com/en/2.3.x/
# • Flask no Visual Studio Code - https://code.visualstudio.com/docs/python/tutorial-flask
# • Socketio - https://socket.io/pt-br/docs/v4/

from flask import Flask, render_template # Estrutura para criar site
from flask_socketio import SocketIO, send # Estruturas para criar chat

# Esse é o código em Python que nós vamos utilizar para a criação do site e do chat. Vamos iniciar com a 
# importação das bibliotecas, lembrando que você precisa instalar todas elas para que consiga construir o projeto.

app = Flask(__name__) # Criar o site
app.config["SECRET"] = "aserehe6aberebere3rerubaraba1tequi209neuba" # Chave de segurança, pode ser qualquer coisa, mas escolha algo dificil 
app.config["DEBUG"] = True # Para Testarmos o codigo, no final tiramos
socketio = SocketIO(app, cors_allowed_origins="*") # Cria uma conexão entre máquinas diferentes que estão no mesmo site 

# Logo abaixo, vamos fazer a criação do site, vamos inserir uma chave de segurança, o debug para fazer o teste do código e por fim vamos fazer a conexão entre as máquinas que estão no site utilizando o chat.

# Aqui nós vamos definir quando a função gerenciar_mensagens vai ser executada. Ela vai ser acionada, quando o evento message acontecer, que é o evento que temos dentro do nosso código html.
# Nessa função nós vamos printar (exibir) a mensagem e fazer o envio da mensagem para todas as pessoas
# que estão conectadas no site. Então sempre que essa evento acontecer nós vamos executar essa função para o envio das mensagens.
@socketio.on("message") # Define a funcao abaixo vai ser adicionada quando o evento de "message" ocorrer
def gerencia_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True) # Envia mensagem para todo mundo conectado no site

# Nessa parte estamos de fato criando a página, o Route é o caminho do nosso “aplicativo”, então temos a página inicial onde vamos utilizar 2 templates na aula.
# Vamos utilizar o homepage.html e o index.html, que são o mesmo arquivo, mas o último já tem alguns códigos em HTML e CSS para melhorar o visual da página.
# Por fim vamos definir que o app vai rodar no servidor local, ou seja, na internet em que o seu computador está conectado
@app.route("/") # Cria uma pagina do site
def home():
    return render_template("index.html") # Essa página vai carregar este arquivo html que está aqui

if __name__ == "__main__":
    socketio.run(app, host='localhost') # Define que o app vai rodar no seu servidor local, ou seja na internet que o computador está conectado

