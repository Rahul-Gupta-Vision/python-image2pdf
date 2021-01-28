import tkinter
import img2pdf
from tkinter.filedialog import *
from tkinter import messagebox

root = tkinter.Tk()
root.resizable(0, 0)
fil_list = []


def ui():
    global label, label2, listbox
    frame = Frame(root, borderwidth=9, relief=SUNKEN)
    frame.pack(side=TOP, fill='x')
    label = Label(frame, text='Image to PDF', bg='cyan', font='Arial 20 bold')
    label.pack(side=TOP)
    frame2 = Frame(root, borderwidth=9, relief=SUNKEN, bg='yellow')
    frame2.pack(side=TOP)
    label2 = Label(frame2, borderwidth=9, relief=SUNKEN, text='Selected files will show up here.')
    label2.pack(side=TOP)
    listbox = Listbox(frame2, borderwidth=9, relief=SUNKEN,font='Arial 15 bold')
    listbox.pack(side=TOP, fill='x')
    butframe = Frame(root, borderwidth=9, relief=SUNKEN)
    butframe.pack(side=TOP, fill='x')
    b1 = Button(butframe, text='select file', command=select_files, bg='grey')
    b1.pack(side=LEFT)
    b2 = Button(butframe, text='Convert', command=convert, bg='grey')
    b2.pack(side=RIGHT)
    b3 = Button(butframe, text='Exit', bg='grey', command=lambda: exit('forced closed'))
    b3.pack(side=BOTTOM)
    b4 = Button(butframe, text='Clear Files', bg='grey', command=clear)
    b4.pack(side=TOP)


def select_files():
    fil = askopenfilename(filetypes=[('Image files', ['*.jpeg', '*.png', '*.jpg'])])
    z = str(fil)
    k = z.replace('/', '\\\\')
    print(fil)
    print(k)
    fil_list.append(k)
    print(fil_list)
    listbox.insert(0, k)


def convert():
    if listbox.size() > 0:
        try:
            with open('Image2PDF.pdf', 'wb') as f1:
                f1.write(img2pdf.convert(fil_list))
            messagebox.showinfo('Pdf created', 'Pdf created with name Image2Pdf.pdf')
        except:
            messagebox.showerror('Error', 'Error in converting pdf from image')
    else:
        messagebox.showwarning('Error', 'no files are selected')


def clear():
    listbox.delete(END)
    fil_list.clear()


ui()
root.mainloop()
