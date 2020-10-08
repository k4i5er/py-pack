from tkinter import Tk, LEFT, RIGHT, TOP, BOTTOM, E, W, N, S, NW, X, Y, BOTH, StringVar
from tkinter.ttk import Label, Style, Frame

root = Tk()
root.geometry('800x600')

myStyle = Style()
myStyle.configure('TLabel', borderwidth=3, relief="solid")
myStyle.configure('TFrame', borderwidth=3, relief="sunken")

frm_top = Frame(root)
frm_one = Frame(frm_top)
Label(frm_one, text="Frame One 1").pack(
    side=LEFT)
text1 = StringVar()
# Asigna el texto a la text1
text1.set('Esta es mi variable')

# Muestra el valor de text1 en consola
print(text1.get())

Label(frm_one,  textvariable=text1).pack(side=LEFT,  padx=20, pady=20)
frm_one.pack(side=LEFT, anchor=N)
frm_top.pack(side=TOP)

frm_two = Frame(frm_top)
Label(frm_two, text="Frame Two").pack(side=TOP, padx=20, pady=20)
frm_two.pack(side=LEFT, anchor=N)

frm_three = Frame(root)
Label(frm_three, text="Frame Three").pack(side=TOP, pady=20)
frm_three.pack()

root.mainloop()
