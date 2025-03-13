# Desenvolvimento de site e sistema para a ONG Semeando Alegria
## Trabalho extensionista da disciplina "Desenvolvimento Web 3".

![alt text](https://i.imgur.com/107cHr2.png)

# Sobre o projeto:
## Objetivo:
Esse trabalho foi desenvolvido como parte das atividades de extensão promovidas na disciplina de "Desenvolvimento Web 3" da Universidade LaSalle. 
Criamos um ambiente onde é facil consultar as ações realizadas pela ONG, além do desenvolvimento de um sistema interno que permite cadastrar, editar e visualizar
os parceiros, voluntários e as despesas da ONG.

## 🛠️ Tecnoloias Utilizadas:
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Banco de dados: MySQL

## ✒️ Autores

* **Michel Soares** - [GitHub](https://github.com/UNI-MichelSoares)
* **Isabella Rocha** - [GitHub](https://github.com/Iswb04)
* **Mariana Machado** - [GitHub](https://github.com/marianamachaddo)
* **Rodrigo Veiga** - [GitHub](https://github.com/RodrigoSoaresVeiga)
* **Victoria Lacerda** - [GitHub](https://github.com/victorialms)

# 📚 Instruções de Uso:

### Clone o repositório:
  ```sh
  git clone https://github.com/UNI-MichelSoares/ONG-Traballho-Web3
  ```
### Instale as dependências:
  ```sh
  pip install requirements.txt
  ```
### Configure corretamente o setub_db.py:
  ```sh
  con = mysql.connector.connect(
    host="NOME DO HOST",
    user="NOME DO USUARIO",
    passwd="SENHA DO USUARIO",
  )
  ```
### Execute o arquivo setup_db.py:
Cria o banco de dados e suas tabelas caso elas não existam. Importante guardar os dados de onde ela foi criada para o próximo passo.
  ```sh
  python setup_db.py
  ```
### Crie e configure o arquivo .env:
  ```sh
  DB_HOST= seu host
  DB_USER= seu usuario
  DB_PASSWORD= sua senha
  DB_NAME= seu db
  DB_PORT= sua porta
  ```
### Execute o arquivo app.py:
  ```sh
  python app.py
  ```
### Navegue pelo site através do seu link local, fornecido ao executar o arquivo 'app.py'.
