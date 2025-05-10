import tkinter as tk

root = tk.Tk()

root.title('CALCULADORA')
 
root.geometry('200x300')


def soma():
    n1 = float(n1_entry1.get())
    n2 = float(n2_entry2.get())
    soma =  n1 + n2
    resultado.config(text=f'Resultado - {soma}')

def sub():
    n1 = float(n1_entry1.get())
    n2 = float(n2_entry2.get())
    calculo =  n1 - n2
    resultado.config(text=f'Resultado - {calculo}')


def multi():
    n1 = float(n1_entry1.get())
    n2 = float(n2_entry2.get())
    calculo =  n1 * n2
    resultado.config(text=f'Resultado - {calculo}')


def div():
    n1 = float(n1_entry1.get())
    n2 = float(n2_entry2.get())
    calculo =  n1 / n2
    resultado.config(text=f'Resultado - {calculo}')        


# INPUT

n1_entry1 = tk.Entry(root, width=5)
n1_entry1.grid(column=1,row=0, pady=10, padx=10)

n2_entry2 = tk.Entry(root, width=5)
n2_entry2.grid(column=2,row=0, pady=10, padx=10)

btn1 = tk.Button(root,text='+', command=soma)
btn1.grid(column=0, row=2, padx=10)

btn2 = tk.Button(root,text='-', command=sub)
btn2.grid(column=1, row=2, padx=10)

btn3 = tk.Button(root,text='*', command=multi)
btn3.grid(column=2, row=2, padx=10)


btn4 = tk.Button(root,text='/', command=div)
btn4.grid(column=3, row=2, padx=10)


resultado = tk.Label(root, text= '', bg='yellow',fg='red')
resultado.grid(column=1, row=5,pady=10)

root.mainloop()