# Importando as dependências do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Importando o pillow
from PIL import ImageTk, Image

# Importando o tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando o "main"
from main import *

# Cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# Crianndo a janela
janela = Tk()
janela.title("")
janela.geometry('810x535')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando os frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_buttons = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_buttons.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_table = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_table.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

# Trabalhando no frame "logo" -------------------------------------
global image, image_string, l_image

app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Sistema de registro de alunos", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

# Abrindo a imagem
image = Image.open('logo.png')
image = image.resize((130,130))
image = ImageTk.PhotoImage(image)
l_image = Label(frame_details, image=image, bg=co1, fg=co4)
l_image.place(x=390, y=10)

# Criando funções para o CRUD ------------------------------------------
# Função para adicionar aluno
def add():
    global image, image_string, l_image

    name = e_name.get()
    email = e_email.get()
    telephone = e_telephone.get()
    sex = c_sex.get()
    date = birth_date.get()
    address = e_address.get()
    course = c_course.get()
    img = image_string

    list = [name, email, telephone, sex, date, address, course, img]

    # Verificando se a lista contém valor vazio
    for i in list:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    # Registrando os valores
    register_system.register_student(list)

    # Limpando os campos de entrada
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_telephone.delete(0, END)
    c_sex.delete(0, END)
    birth_date.delete(0, END)
    e_address.delete(0, END)
    c_course.delete(0, END)

    # Mostrando os valores na tabela
    show_students()

# Função para procurar aluno
def search():
    global image, image_string, l_image

    # Obtendo o id
    id_student = int(e_search.get())

    # Procurando o aluno
    data = register_system.search_student(id_student)

    # Limpando os campos de entrada
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_telephone.delete(0, END)
    c_sex.delete(0, END)
    birth_date.delete(0, END)
    e_address.delete(0, END)
    c_course.delete(0, END)

    # Inserindo dados nos campos de entrada
    e_name.insert(END, data[1])
    e_email.insert(END, data[2])
    e_telephone.insert(END, data[3])
    c_sex.insert(END, data[4])
    birth_date.insert(END, data[5])
    e_address.insert(END, data[6])
    c_course.insert(END, data[7])

    image = data[8]
    image_string = image

    image = Image.open(image)
    image = image.resize((130,130))
    image = ImageTk.PhotoImage(image)

    l_image = Label(frame_details, image=image, bg=co1, fg=co4)
    l_image.place(x=390, y=10)

# Função para atualizar aluno
def update():
    global image, image_string, l_image

    # Obtendo o id
    id_student = int(e_search.get())

    name = e_name.get()
    email = e_email.get()
    telephone = e_telephone.get()
    sex = c_sex.get()
    date = birth_date.get()
    address = e_address.get()
    course = c_course.get()
    img = image_string

    list = [name, email, telephone, sex, date, address, course, img, id_student]

    # Verificando se a lista contém valor vazio
    for i in list:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    # Atualizando os valores
    register_system.update_student(list)

    # Limpando os campos de entrada
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_telephone.delete(0, END)
    c_sex.delete(0, END)
    birth_date.delete(0, END)
    e_address.delete(0, END)
    c_course.delete(0, END)

    # Abrindo a imagem
    image = Image.open('logo.png')
    image = image.resize((130,130))
    image = ImageTk.PhotoImage(image)

    l_image = Label(frame_details, image=image, bg=co1, fg=co4)
    l_image.place(x=390, y=10)

    # Mostrando os valores na tabela
    show_students()

# Função para deletar aluno
def delete():
    global image, image_string, l_image

    # Obtendo o id
    id_student = int(e_search.get())

    # Deletando o aluno
    register_system.delete_student(id_student)

    # Limpando os campos de entrada
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_telephone.delete(0, END)
    c_sex.delete(0, END)
    birth_date.delete(0, END)
    e_address.delete(0, END)
    c_course.delete(0, END)

    e_search.delete(0, END)

    # Abrindo a imagem
    image = Image.open('logo.png')
    image = image.resize((130,130))
    image = ImageTk.PhotoImage(image)

    l_image = Label(frame_details, image=image, bg=co1, fg=co4)
    l_image.place(x=390, y=10)

    # Mostrando os valores na tabela
    show_students()

