from tkinter import *
from math import sqrt, sin, cos, acos

def calculate_median():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        # Формула медіани до сторони a
        median_a = 0.5 * sqrt(2 * b2 + 2 * c2 - a**2)
        result_label['text'] = f"Медіана до a: {median_a:.4f} см"
    except ValueError:
        result_label['text'] = "Введіть коректні числові значення!"

root = Tk()
root.title("Трикутник - Варіант 13")
root.geometry("300x200")

# Введення a
Label(root, text="a (см):").place(x=20, y=20)
entry_a = Entry(root)
entry_a.place(x=100, y=20)
entry_a.insert(0, "8.6")

# Введення b
Label(root, text="b (см):").place(x=20, y=60)
entry_b = Entry(root)
entry_b.place(x=100, y=60)
entry_b.insert(0, "13.6")

# Введення c
Label(root, text="c (см):").place(x=20, y=100)
entry_c = Entry(root)
entry_c.place(x=100, y=100)
entry_c.insert(0, "7.8")

# Кнопка обчислення
Button(root, text="Обчислити медіану", command=calculate_median).place(x=50, y=140)

# Виведення результату
result_label = Label(root, text="Результат: ")
result_label.place(x=50, y=170)

root.mainloop()