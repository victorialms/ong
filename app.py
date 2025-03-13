from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT")
    )

# Endereçamento da página principal:
@app.route('/')
def index():
    return render_template('home/index.html')


# Endereçamento de outras páginas que não utilizam conexão com o banco de dados (quem somos, pix, transparencia, etc)
@app.route('/transparency')
def transparency():
    return render_template('/transparencia/transparency.html')

@app.route('/pix')
def pix():
    return render_template('/pix/ONGPIX_HTML.html')

@app.route('/pix2')
def pix2():
    return render_template('/pix/ONGPIX2_HTML.html')


# Endereçamento da página principal do sistema
@app.route('/sistema')
def sistema():
    return render_template('/sistema/SYSTEM_HTML.html')

@app.route('/sistema2')
def sistema2():
    return render_template('/sistema/SYSTEM2_HTML.html')

@app.route('/parceiros')
def parceiros():
    return render_template('/sistema/PARTNERS_HTML.html')

@app.route('/despesas')
def despesas():
    return render_template('/sistema/EXPENSES_HTML.html')

@app.route('/voluntarios')
def voluntarios():
    return render_template('/sistema/VOLUNTEERS_HTML.html')


# Parceiros
@app.route('/cadastrar_parceiro', methods=['GET', 'POST'])
def cadastrar_parceiro():
    if request.method == 'POST':
        nome = request.form['nome_parceiro']
        data = request.form['data_parceiro']
        descricao = request.form['descricao_parceiro']

        con = get_db_connection()
        cursor = con.cursor()

        cursor.execute('''INSERT INTO parceiros (nome_parceiro, data_parceiro, descricao_parceiro) 
                          VALUES (%s, %s, %s)''', (nome, data, descricao))
        con.commit()

        cursor.close()
        con.close()

        return redirect(url_for('exibir_parceiro'))
    
    return render_template('sistema/PARTNERS2_HTML.html')

@app.route('/exibir_parceiro', methods=['GET', 'POST'])
def exibir_parceiro():
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
    
    search_name = request.args.get('search_name', '')  # Pega o parâmetro de pesquisa da URL (Para filtar durante exibição)
    
    if search_name:
        cursor.execute("SELECT * FROM parceiros WHERE nome_parceiro LIKE %s", ('%' + search_name + '%',))
    else:
        cursor.execute('SELECT * FROM parceiros')
    
    parceiros = cursor.fetchall()
    
    cursor.close()
    con.close()
    
    return render_template('sistema/PARTNERS3_HTML.html', parceiros=parceiros)

@app.route('/excluir_parceiro/<int:id_parceiro>', methods=['POST'])
def excluir_parceiro(id_parceiro):
    con = get_db_connection()
    cursor = con.cursor()
    
    cursor.execute('DELETE FROM parceiros WHERE id_parceiro = %s', (id_parceiro,))
    con.commit()
    
    cursor.close()
    con.close()
    
    return redirect(url_for('exibir_parceiro'))

@app.route('/editar_parceiro/<int:id_parceiro>', methods=['GET', 'POST'])
def editar_parceiro(id_parceiro):
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)

    if request.method == 'POST':
        nome = request.form['nome_parceiro']
        data = request.form['data_parceiro']
        descricao = request.form['descricao_parceiro']

        cursor.execute('''
            UPDATE parceiros
            SET nome_parceiro = %s, data_parceiro = %s, descricao_parceiro = %s
            WHERE id_parceiro = %s
        ''', (nome, data, descricao, id_parceiro))
        
        con.commit()
        cursor.close()
        con.close()

        return redirect(url_for('exibir_parceiro'))

    cursor.execute('SELECT * FROM parceiros WHERE id_parceiro = %s', (id_parceiro,))
    parceiro = cursor.fetchone()
    
    cursor.close()
    con.close()

    return render_template('sistema/PARTNERS4_HTML.html', parceiro=parceiro)


# Despesas
@app.route('/cadastrar_despesa', methods=['GET', 'POST'])
def cadastrar_despesa():
    if request.method == 'POST':
        nome_despesa = request.form['nome_despesa']
        data_despesa = request.form['data_despesa']
        descricao_despesa = request.form['descricao_despesa']
        valor_despesa = request.form['valor_despesa']

        con = get_db_connection()
        cursor = con.cursor()

        cursor.execute('''INSERT INTO despesas (nome_despesa, data_despesa, descricao_despesa, valor_despesa) 
                          VALUES (%s, %s, %s, %s)''', (nome_despesa, data_despesa, descricao_despesa, valor_despesa))
        con.commit()

        cursor.close()
        con.close()

        return redirect(url_for('exibir_despesa'))

    return render_template('sistema/EXPENSES2_HTML.html')

@app.route('/exibir_despesa', methods=['GET'])
def exibir_despesa():
    search_name = request.args.get('search_name', '')  # Obtém o parâmetro de pesquisa

    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
    
    if search_name:
        # Se houver um nome para filtrar, aplicamos o filtro na consulta
        cursor.execute('SELECT * FROM despesas WHERE nome_despesa LIKE %s', ('%' + search_name + '%',))
    else:
        # Se não houver filtro, trazemos todas as despesas
        cursor.execute('SELECT * FROM despesas')
    
    despesas = cursor.fetchall()
    
    cursor.close()
    con.close()
    
    return render_template('sistema/EXPENSES3_HTML.html', despesas=despesas)

