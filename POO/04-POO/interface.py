from tkinter import Tk, ttk, PhotoImage

window = Tk()

window.title('Software da Fabi')
window.geometry('500x500+10+20')

frame = ttk.Frame(window, padding=10)
frame.grid()

label = ttk.Label(frame, text='Oi, Fabi!')
label.grid(column=0, row=0)

button = ttk.Button(frame, text='Sair', command=window.destroy)
button.grid(column=0, row=10)

photo = PhotoImage(file=r'POO/04-POO/figs/passada.png')
img = ttk.Label(frame, image=photo)
img.grid(column=0, row=20)

window.mainloop()
