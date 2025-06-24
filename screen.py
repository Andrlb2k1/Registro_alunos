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
global imagem, imagem_string, l_imagem

app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text=" Sistema de registro de alunos", width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

# Criando os campos de entrada --------------------------------------
l_nome = Label(frame_details, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_details, width=30, justify='left', relief='solid')
e_nome.place(x=7, y=40)

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
c_sex['values'] = ('M', 'F', 'T')
c_sex.place(x=130, y=160)

janela.mainloop()