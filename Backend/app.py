from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Defina uma chave secreta para o Flask

# Função para conectar ao MySQL
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',    # Endereço do servidor MySQL (geralmente 'localhost')
        user='root',         # Substitua pelo seu usuário MySQL
        password='svsss99',  # Substitua pela sua senha MySQL
        database='cafeteria' # Nome do banco de dados
    )

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Conectar ao banco de dados
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()

        if user:
            return redirect(url_for('dashboard'))  # Redireciona para a página do painel
        else:
            flash('Nome de usuário ou senha inválidos', 'danger')  # Exibe erro

        cursor.close()
        connection.close()

    return render_template('login.html')

# Página do painel de controle (após login bem-sucedido)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

