import tkinter as tk

def calculate_sum():
    try:
        y = float(entry_y.get())
        total = sum(x * y for x in range(2, 25))
        label_result.config(text=f"Сума: {total}")
    except ValueError:
        label_result.config(text="Введіть коректне число!")

# Створення вікна
root = tk.Tk()
root.title("Варіант 13: Сума x*y")

# Ввід y
tk.Label(root, text="Введіть значення y:").grid(row=0, column=0, padx=5, pady=5)
entry_y = tk.Entry(root)
entry_y.grid(row=0, column=1, padx=5, pady=5)

# Кнопка обчислення
btn_calc = tk.Button(root, text="Обчислити", command=calculate_sum)
btn_calc.grid(row=1, column=0, columnspan=2, pady=5)

# Результат
label_result = tk.Label(root, text="Сума: ")
label_result.grid(row=2, column=0, columnspan=2, pady=5)

# Запуск головного циклу
root.mainloop()