from flask import Flask, flash, render_template, request, redirect, session

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console 

jogo1 = Jogo('Valorant', 'FPS', 'PC')
jogo2 = Jogo('Pokémon Diamond', 'RPG', 'Nintendo DS')
jogo3 = Jogo('The Legend Of Zelda Breath Of The Wild', 'Aventura', 'Nintendo Switch')
lista_de_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'secreta'

@app.route('/')
def inicio():
    return render_template('lista.html', titulo='Jogos', jogos = lista_de_jogos)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo = 'Login')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso.')
        return redirect('/')
    else:
        flash('Usuário não logado.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso.')
    return redirect('/')


app.run(debug=True)