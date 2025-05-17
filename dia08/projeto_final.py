import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
def conectar ():
    return sqlite3.connect("financas.db")
    


def criar_tabela():
    conn = conectar()
    c = conn.cursor()
   
    c.execute('''
          CREATE TABLE IF NOT EXISTS contas (
          ID INTEGER PRIMARY KEY AUTOINCREMENT,
          Nome TEXT NOT NULL,
          Saldo REAL NOT NULL DEFAULT 0.0
        )
''')
    

def adicionar_pessoas():
    nome = entry_nome.get()
    
    if nome:
        conn = sqlite3.connect("financas.db")
        c = conn.cursor()
        c.execute("INSERT INTO contas (Nome, Saldo) VALUES (?, ?)", (nome, 0.0))
        conn.commit()
        conn.close()
        mostrar_contas()
        messagebox.showinfo("Sucesso", "Usuário ",nome," adicionado com sucesso!")
    if not nome:
        messagebox.showerror("Erro", "Por favor, insira um nome.")  

def inserir_dinheiro():
    selecao = tree.selection()
    if selecao:
        user_ID = tree.item(selecao)["values"][0]
        saldo = float(entry_valor.get())
        conn = conectar()
        c = conn.cursor()
        c.execute("UPDATE contas SET Saldo = Saldo + ? WHERE ID = ?", (saldo, user_ID))
        conn.commit()
        conn.close()
        mostrar_contas()

def sacar_dinheiro():
    selecao = tree.selection()
    if selecao:
        user_ID = tree.item(selecao)["values"][0]
        saldo = float(entry_valor.get())
        conn = conectar()
        c = conn.cursor()
        c.execute("UPDATE contas SET Saldo = Saldo - ? WHERE ID = ?", (saldo, user_ID))
        conn.commit()
        conn.close()
        mostrar_contas()

def excluir_usuario():
    selecao = tree.selection()
    if selecao:
        user_ID = tree.item(selecao)["values"][0]
        conn = conectar()
        c = conn.cursor()
        c.execute("DELETE FROM contas WHERE ID = ?", (user_ID,))
        conn.commit()
        conn.close()
        mostrar_contas()
        
def mostrar_contas():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM contas")
    contas = c.fetchall()
    for conta in contas:
        tree.insert("", "end", values=(conta[0], conta[1], conta[2]))
    conn.close()
    
def excluir_conta():
    selecao = tree.selection()
    if selecao:
        user_ID = tree.item(selecao)["values"][0] 
        conn = conectar()
        c = conn.cursor()
        c.execute("DELETE FROM contas WHERE ID = ?", (user_ID,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Conta excluída com sucesso!")
        mostrar_contas() 
    else:
        messagebox.showerror("Erro", "Selecione uma conta para excluir!")



janela = tk.Tk()
janela.title("Finanças simples")


label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_valor = tk.Label(janela, text="Valor:")
label_valor.grid(row=1, column=0, padx=10, pady=5)
entry_valor = tk.Entry(janela)
entry_valor.grid(row=1, column=1, padx=10, pady=5)


btn_criar = tk.Button(janela, text="Criar Conta", command=adicionar_pessoas)
btn_criar.grid(row=2, column=0, padx=10, pady=5)

btn_depositar = tk.Button(janela, text="Depositar", command=inserir_dinheiro)
btn_depositar.grid(row=2, column=1, padx=10, pady=5)

btn_sacar = tk.Button(janela, text="Sacar", command=sacar_dinheiro)
btn_sacar.grid(row=2, column=2, padx=10, pady=5)

btn_excluir = tk.Button(janela, text="Excluir Conta", command=excluir_conta)
btn_excluir.grid(row=2, column=3, padx=10, pady=5)



columns = ("ID", "Nome", "Saldo")
tree = ttk.Treeview(janela, columns=columns, show="headings")
tree.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col)


criar_tabela()
mostrar_contas()

janela.mainloop()
      