# Criando os campos de entrada --------------------------------------
l_name = Label(frame_details, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_name.place(x=4, y=10)
e_name = Entry(frame_details, width=30, justify='left', relief='solid')
e_name.place(x=7, y=40)

l_email = Label(frame_details, text="Email *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_telephone = Label(frame_details, text="Telefone *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_telephone.place(x=4, y=130)
e_telephone = Entry(frame_details, width=15, justify='left', relief='solid')
e_telephone.place(x=7, y=160)

l_sex = Label(frame_details, text="Sexo *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sex.place(x=127, y=130)
c_sex = ttk.Combobox(frame_details, width=7, font=('Ivy 8 bold'), justify='center')
c_sex['values'] = ('M', 'F', 'X')
c_sex.place(x=130, y=160)

l_birth_date = Label(frame_details, text="Data de nascimento *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_birth_date.place(x=220, y=10)
birth_date = DateEntry(frame_details, width=18, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2023)
birth_date.place(x=224, y=40)

l_address = Label(frame_details, text="Endereço *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_address.place(x=220, y=70)
e_address = Entry(frame_details, width=15, justify='left', relief='solid')
e_address.place(x=224, y=100)

courses = ['Engenharia', 'Medicina', 'Sociais', 'Informática', 'Outro']

l_course = Label(frame_details, text="Cursos *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_course.place(x=220, y=130)
c_course = ttk.Combobox(frame_details, width=20, font=('Ivy 8 bold'), justify='center')
c_course['values'] = (courses)
c_course.place(x=224, y=160)

# Função para escolher imagem
def choose_image():
    global image, image_string, l_image

    image = fd.askopenfilename()
    image_string = image

    image = Image.open(image)
    image = image.resize((130,130))
    image = ImageTk.PhotoImage(image)
    l_image = Label(frame_details, image=image, bg=co1, fg=co4)
    l_image.place(x=390, y=10)

    load_button['text'] = 'Trocar de foto'.upper()

load_button = Button(frame_details, command=choose_image, text='Carregar foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
load_button.place(x=390, y=160)

# Tabela de alunos
def show_students():
    list_header = ['Id', 'Nome', 'Email', 'Telefone', 'Sexo', 'Data', 'Endereço', 'Curso']

    df_list = register_system.view_all_students()

    tree_student = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show='headings')

    vsb = ttk.Scrollbar(frame_table, orient='vertical', command=tree_student.yview)

    hsb = ttk.Scrollbar(frame_table, orient='horizontal', command=tree_student.xview)

    tree_student.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_student.grid(column=0, row=1, sticky=NSEW)
    vsb.grid(column=1, row=1, sticky=NS)
    hsb.grid(column=0, row=2, sticky=EW)
    frame_table.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
    h = [40, 150, 150, 70, 70, 70, 120, 100, 100]
    n = 0

    for col in list_header:
        tree_student.heading(col, text=col.title(), anchor=NW)
        tree_student.column(col, width=h[n], anchor=hd[n])

        n+=1
    
    for item in df_list:
        tree_student.insert('', 'end', values=item)

# Procurar aluno
frame_search = Frame(frame_buttons, width=40, height=55, bg=co1, relief=RAISED)
frame_search.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_search = Label(frame_search, text=" Procurar aluno [Entra ID]", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_search.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_search = Entry(frame_search, width=5, justify='center', relief='solid', font=('Ivy 10'))
e_search.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

search_button = Button(frame_search, command=search, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co1, fg=co0)
search_button.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# Botões ----------------------------------------------
app_img_add = Image.open('add.png')
app_img_add = app_img_add.resize((25,25))
app_img_add = ImageTk.PhotoImage(app_img_add)
app_add = Button(frame_buttons, command=add, image=app_img_add, relief=GROOVE, text=' Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_add.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_update = Image.open('update.png')
app_img_update = app_img_update.resize((25,25))
app_img_update = ImageTk.PhotoImage(app_img_update)
app_update = Button(frame_buttons, command=update, image=app_img_update, relief=GROOVE, text=' Atualizar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_update.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_delete = Image.open('delete.png')
app_img_delete = app_img_delete.resize((25,25))
app_img_delete = ImageTk.PhotoImage(app_img_delete)
app_delete = Button(frame_buttons, command=delete, image=app_img_delete, relief=GROOVE, text=' Deletar', width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_delete.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# Linha separatória
l_line = Label(frame_buttons, relief=GROOVE, text='h', width=1, height=123, anchor=NW, font=('Ivy 1'), bg=co1, fg=co1)
l_line.place(x=235, y=15)

# Chamar a tabela
show_students()

janela.mainloop()