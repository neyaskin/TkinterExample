# Импортируем все классы и функции из библиотеки Tkinter
from tkinter import *

# Создаем окно
window = Tk()

def check():
    print(name.get(), selected.get(), age.get(), check_state.get())
    # label.configure(text=f'Спасибо, {name.get()}')
    label['text'] = f'Спасибо, {name.get()}'

# Изменяем заголовок окна
window.title('Анкета')
# Изменяем размеры окна width x height
window.geometry('700x500')

# Выводит однострочный текст
label = Label(text='Расскажите о себе',
              font=('Arial', 16))
label.place(x=250, y=10)

# Выводит многострочный текст
about = Message(text='Мы рады приветствовать вас в нашей анкете дружбы! '
                     'Пожалуйста, отвечайте на вопросы честно, вся информация останется между нами.',
                font=('Arial', 12),
                width=680)
about.configure(justify=CENTER)
about.place(x=10, y=70)

label_name = Label(text='ФИО: ', font=('Arial', 12))
label_name.place(x=10, y=150)

# Дает возможность ввести какой-то текст
name = Entry(width=30)
name.place(x=60, y=155)

label_gender = Label(text='Ваш пол? ', font=('Arial', 12))
label_gender.place(x=10, y=200)

# Добавляем вохможность выбрать пол
selected = IntVar()
# Если кликнуть по Мужской, в переменнуя selected сохранится число 1
man_radbtn = Radiobutton(text='Мужской', value=1, variable=selected)
woman_radbtn = Radiobutton(text='Женский', value=2, variable=selected)
man_radbtn.place(x=90, y=200)
woman_radbtn.place(x=170, y=200)

label_age = Label(text='Сколько вам лет? ', font=('Arial', 12))
label_age.place(x=10, y=250)

# Позволяет выбрать значение нажимая на стрелочки вверх вниз
age = Spinbox(from_=0, to=100, width=20)
age.place(x=10, y=280)

# Позволяет выбрать несколько галочкой несколько вариантов, но в нашей случае будет только один
check_state = IntVar()
check_btn = Checkbutton(text='Запомнить меня', variable=check_state)
check_btn.place(x=10, y=350)

# Позволяет обработать нажатие пользователя на кнопку
btn = Button(text='Отправить',
             font=('Arial', 10),
             background='green',
             command=check)
btn.place(x=10, y=400)




# Вызываем функцию, чтобы окно не закрывалось сразу после открытия
window.mainloop()
