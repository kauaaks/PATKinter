import string
a = list(string.ascii_lowercase)
import random
from tkinter import *
from tkinter import ttk

def funcao(*args):  
    numero = ''.join(str(i) for i in range(10))
    caracteres = ''.join(chr(i) for i in range(128))
    juntar_numeros = caracteres + numero
    juntando_tudo = list(juntar_numeros)
    random.shuffle(juntando_tudo)
    embaralhar = ''.join(juntando_tudo[:8])
    senha.set(embaralhar)
    

#janela e titulo
root = Tk()
root.title("criptografia")

# Configurando o layout da janela
mainframe = ttk.Frame(root, padding="3 3 12 12")  # Cria um Frame com padding
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # Posiciona o Frame na grade
root.columnconfigure(0, weight=1)  # Configura a coluna para se ajustar ao redimensionar
root.rowconfigure(0, weight=1)  # Configura a linha para se ajustar ao redimensionar

ttk.Button(mainframe, text="gerar", command=funcao).grid(column=3, row=3, sticky=W)


ttk.Label(mainframe, text="senha:").grid(column=1, row=2, sticky=E)  # Rótulo informando o que é mostrado
senha = StringVar()

ttk.Label(mainframe, textvariable=senha).grid(column=2, row=2, sticky=(W, E))
# Configuração de estilo
for child in mainframe.winfo_children():  # Para cada widget filho do mainframe
    child.grid_configure(padx=5, pady=5)  # Aplica padding aos widgets

  
root.bind("<Return>", funcao)  # Associa a tecla Enter à função calculate

root.mainloop()  # Inicia o loop principal da aplicação
