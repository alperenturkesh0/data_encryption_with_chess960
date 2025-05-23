import tkinter as tk
from tkinter import ttk, messagebox
from crypto_class import data_encryption

BG_COLOR = "#f0f0f0"
PRIMARY_COLOR = "#4a6fa5"
SECONDARY_COLOR = "#166088"
TEXT_COLOR = "#333333"
BUTTON_COLOR = "#4a6fa5"
BUTTON_HOVER = "#3a5a80"

def on_decrypt():
    text = text_input.get("1.0", "end-1c")
    if not text.strip():
        messagebox.showerror("Error", "Please enter the text you want to decrypt.")
        return
    try:
        encryption = data_encryption()
        result = encryption.decrypt(text)
        result_output.config(state=tk.NORMAL)
        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, result)
        result_output.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"An error occured while decrypting: {str(e)}")

def on_enter(e):
    decrypt_button['background'] = BUTTON_HOVER

def on_leave(e):
    decrypt_button['background'] = BUTTON_COLOR

root = tk.Tk()
root.title("Data Encryption")
root.geometry("500x500")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

style = ttk.Style()
style.theme_use('clam')
style.configure('TNotebook', background=BG_COLOR, borderwidth=0)
style.configure('TNotebook.Tab', background=BG_COLOR, padding=[10, 5], font=('Helvetica', 10))
style.map('TNotebook.Tab', background=[('selected', PRIMARY_COLOR)], foreground=[('selected', 'white')])

notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=10, fill='both', expand=True)

frame_decrypt = ttk.Frame(notebook, style='TFrame')
frame_decrypt.pack(fill='both', expand=True)

notebook.add(frame_decrypt, text="Decryption")

title_label = tk.Label(frame_decrypt, 
                      text="Deşifreleme Aracı", 
                      font=('Helvetica', 14, 'bold'), 
                      fg=PRIMARY_COLOR,
                      bg=BG_COLOR)
title_label.pack(pady=(10, 20))

input_frame = tk.Frame(frame_decrypt, bg=BG_COLOR)
input_frame.pack(pady=5, padx=20, fill='x')

text_label = tk.Label(input_frame, 
                     text="Encrypted Text:", 
                     font=('Helvetica', 10), 
                     bg=BG_COLOR,
                     fg=TEXT_COLOR)
text_label.pack(anchor='w')

text_input = tk.Text(input_frame, 
                    height=8, 
                    width=50,
                    font=('Helvetica', 10),
                    wrap=tk.WORD,
                    padx=10,
                    pady=10,
                    bd=0,
                    highlightthickness=1,
                    highlightbackground="#ccc",
                    highlightcolor=PRIMARY_COLOR)
text_input.pack(pady=(5, 10))

button_frame = tk.Frame(frame_decrypt, bg=BG_COLOR)
button_frame.pack(pady=10)

decrypt_button = tk.Button(button_frame,
                          text="Decrypt", 
                          command=on_decrypt,
                          bg=BUTTON_COLOR,
                          fg='white',
                          activebackground=SECONDARY_COLOR,
                          activeforeground='white',
                          relief=tk.FLAT,
                          font=('Helvetica', 10, 'bold'),
                          padx=20,
                          pady=5)
decrypt_button.pack()
decrypt_button.bind("<Enter>", on_enter)
decrypt_button.bind("<Leave>", on_leave)

result_frame = tk.Frame(frame_decrypt, bg=BG_COLOR)
result_frame.pack(pady=5, padx=20, fill='x')

result_label = tk.Label(result_frame, 
                      text="Decrypted Text:", 
                      font=('Helvetica', 10), 
                      bg=BG_COLOR,
                      fg=TEXT_COLOR)
result_label.pack(anchor='w')

result_output = tk.Text(result_frame, 
                       height=8, 
                       width=50,
                       font=('Helvetica', 10),
                       wrap=tk.WORD,
                       padx=10,
                       pady=10,
                       bd=0,
                       highlightthickness=1,
                       highlightbackground="#ccc",
                       highlightcolor=PRIMARY_COLOR,
                       state=tk.DISABLED)
result_output.pack(pady=(5, 20))

root.mainloop()