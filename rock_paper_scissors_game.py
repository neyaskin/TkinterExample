from tkinter import *
from random import choice

class Game:
    def __init__(self):
        self.win = 0
        self.lose = 0
        self.draw = 0
        self.moves = ['Камень', 'Ножницы', 'Бумага']

    def move_result(self, user_choice):
        comp_choice = choice(self.moves)
        if user_choice == comp_choice:
            self.draw += 1
            return (f'Ход игрока: {user_choice}\n'
                    f'Ход компьютера: {comp_choice}\n'
                    f'Ничья')
        elif user_choice == 'Камень' and comp_choice == 'Ножницы' or \
            user_choice == 'Ножницы' and comp_choice == 'Бумага' or \
            user_choice == 'Бумага' and comp_choice == 'Камень':
            self.win += 1
            return (f'Ход игрока: {user_choice}\n'
                    f'Ход компьютера: {comp_choice}\n'
                    f'Победа')
        else:
            self.lose += 1
            return (f'Ход игрока: {user_choice}\n'
                    f'Ход компьютера: {comp_choice}\n'
                    f'Поражение')

    def show_info(self):
        return (f'Победы: {self.win}\n'
                    f'Поражения: {self.lose}\n'
                    f'Ничьи: {self.draw}')

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x300')
        self.window.title('Камень, ножницы, бумага')
        self.game = Game()
        self.startUI(self.window)

        self.window.mainloop()

    def startUI(self, window):
        for c in range(3): window.columnconfigure(index=c, weight=1)
        for r in range(3): window.rowconfigure(index=r, weight=1)

        self.btn1 = Button(window, text='Камень', font=('Arial', 12),
                           command=lambda: self.btn_click('Камень'))
        self.btn2 = Button(window, text='Ножницы', font=('Arial', 12),
                           command=lambda: self.btn_click('Ножницы'))
        self.btn3 = Button(window, text='Бумага', font=('Arial', 12),
                           command=lambda: self.btn_click('Бумага'))
        self.btn1.grid(row=2, column=0)
        self.btn2.grid(row=2, column=1)
        self.btn3.grid(row=2, column=2)

        self.lb1 = Label(window, text='Начало игры!', font=('Arial', 16))
        self.lb1.grid(row=1, column=0, columnspan=3)

        self.lb2 = Label(window,
                         justify=LEFT,
                         font=('Arial', 12),
                         text=self.game.show_info())
        self.lb2.grid(row=0, column=0)

    def btn_click(self, user_choice):
        self.lb1['text'] = self.game.move_result(user_choice)
        self.lb2['text'] = self.game.show_info()

app = GUI()