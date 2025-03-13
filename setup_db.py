import mysql.connector

con = mysql.connector.connect(
    host="HOST",
    user="USER",
    passwd="PASSWORD",
)

cursor = con.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS semeando_alegria')
cursor.execute('USE semeando_alegria')

cursor.execute('''CREATE TABLE IF NOT EXISTS parceiros(
    id_parceiro INT AUTO_INCREMENT PRIMARY KEY,
    nome_parceiro VARCHAR(255) NOT NULL,
    data_parceiro DATE NOT NULL,
    descricao_parceiro VARCHAR(255)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS despesas(
    id_despesa INT AUTO_INCREMENT PRIMARY KEY,
    nome_despesa VARCHAR(255) NOT NULL,
    valor_despesa DECIMAL(10, 2) NOT NULL,
    data_despesa DATE NOT NULL,
    descricao_despesa VARCHAR(255)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS voluntarios(
    id_voluntario INT AUTO_INCREMENT PRIMARY KEY,
    nome_voluntario VARCHAR(255) NOT NULL,
    data_voluntario DATE NOT NULL,
    tipo_voluntario ENUM('Marmitas', 'Divinavó', 'Crianças'),
    telefone_voluntario VARCHAR(15) NOT NULL
)''')