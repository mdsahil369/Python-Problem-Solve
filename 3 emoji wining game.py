import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.constants import ANCHOR, CENTER, LEFT, N, NW, RIGHT, TOP, W

game = tk.Tk()
game.title('Falcon Game')
game.geometry('300x350+500+50')

a = '\U0001F600'
entry_1 = tk.Label(game,text=a,font='arial 50')
entry_1.grid(row=1,column=0,padx=10)
entry_2 = tk.Label(game,text=a,font='arial 50')
entry_2.grid(row=1,column=1,padx=10)
entry_3 = tk.Label(game,text=a,font='arial 50')
entry_3.grid(row=1,column=2,padx=10)

money = [0,0,0,0,0,0,0,0,0,0]

money_lable = ttk.Label(game,text=f'The Amount Of Money Is : {len(money)}$')
money_lable.grid(row=0,column=0,columnspan=3)

def start():
    if len(money) != 0:
        emoji = ('\U0001F600','\U0001F60D','\U0001F911')#,'\U0001F60E'
        last_range = 3
        money.pop()
        print(money)
        import random
        a = random.randrange(0,last_range)
        import random
        b = random.randrange(0,last_range)
        import random
        c = random.randrange(0,last_range)
        money_lable = ttk.Label(game,text=f'The Amount Of Money Is : {len(money)}$')
        money_lable.grid(row=0,column=0,columnspan=3)
        entry_1 = tk.Label(game,text=emoji[a],font='arial 50')
        entry_1.grid(row=1,column=0,padx=10)
        entry_2 = tk.Label(game,text=emoji[b],font='arial 50')
        entry_2.grid(row=1,column=1,padx=10)
        entry_3 = tk.Label(game,text=emoji[c],font='arial 50')
        entry_3.grid(row=1,column=2,padx=10)
        if a==b and b==c:
            messagebox.showinfo('Message','You Are Win ! And You Win 10$ To Play Game !')
            for i in range(0,11):
                money.append(0)
    else:
        messagebox.showinfo('Message','End Game')

submit = ttk.Button(game,text='Start',command=start)
submit.grid(row=2,column=0,padx=10,pady=20)

game.mainloop()