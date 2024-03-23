"""
Created on 22.03.2024
@author: Matheus
"""

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


class App:
    def __init__(self, root):
        self.root = root
        root.title('Divisor de Pastas')

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Origem
        self.origem_label = tk.Label(self.frame, text='Diretório de Origem:')
        print(self.origem_label)
        self.origem_label.pack()
        self.origem_entry = tk.Entry(self.frame, width=50)
        self.origem_entry.pack(pady=5)
        self.origem_button = tk.Button(
            self.frame, text='Escolher', command=self.escolher_origem
        )
        self.origem_button.pack()

        # Destino
        self.destino_label = tk.Label(self.frame, text='Diretório de Destino:')
        self.destino_label.pack()
        self.destino_entry = tk.Entry(self.frame, width=50)
        self.destino_entry.pack(pady=5)
        self.destino_button = tk.Button(
            self.frame, text='Escolher', command=self.escolher_destino
        )
        self.destino_button.pack()

        # Ação
        self.iniciar_button = tk.Button(
            self.frame, text='Iniciar Divisão', command=self.iniciar_divisao
        )
        self.iniciar_button.pack(pady=20)

    def escolher_origem(self):
        diretorio = filedialog.askdirectory()
        self.origem_entry.delete(0, tk.END)
        self.origem_entry.insert(0, diretorio)

    def escolher_destino(self):
        diretorio = filedialog.askdirectory()
        self.destino_entry.delete(0, tk.END)
        self.destino_entry.insert(0, diretorio)

    def iniciar_divisao(self):
        origem = self.origem_entry.get()
        destino = self.destino_entry.get()
        if not origem or not destino:
            messagebox.showerror(
                'Erro', 'Por favor, escolha os diretórios de origem e destino.'
            )
            return 0
        try:
            self.dividir_pastas(origem, destino)
            messagebox.showinfo(
                'Sucesso', 'Pastas divididas e movidas com sucesso.'
            )
        except Exception as e:
            messagebox.showerror('Erro', f'Ocorreu um erro: {str(e)}')

    def dividir_pastas(self, origem, destino):
        pastas = [
            os.path.join(origem, pasta)
            for pasta in os.listdir(origem)
            if os.path.isdir(os.path.join(origem, pasta))
        ]
        lotes = [pastas[i: i + 50] for i in range(0, len(pastas), 50)]

        for indice, lote in enumerate(lotes):
            pasta_destino = os.path.join(destino, f'lote_{indice + 1}')
            os.makedirs(pasta_destino, exist_ok=True)
            for pasta in lote:
                shutil.move(pasta, pasta_destino)


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
