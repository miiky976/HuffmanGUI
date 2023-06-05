import tkinter.ttk as ttk
import ttkthemes.themed_tk as Tk

root = Tk.ThemedTk(theme="breeze")
root.configure(bg="white")

entry = ttk.Entry(root)
entry.pack()

btn = ttk.Button(root, text="Hola")
btn.pack()

root.mainloop()