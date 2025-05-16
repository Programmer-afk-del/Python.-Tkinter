from tkinter import *
from math import cos, acos, sqrt, log

def calculate_result():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        numerator = sqrt(a) + cos(b)
        denominator = log(c + 2)
        if denominator == 0:
            result_label['text'] = "Ділення на нуль!"
        else:
            result = numerator / denominator
            result_label['text'] = f"Результат: {result:.4f}"
    except ValueError:
        result_label['text'] = "Введіть коректні числові значення!"

root = Tk()
root.title("Завдання 1 - Варіант 13")
root.geometry("300x200")

#Введення a
Label(root, text="a:").grid(row=0, column=0, padx=10, pady=5)
entry_a = Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5)
entry_a.insert(0, "1.6")

#Введення b
Label(root, text="b:").grid(row=1, column=0, padx=10, pady=5)
entry_b = Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=5)
entry_b.insert(0, "4.2")

#Введення c
Label(root, text="c:").grid(row=2, column=0, padx=10, pady=5)
entry_c = Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=5)
entry_c.insert(0, "6.3")

#Кнопка обчислення
Button(root, text="Обчислити", command=calculate_result).grid(row=3, column=0, columnspan=2, pady=10)

#Виведення результату
result_label = Label(root, text="Результат: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()