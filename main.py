import tkinter.ttk as ttk
import ttkthemes.themed_tk as Tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import tkinter as tk
import huffman
import math

def select_file():
	filetypes = (
		('text files', '*.txt'),
		('All files', '*.*')
	)
	# show the open file dialog
	f = fd.askopenfile(filetypes=filetypes)
	content = f.read()
	f.close()
	entryfile.delete('1.0', tk.END)
	entryfile.insert('1.0', content)
	data, info = huffman.huffman(content)
	msg = huffman.decode_huffman(data, info)
	datos = huffman.join_sort(content, msg)
	writes = huffman.write(content, datos)
	entryfileout.delete('1.0', tk.END)
	entryfileout.insert('1.0', writes)
	total = len(content)
	before = len(content)*8
	after = len(writes)
	mean = 0
	sum = 0
	for i in datos[2]:
		sum += len(i)
	mean = sum/len(datos[2])
	entropy = 0
	for i in datos[1]:
		entropy += (i/len(content))*(math.log(1/(i/len(content))) / math.log(2))
	perc = 100-((after*100)/before)
	informacion = "Total de caracteres: "+str(total)+"\nBits antes: "+str(before)+"\nBits con Huffman: "+str(after)+"\nPromedio: "+str(mean)+"\nEntropia: "+str(entropy)+"\nPorcentaje de compactacion: "+str(perc)+"."
	lblinfile.delete('1.0', tk.END)
	lblinfile.insert('1.0', informacion)
	for item in treef.get_children():
		treef.delete(item)
	for i in range(len(datos[0])):
		treef.insert("", "end",text=datos[0][i], values=(datos[0][i], datos[1][i], datos[2][i]))

def get_data():
	text = entry.get()
	entry_output.delete(0,tk.END)
	data, info = huffman.huffman(text)
	msg = huffman.decode_huffman(data, info)
	datos = huffman.join_sort(text, msg)
	writes = huffman.write(text, datos)
	entry_output.insert(0, writes)
	total = len(text)
	before = len(text)*8
	after = len(writes)
	mean = 0
	sum = 0
	for i in datos[2]:
		sum += len(i)
	mean = sum/len(datos[2])
	entropy = 0
	for i in datos[1]:
		entropy += (i/len(text))*(math.log(1/(i/len(text))) / math.log(2))
	perc = 100-((after*100)/before)
	informacion = "Total de caracteres: "+str(total)+"\nBits antes: "+str(before)+"\nBits con Huffman: "+str(after)+"\nPromedio: "+str(mean)+"\nEntropia: "+str(entropy)+"\nPorcentaje de compactacion: "+str(perc)+"."
	lblinfo.delete('1.0', tk.END)
	lblinfo.insert('1.0', informacion)
	for item in tree.get_children():
		tree.delete(item)
	for i in range(len(datos[0])):
		tree.insert("", "end",text=datos[0][i], values=(datos[0][i], datos[1][i], datos[2][i]))

root = Tk.ThemedTk(theme="adapta")
root.configure(bg="white")
root.title("Metodo de Huffman con interfaz grafica :)")
root.geometry('400x300')

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

fr_file = ttk.Frame(notebook)
fr_text = ttk.Frame(notebook)

fr_file.pack(fill="both", expand=True)
fr_text.pack(fill="both", expand=True)

notebook.add(fr_text, text='Mensaje desde entry')
notebook.add(fr_file, text='Mensaje desde archivo.txt')

# Frame de entrada de mensaje con archivo
frameFile = ttk.Frame(fr_file)
frameFile.pack(fill="both", expand=True, pady=10, padx=10)

btnFile = ttk.Button(
	frameFile,
	text="Seleccionar archivo",
	command=select_file
)
btnFile.pack()

entryfile = tk.Text(frameFile, height=10)
entryfile.pack()

entryfileout = tk.Text(frameFile, height=10)
entryfileout.pack()

treef = ttk.Treeview(frameFile)
treef['columns'] = ("Letra", "Repeticion", "Codigo")

treef.column('#0', width=0, stretch=0)
treef.column("Letra",anchor='center', width=80)
treef.column("Repeticion",anchor='center',width=80)
treef.column("Codigo",anchor='center',width=80)

treef.heading("#0",text="",anchor='center')
treef.heading("Letra",text="Letra",anchor='center')
treef.heading("Repeticion",text="Repeticion",anchor='center')
treef.heading("Codigo",text="Binario",anchor='center')

treef.pack()

lblinfile = tk.Text(frameFile)
lblinfile.pack()

# Frame de entrada de mensaje con texto
frameEntry = ttk.Frame(fr_text)
frameEntry.pack(fill="both", expand=True, padx=10)

entry = ttk.Entry(frameEntry)
entry.pack(fill='x', pady=10)

btn = ttk.Button(frameEntry, text="Comenzar", command=get_data)
btn.pack()

entry_output = ttk.Entry(frameEntry)
entry_output.pack(fill='x', pady=10)

tree = ttk.Treeview(frameEntry)
tree['columns'] = ("Letra", "Repeticion", "Codigo")

tree.column('#0', width=0, stretch=0)
tree.column("Letra",anchor='center', width=80)
tree.column("Repeticion",anchor='center',width=80)
tree.column("Codigo",anchor='center',width=80)

tree.heading("#0",text="",anchor='center')
tree.heading("Letra",text="Letra",anchor='center')
tree.heading("Repeticion",text="Repeticion",anchor='center')
tree.heading("Codigo",text="Binario",anchor='center')

tree.pack(fill='y')

lblinfo = tk.Text(frameEntry)
lblinfo.pack()

root.mainloop()