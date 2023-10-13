import tkinter

window = tkinter.Tk()
window.title("Baton calculator")
window.geometry("385x505+0+0")
window.configure(background="black")


def baton_rabotau_pazyuzyu(nasmork):
    riliz_skora = len(baton.get()) + 1
    if riliz_skora > 9:
        return
    baton.insert(index=1000, string=nasmork)


def Hy_kogda_riliz():
    up_coming_riliz_hleba = baton.get()
    up_coming_riliz_hleba = up_coming_riliz_hleba.replace("÷", "/")
    baton.delete(0, "end")
    baton.insert(0, eval(up_coming_riliz_hleba))


# ------------------ Картинки ------------------ #

baton_minip = tkinter.PhotoImage(file="button_0.png")
baton_minid = tkinter.PhotoImage(file="button_1.png")
baton_minin = tkinter.PhotoImage(file="button_2.png")
baton_minini = tkinter.PhotoImage(file="button_3.png")
baton_minnnni = tkinter.PhotoImage(file="button_4.png")
baton_minnni = tkinter.PhotoImage(file="button_5.png")
baton_minni = tkinter.PhotoImage(file="button_6.png")
baton_minnig7 = tkinter.PhotoImage(file="button_7.png")
baton_minnig8 = tkinter.PhotoImage(file="button_8.png")
baton_minnig9 = tkinter.PhotoImage(file="button_9.png")

baton_mini_ultra_555 = tkinter.PhotoImage(file="button_plus.png")
baton_minio = tkinter.PhotoImage(file="button_dot.png")
baton_minim = tkinter.PhotoImage(file="button_eq.png")
baton_minimy = tkinter.PhotoImage(file="button_div.png")
baton_minnig = tkinter.PhotoImage(file="button_minus.png")
baton_minnigx = tkinter.PhotoImage(file="button_multi.png")

cateyca = tkinter.PhotoImage(file="cateyca (1).png")

# ------------------ Кнопки ------------------ №

button_0 = tkinter.Button(window, text="0", bg='gray', highlightbackground='black', padx=40, pady=35, image=baton_minip,
                          command=lambda: baton_rabotau_pazyuzyu(0))
button_0.place(x=0, y=410)

button_1 = tkinter.Button(window, text="1", bg='gray', highlightbackground='black', padx=30, pady=35, image=baton_minid,
                          command=lambda: baton_rabotau_pazyuzyu(1))
button_1.place(x=0, y=318)

button_2 = tkinter.Button(window, text="2", bg='gray', highlightbackground='black', padx=30, pady=35, image=baton_minin,
                          command=lambda: baton_rabotau_pazyuzyu(2))
button_2.place(x=95, y=318)

button_3 = tkinter.Button(window, text="3", bg='gray', highlightbackground='black', padx=30, pady=35,
                          image=baton_minini, command=lambda: baton_rabotau_pazyuzyu(3))
button_3.place(x=190, y=318)

baton_p = tkinter.Button(window, text="+", bg='orange', highlightbackground='black', padx=30, pady=35,
                         image=baton_mini_ultra_555, command=lambda: baton_rabotau_pazyuzyu("+"))
baton_p.place(x=285, y=318)

baton_4 = tkinter.Button(window, text="4", bg='gray', highlightbackground='black', padx=30, pady=35,
                         image=baton_minnnni, command=lambda: baton_rabotau_pazyuzyu(4))
baton_4.place(x=0, y=225)

baton_5 = tkinter.Button(window, text="5", bg='gray', highlightbackground='black', padx=30, pady=35, image=baton_minnni,
                         command=lambda: baton_rabotau_pazyuzyu(5))
baton_5.place(x=95, y=225)

baton_6 = tkinter.Button(window, text="6", bg='gray', highlightbackground='black', padx=30, pady=35, image=baton_minni,
                         command=lambda: baton_rabotau_pazyuzyu(6))
baton_6.place(x=190, y=225)

button_dot = tkinter.Button(window, text=",", bg='gray', highlightbackground='black', padx=30, pady=35,
                            image=baton_minio, command=lambda: baton_rabotau_pazyuzyu("."))
button_dot.place(x=95, y=410)

button_eq = tkinter.Button(window, text="=", bg='orange', highlightbackground='black', padx=30, pady=35,
                           image=baton_minim, command=Hy_kogda_riliz)
button_eq.place(x=190, y=410)

button_div = tkinter.Button(window, text="÷", bg='orange', highlightbackground='black', padx=30, pady=35,
                            image=baton_minimy, command=lambda: baton_rabotau_pazyuzyu("÷"))
button_div.place(x=285, y=413)

baton_minus = tkinter.Button(window, text="-", bg='gray', highlightbackground='black', padx=30, pady=35,
                             image=baton_minnig, command=lambda: baton_rabotau_pazyuzyu("-"))
baton_minus.place(x=285, y=225)

baton_7 = tkinter.Button(window, text="7", bg='gray', highlightbackground='black', padx=30, pady=35,
                         image=baton_minnig7, command=lambda: baton_rabotau_pazyuzyu(7))
baton_7.place(x=0, y=130)

baton_8 = tkinter.Button(window, text="8", bg='gray', highlightbackground='black', padx=30, pady=35,
                         image=baton_minnig8, command=lambda: baton_rabotau_pazyuzyu(8))
baton_8.place(x=95, y=130)

baton_9 = tkinter.Button(window, text="9", bg='gray', highlightbackground='black', padx=30, pady=35,
                         image=baton_minnig9, command=lambda: baton_rabotau_pazyuzyu(9))
baton_9.place(x=190, y=130)

baton_X = tkinter.Button(window, text="x", bg='gray', highlightbackground='black', padx=30, pady=35,
                         image=baton_minnigx, command=lambda: baton_rabotau_pazyuzyu("*"))
baton_X.place(x=285, y=130)

baton = tkinter.Entry(window, width=9, font="Consolas 68", bg="black", justify="right", bd=0, selectbackground="orange",
                      fg="white")
baton.place(x=0, y=0)
baton.focus_set()

cateyca_ultra_120_gb_na_procesare_intl = tkinter.Button(window, text="6", bg='gray', highlightbackground='black',
                                                        padx=30, pady=35, image=cateyca, state="disabled")
cateyca_ultra_120_gb_na_procesare_intl.place(x=700, y=225)

window.mainloop()
