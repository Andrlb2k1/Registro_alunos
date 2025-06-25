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
        data = self.c.fetchall()
        
        return data

    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        data = self.c.fetchone()
        
        return data

    def update_student(self, nova_valores):
        query = "UPDATE estudantes SET nome=?, email=?, telefone=?, sexo=?, data_nascimento=?, endereco=?, curso=?, imagem=? WHERE id=?"
        self.c.execute(query, nova_valores)
        self.conn.commit()

        # Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'O(A) estudante com ID:{nova_valores[8]} foi atualizado(a)!')
    
    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()

        # Mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'O(a) estudante com ID:{id} foi deletado(a)!')

# Criando uma instância do sistema de registro
register_system = SistemaDeRegistro()

# Informações
# estudante = ('João', 'joao@gmail.com', '12345678', 'M', '12/11/2003', 'Brasil, Paraná', 'Informática', 'imagem2.png')
# register_system.register_student(estudante)

# Ver os estudantes
# todos_alunos = register_system.view_all_students()

# Procurar aluno
# aluno = register_system.search_student(2)

# Atualizar aluno
# estudante = ('João', 'joao@gmail.com', '87654321', 'M', '11/11/2003', 'Brasil, Paraná', 'Informática', 'imagem2.png', 2)
# aluno = register_system.update_student(estudante)

# Deletar aluno
# register_system.delete_student(2)