import random
import string
import tkinter as tk
from tkinter import messagebox, font

def generate_code(length=8, use_numbers=True, use_uppercase=True, use_lowercase=True):
    characters = ""
    if use_numbers:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    
    if not characters:
        raise ValueError("Трябва да бъде избрана поне една опция за символи.")
    
    return ''.join(random.choice(characters) for _ in range(length))

def on_generate():
    try:
        length = int(length_entry.get())
        use_numbers = numbers_var.get()
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        
        code = generate_code(length, use_numbers, use_uppercase, use_lowercase)
        
        # Копиране на кода в клипборда
        root.clipboard_clear()
        root.clipboard_append(code)
        
        messagebox.showinfo("Случаен код", f"Генерираният код е: {code}\n\nКодът е копиран в клипборда!")
    except ValueError:
        messagebox.showerror("Грешка", "Моля, въведете валидна дължина на кода.")

# Основен прозорец с цветове и стилове, вдъхновени от Telegram
root = tk.Tk()
root.title("Генератор на кодове")
root.geometry("400x400")
root.config(bg="#0088cc")  # Син фон, подобен на Telegram

# Настройки за стилове на шрифтовете с "Roboto"
try:
    title_font = font.Font(family="Roboto", size=16, weight="bold")
    label_font = font.Font(family="Roboto", size=12)
    button_font = font.Font(family="Roboto", size=12, weight="bold")
except:
    title_font = font.Font(family="Helvetica", size=16, weight="bold")
    label_font = font.Font(family="Helvetica", size=12)
    button_font = font.Font(family="Helvetica", size=12, weight="bold")

# Заглавие на приложението
title_label = tk.Label(root, text="Генератор на случайни кодове", font=title_font, bg="#0088cc", fg="white")
title_label.pack(pady=15)

# Рамка за входни данни
frame = tk.Frame(root, bg="white", padx=15, pady=15, relief="groove", bd=2)
frame.pack(pady=10)

tk.Label(frame, text="Дължина на кода:", font=label_font, bg="white", fg="#0088cc").pack(anchor="w")
length_entry = tk.Entry(frame, font=label_font, width=10, justify="center", bg="#f0f0f0", fg="#0088cc")
length_entry.pack(pady=5)

numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text="Включване на цифри", variable=numbers_var, font=label_font, bg="white", fg="#0088cc", selectcolor="#e1f5fe").pack(anchor="w")

uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text="Включване на главни букви", variable=uppercase_var, font=label_font, bg="white", fg="#0088cc", selectcolor="#e1f5fe").pack(anchor="w")

lowercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(frame, text="Включване на малки букви", variable=lowercase_var, font=label_font, bg="white", fg="#0088cc", selectcolor="#e1f5fe").pack(anchor="w")

# Бутон за генериране с Telegram стил
generate_button = tk.Button(root, text="Генерирай код", command=on_generate, font=button_font, bg="#ffffff", fg="#0088cc", padx=10, pady=5, relief="raised")
generate_button.pack(pady=20)

# Стартиране на приложението
root.mainloop()!
