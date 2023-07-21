
from tkinter import Tk,  ttk, PhotoImage

window = Tk()
window.title('Software da Fabi')
window.geometry("300x200+10+20")

frm = ttk.Frame(window, padding=10)
frm.grid()

# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

# ttk.Button(frm, text="Quit", command=window.destroy).grid(column=1, row=0)

# photo = PhotoImage(file = r"../../Figures/passada.png")
# ttk.Label(frm, text = 'Ficar passada', image = photo).grid(column=10, row=0)


window.mainloop()