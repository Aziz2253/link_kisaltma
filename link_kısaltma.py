import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip

def shorten_url():
    long_url = entry.get()
    if long_url:
        try:
            response = requests.get(f'https://tinyurl.com/api-create.php?url={long_url}')
            short_url = response.text
            result_label.config(text=f"Kısa URL: {short_url}")
            copy_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Hata", "URL kısaltılamadı.")
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir URL giriniz.")

def copy_to_clipboard():
    short_url = result_label.cget("text")[10:]  # "Kısa URL: " kısmını kesmek için
    if short_url:
        pyperclip.copy(short_url)
        messagebox.showinfo("Kopyalandı", "Kısa URL kopyalandı!")

# tkinter arayüzü
app = tk.Tk()
app.title("Link Kısaltma")

# Uzun adresin girileceği yer
label = tk.Label(app, text="Linki Giriniz:")
label.pack(pady=20)

entry = tk.Entry(app, width=40)
entry.pack()

# Adresin kısaltılacağı alan
shorten_button = tk.Button(app, text="Kısalt", command=shorten_url)
shorten_button.pack(pady=10)

# Kısa URL'nin görüleceği yer
result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Kopyala Butonu
copy_button = tk.Button(app, text="Kopyala", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=10)

app.mainloop()
