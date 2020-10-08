from tkinter import Tk, LEFT, RIGHT, TOP, BOTTOM, E, W, N, S, NW, X, Y, BOTH, StringVar, Toplevel
from tkinter.ttk import Label, Style, Frame, Button, Entry

# new_window = ''


def say_hi():
    global new_window
    Label(new_window, text="Hola mundo!").pack()


new_window_2 = ''


def process_data():
    global new_window_2
    global dato
    Label(new_window_2, text=dato.get()).pack()


def open_another_new_window():
    # global new_window_2
    global dato
    new_window_2 = Toplevel(root)
    new_window_2.geometry('200x200')
    new_window_2.title('Mi segunda ventana secundaria')
    dato = StringVar()
    Entry(new_window_2, textvariable=dato).pack()
    Button(new_window_2, text="Procesar dato", command=process_data).pack()


def open_new_window():
    global new_window
    new_window = Toplevel(root)
    new_window.geometry('200x200')
    new_window.title('Mi primera ventana secundaria')

    frm_equis = Frame(new_window)
    Label(frm_equis, text="Soy un texto dentro de una ventana secundaria!! (=").pack()
    Button(frm_equis, text="Saludo", command=say_hi).pack()
    frm_equis.pack()


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
# Label(frm_three, text="Frame Three").pack(side=TOP, pady=20)
Button(frm_three, text="Abrir nueva ventana...",
       command=open_new_window).pack()
Button(frm_three, text="Abrir otra nueva ventana...",
       command=open_another_new_window).pack()
frm_three.pack()

root.mainloop()
