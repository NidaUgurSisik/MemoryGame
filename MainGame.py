import random
from tkinter import *
from tkinter import messagebox
import time

game = Tk()
game.title("Memory Game")  # başlık
canvas_width = 450
canvas_height = 450

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
w = Canvas(game,
           width=canvas_width,
           height=canvas_height)
w.pack()
w.create_rectangle(10, 45, canvas_width-10, canvas_width-70, fill=random.choice(colors))
w.create_line(5,40,445,40,fill="black",width="10")
w.create_line(5,40,5,385,fill="black",width="10")
w.create_line(445,40,445,385,fill="black",width="10")
w.create_line(5,385,445,385,fill="black",width="10")

level = 5  # başlangıç leveli
x = 0
DELAY = 400
memo = []
entry1 = Entry(game)
w.create_window(225, 400, window=entry1)


def randomly():
    entry1.config(state='disabled')
    for x in range(0, level):
        number = random.randint(0, 9)
        w.create_text(random.randint(15, 430),
                      random.randint(50, 375),
                      font=("family ", 15),
                      text=number, tag="number"+str(x))
        w.itemconfigure("number"+str(x), state='hidden')
        memo.append(number)


def clear():
    for x in range(0, level):
        w.delete("number"+str(x))


def show_numbers(c=0):
    if c <= level:
        w.itemconfigure("number"+str(c), state="normal")
        game.after(DELAY, hide_numbers, c)
    if c == level:
        entry1.config(state='normal')


def hide_numbers(c=0):
    if c <= level:
        w.itemconfigure("number"+str(c), state="hidden")
        game.after(DELAY, show_numbers, c+1)
    if c == level:
        entry1.config(state='normal')


def basla():
    randomly()
    show_numbers()
    button1.destroy()


button1 = Button(game, text="Başla", command=basla)  # BAŞLATMA BUTONU
button1.configure(width=10, background="#340273",
                  fg="white", activebackground="#545454")
button1_window = w.create_window(225, 15, window=button1)


def kontrol_noktasi():
    global level
    answer = []

    for ch in entry1.get():
        if ch.isdigit():
            answer.append(int(ch))

    if answer == memo:
        memo.clear()
        clear()
        entry1.delete(0, 'end')
        messagebox.showinfo(
            "Sonuç", f"Level {level} Başarılı {level+1}. Levele geçmek için butona basınız :) ")
        level += 1
        randomly()
        show_numbers()
    else:
        messagebox.showinfo(
            "Sonuç", f"Level {level} Başarısız daha sonra tekrar deneyiniz cevap {memo} olacaktı :(")
        game.quit()


button2 = Button(game, text="Kontrol Et",
                 command=kontrol_noktasi)  # KONTROL BUTONU
button2.configure(width=10, background="#340273",
                  fg="white", activebackground="#545454")
button2_window = w.create_window(225, 435, window=button2)

mainloop()
