import sqlite3
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def conectar():
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
    conn.commit()
    conn.close()


def adicionar_pessoa():
    nome = entry_nome.get()
    if nome:
        conn = conectar()
        c = conn.cursor()
        c.execute("INSERT INTO contas (Nome, Saldo) VALUES (?, ?)", (nome, 0.0))
        conn.commit()
        conn.close()
        mostrar_contas()
        messagebox.showinfo("Sucesso", f"Usuário {nome} adicionado com sucesso!")
    else:
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


janela = ctk.CTk()
janela.geometry("800x500")
janela.title("Finanças Simples")

frame = ctk.CTkFrame(janela)
frame.pack(pady=10, padx=5, fill="both", expand=True)

style = ttk.Style()
style.configure("Treeview", fill = "both", expand=True)


label_nome = ctk.CTkLabel(frame, text="Nome:")
label_nome.grid(row=0, column=0, padx=1, pady=5)
entry_nome = ctk.CTkEntry(frame)
entry_nome.grid(row=0, column=1, padx=1, pady=5)

label_valor = ctk.CTkLabel(frame, text="Valor:")
label_valor.grid(row=1, column=0, padx=1, pady=5)
entry_valor = ctk.CTkEntry(frame)
entry_valor.grid(row=1, column=1, padx=1, pady=5)


btn_criar = ctk.CTkButton(frame, text="Criar Conta", command=adicionar_pessoa, width = 200)
btn_criar.grid(row=2, column=0, padx=0, pady=5)

btn_depositar = ctk.CTkButton(frame, text="Depositar", command=inserir_dinheiro, width = 200)
btn_depositar.grid(row=2, column=1, padx=0, pady=5)

btn_sacar = ctk.CTkButton(frame, text="Sacar", command=sacar_dinheiro, width = 200)
btn_sacar.grid(row=2, column=2, padx=0, pady=5)

btn_excluir = ctk.CTkButton(frame, text="Excluir Conta", command=excluir_conta, width = 200)
btn_excluir.grid(row=2, column=3, padx=0, pady=5)

columns = ("ID", "Nome", "Saldo")
tree = ttk.Treeview(frame, columns=columns, show="headings", height = 18)
tree.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_contas()

janela.mainloop()
