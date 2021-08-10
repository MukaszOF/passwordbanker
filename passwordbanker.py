import sqlite3
import os

CHAVE_MESTRA = "free"

senha= input("Insira sua senha Mestra: ")
if senha != CHAVE_MESTRA:
    print("Senha Inválida! Encerrando...")
    exit()

conn = sqlite3.connect('coding.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print("********************************")
    print("*  [1]: Enter New Password     *")
    print("*  [2]: List Saved Services    *")
    print("*  [3]: Recover a Password     *")
    print("*  [4]: Exit.                  *")
    print("*  🐍  Developed by Mukasz     *")
    print("********************************")

def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("Serviço não cadastrado (use '2' para verificar os serviços).")
    else:
        for user in cursor.fetchall():
            print(user)

def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password) 
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)


while True:
    menu()
    op = input("O que deseja fazer? ")
    if op not in ['1', '2', '3', '4']:
        print("Opção invalida!")
        continue

    if op == '4':
        break

    if op == '1':
        service = input('Qual o nome do serviço? : ')
        username = input('Qual o nome de Usuario? : ')
        password = input('Qual a senha? : ')
        insert_password(service, username, password)

    if op == '2':
        show_services()

    if op == '3':
        service = input('Qual o serviço para o qual quer a senha? : ')
        get_password(service)
conn.close()