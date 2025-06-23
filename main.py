import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            telefone TEXT NOT NULL,
                            sexo TEXT NOT NULL,
                            data_nascimento TEXT NOT NULL,
                            endereco TEXT NOT NULL,
                            curso TEXT NOT NULL,
                            imagem TEXT NOT NULL)''')
    
    def register_student(self, estudantes):
        self.c.execute("INSERT INTO estudantes(nome, email, telefone, sexo, data_nascimento, endereco, curso, imagem) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", 
            (estudantes))
        self.conn.commit()

        # Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registro feito com sucesso!')

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados = self.c.fetchall()

        for i in dados:
            print(f'Id: {i[0]} | Nome: {i[1]} | Email: {i[2]} | Telefone: {i[3]} | Sexo: {i[4]} | Dta de nascimento: {i[5]} | Endereço: {i[6]} | Curso: {i[7]} | Imagem: {i[8]}')

    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id))
        dados = self.c.fetchone()
        
        print(f'Id: {dados[0]} | Nome: {dados[1]} | Email: {dados[2]} | Telefone: {dados[3]} | Sexo: {dados[4]} | Dta de nascimento: {dados[5]} | Endereço: {dados[6]} | Curso: {dados[7]} | Imagem: {dados[8]}')

    def update_student(self, nova_valores):
        query = "UPDATE estudantes SET nome=?, email=?, telefone=?, sexo=?, data_nascimento=?, endereco=?, curso=?, imagem=? WHERE id=?"
        self.c.execute(query, nova_valores)
        self.conn.commit()

        # Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'O(A) estudante com ID:{nova_valores[8]} foi atualizado!')
    
    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()

        # Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'O(a) estudante com ID:{id} foi deletado!')

# Criando uma instância do sistema de registro
sistema_de_registro = SistemaDeRegistro()