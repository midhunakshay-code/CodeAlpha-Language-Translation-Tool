import tkinter as tk
from deep_translator import GoogleTranslator

def translate_text():
    text = input_box.get("1.0", tk.END).strip()

    translated = GoogleTranslator(
        source='auto',
        target='ta'
    ).translate(text)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, translated)

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("500x400")

tk.Label(root, text="Enter Text").pack()

input_box = tk.Text(root, height=5, width=50)
input_box.pack()

tk.Button(root, text="Translate", command=translate_text).pack(pady=10)

tk.Label(root, text="Translated Text").pack()

output_box = tk.Text(root, height=5, width=50)
output_box.pack()

root.mainloop()