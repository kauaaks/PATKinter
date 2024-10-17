from tkinter import *
from tkinter import ttk

def calculate():
    try:
        value = float(milhas.get())  
        km.set(float(value) * 1.6093)
    except ValueError:  # Se ocorrer um erro na conversão
        pass

#janela e titulo
root = Tk()
root.title("milhas para KM")

# Configurando o layout da janela
mainframe = ttk.Frame(root, padding="3 3 12 12")  # Cria um Frame com padding
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # Posiciona o Frame na grade
root.columnconfigure(0, weight=1)  # Configura a coluna para se ajustar ao redimensionar
root.rowconfigure(0, weight=1)  # Configura a linha para se ajustar ao redimensionar

milhas = StringVar()
milhas_entry = ttk.Entry(mainframe, width=7, textvariable=milhas)
milhas_entry.grid(column=2, row=1, sticky=(W, E))

km = StringVar()  # Cria uma variável para o resultado em metros
ttk.Label(mainframe, textvariable=km).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="calcular", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Milhas").grid(column=3, row=1, sticky=W)  # Rótulo para a entrada em pés
ttk.Label(mainframe, text="equivalente à:").grid(column=1, row=2, sticky=E)  # Rótulo informando o que é mostrado
ttk.Label(mainframe, text="Quilômetros").grid(column=3, row=2, sticky=W)  # Rótulo para a saída em metros

# Configuração de estilo
for child in mainframe.winfo_children():  # Para cada widget filho do mainframe
    child.grid_configure(padx=5, pady=5)  # Aplica padding aos widgets

milhas_entry.focus()  # Define o foco no campo de entrada para facilitar a digitação
root.bind("<Return>", calculate)  # Associa a tecla Enter à função calculate

root.mainloop()  # Inicia o loop principal da aplicação
