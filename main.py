# Импортируем все классы и функции из библиотеки Tkinter
from tkinter import *

# Создаем окно
window = Tk()

# Изменяем заголовок окна
window.title('Welcome')
# Изменяем размеры окна width x height
window.geometry('400x300')

# Вызываем функцию, чтобы окно не закрывалось сразу после открытия
window.mainloop()