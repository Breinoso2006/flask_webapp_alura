from flask import Flask, flash, render_template, request, redirect, session, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console 

jogo1 = Jogo('Valorant', 'FPS', 'PC')
jogo2 = Jogo('Pokémon Diamond', 'RPG', 'Nintendo DS')
jogo3 = Jogo('The Legend Of Zelda Breath Of The Wild', 'Aventura', 'Nintendo Switch')
lista_de_jogos = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario('Bruno Reinoso', 'breinoso', 'senha')
usuario2 = Usuario('Mariana França', 'mare', 'peixin')
usuario3 = Usuario('Gabriel Lincoln', 'lincoln', 'front')

usuarios = {
    usuario1.nickname : usuario1,
    usuario2.nickname : usuario2,
    usuario3.nickname : usuario3
}

app = Flask(__name__)
app.secret_key = 'secreta'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos = lista_de_jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima = url_for('index')
    return render_template('login.html', titulo = 'Login', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso.')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso.')
    return redirect(url_for('login'))


app.run(debug=True)