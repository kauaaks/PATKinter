from tkinter import *  
from tkinter import ttk  

def calcular(*args):  
    try:
        altura_valor = float(altura.get()) 
        peso_valor = float(peso.get())
        
        resultado.set(peso_valor / altura_valor**2)
    except ValueError:  
        pass 

root = Tk() 
root.title("IMC")  

primeiro = ttk.Frame(root, padding="5 5 14 14")
primeiro.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1) 
root.rowconfigure(0, weight=1) 

altura = StringVar() 
altura_entry = ttk.Entry(primeiro, width=7, textvariable=altura)
altura_entry.grid(column=1, row=1, sticky=(W, E))  

peso = StringVar() 
peso_entry = ttk.Entry(primeiro, width=7, textvariable=peso) 
peso_entry.grid(column=1, row=2, sticky=(W, E))

resultado = StringVar() 
ttk.Label(primeiro, textvariable=resultado).grid(column=2, row=2, sticky=(W, E))

ttk.Button(primeiro, text="calcular", command=calcular).grid(column=3, row=2, sticky=W)  

for child in primeiro.winfo_children(): 
    child.grid_configure(padx=5, pady=5) 

altura_entry.focus()
root.bind("<Return>", calcular) 

root.mainloop()