@app.route('/excluir_despesa/<int:id_despesa>', methods=['POST'])
def excluir_despesa(id_despesa):
    con = get_db_connection()
    cursor = con.cursor()
    
    cursor.execute('DELETE FROM despesas WHERE id_despesa = %s', (id_despesa,))
    con.commit()
    
    cursor.close()
    con.close()
    
    return redirect(url_for('exibir_despesa'))

@app.route('/editar_despesa/<int:id_despesa>', methods=['GET', 'POST'])
def editar_despesa(id_despesa):
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)

    if request.method == 'POST':
        nome_despesa = request.form['nome_despesa']
        data_despesa = request.form['data_despesa']
        descricao_despesa = request.form['descricao_despesa']
        valor_despesa = request.form['valor_despesa']

        cursor.execute('''
            UPDATE despesas
            SET nome_despesa = %s, data_despesa = %s, descricao_despesa = %s, valor_despesa = %s
            WHERE id_despesa = %s
        ''', (nome_despesa, data_despesa, descricao_despesa, valor_despesa, id_despesa))
        
        con.commit()
        cursor.close()
        con.close()

        return redirect(url_for('exibir_despesa'))

    cursor.execute('SELECT * FROM despesas WHERE id_despesa = %s', (id_despesa,))
    despesa = cursor.fetchone()
    
    cursor.close()
    con.close()

    return render_template('sistema/EXPENSES4_HTML.html', despesa=despesa)


# Voluntários
@app.route('/cadastrar_voluntario', methods=['GET', 'POST'])
def cadastrar_voluntario():
    if request.method == 'POST':
        nome_voluntario = request.form['nome_voluntario']
        data_voluntario = request.form['data_voluntario']
        tipo_voluntario = request.form['tipo_voluntario']
        telefone_voluntario = request.form['telefone_voluntario']

        con = get_db_connection()
        cursor = con.cursor()

        cursor.execute('''INSERT INTO voluntarios (nome_voluntario, data_voluntario, tipo_voluntario, telefone_voluntario) 
                          VALUES (%s, %s, %s, %s)''', 
                       (nome_voluntario, data_voluntario, tipo_voluntario, telefone_voluntario))
        con.commit()

        cursor.close()
        con.close()

        return redirect(url_for('exibir_voluntario'))

    return render_template('sistema/VOLUNTEERS2_HTML.html')

@app.route('/exibir_voluntario', methods=['GET'])
def exibir_voluntario():
    search_name = request.args.get('search_name', '')  # Obtém o parâmetro de pesquisa de nome
    tipo_voluntario = request.args.get('tipo_voluntario', '')  # Obtém o parâmetro de filtro de tipo de voluntário

    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
    
    query = 'SELECT * FROM voluntarios WHERE 1=1'  # Começamos com uma consulta básica que retorna todos os voluntários
    params = []

    if search_name:
        query += ' AND nome_voluntario LIKE %s'
        params.append('%' + search_name + '%')
    
    if tipo_voluntario:
        query += ' AND tipo_voluntario = %s'
        params.append(tipo_voluntario)
    
    cursor.execute(query, params)
    voluntarios = cursor.fetchall()
    
    cursor.close()
    con.close()
    
    return render_template('sistema/VOLUNTEERS3_HTML.html', voluntarios=voluntarios)

@app.route('/excluir_voluntario/<int:id_voluntario>', methods=['POST'])
def excluir_voluntario(id_voluntario):
    con = get_db_connection()
    cursor = con.cursor()
    
    cursor.execute('DELETE FROM voluntarios WHERE id_voluntario = %s', (id_voluntario,))
    con.commit()
    
    cursor.close()
    con.close()
    
    return redirect(url_for('exibir_voluntario'))

@app.route('/editar_voluntario/<int:id_voluntario>', methods=['GET', 'POST'])
def editar_voluntario(id_voluntario):
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)

    if request.method == 'POST':
        nome_voluntario = request.form['nome_voluntario']
        data_voluntario = request.form['data_voluntario']
        tipo_voluntario = request.form['tipo_voluntario']
        telefone_voluntario = request.form['telefone_voluntario']

        cursor.execute('''
            UPDATE voluntarios
            SET nome_voluntario = %s, data_voluntario = %s, tipo_voluntario = %s, telefone_voluntario = %s
            WHERE id_voluntario = %s
        ''', (nome_voluntario, data_voluntario, tipo_voluntario, telefone_voluntario, id_voluntario))
        
        con.commit()
        cursor.close()
        con.close()

        return redirect(url_for('exibir_voluntario'))

    cursor.execute('SELECT * FROM voluntarios WHERE id_voluntario = %s', (id_voluntario,))
    voluntario = cursor.fetchone()
    
    cursor.close()
    con.close()

    return render_template('sistema/VOLUNTEERS4_HTML.html', voluntario=voluntario)


if __name__ == '__main__':
    app.run()
