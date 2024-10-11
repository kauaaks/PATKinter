from tkinter import *  # Importa todos os componentes da biblioteca tkinter
from tkinter import ttk  # Importa o módulo ttk para widgets com estilo moderno

def calculate(*args):  # Função para fazer a conversão
    try:
        value = float(feet.get())  # Tenta obter o valor em pés e converter para float
        # Converte pés para metros e define o valor formatado em 4 casas decimais
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:  # Se ocorrer um erro na conversão
        pass  # Ignora o erro

# Criando a janela principal
root = Tk()  # Cria a janela principal do aplicativo
root.title("pés para metros")  # Define o título da janela

# Configurando o layout da janela
mainframe = ttk.Frame(root, padding="3 3 12 12")  # Cria um Frame com padding
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # Posiciona o Frame na grade
root.columnconfigure(0, weight=1)  # Configura a coluna para se ajustar ao redimensionar
root.rowconfigure(0, weight=1)  # Configura a linha para se ajustar ao redimensionar

# Variável para armazenar o valor em pés
feet = StringVar()  # Cria uma variável para a entrada em pés
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)  # Campo de entrada para pés
feet_entry.grid(column=2, row=1, sticky=(W, E))  # Posiciona o campo na grade

# Variável para armazenar o resultado em metros
meters = StringVar()  # Cria uma variável para o resultado em metros
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))  # Exibe o resultado

# Botão para calcular a conversão
ttk.Button(mainframe, text="calcular", command=calculate).grid(column=3, row=3, sticky=W)  # Botão que chama a função calculate

# Rótulos informativos
ttk.Label(mainframe, text="Pés").grid(column=3, row=1, sticky=W)  # Rótulo para a entrada em pés
ttk.Label(mainframe, text="equivalente à:").grid(column=1, row=2, sticky=E)  # Rótulo informando o que é mostrado
ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=W)  # Rótulo para a saída em metros

# Configuração de estilo
for child in mainframe.winfo_children():  # Para cada widget filho do mainframe
    child.grid_configure(padx=5, pady=5)  # Aplica padding aos widgets

feet_entry.focus()  # Define o foco no campo de entrada para facilitar a digitação
root.bind("<Return>", calculate)  # Associa a tecla Enter à função calculate

root.mainloop()  # Inicia o loop principal da aplicação
