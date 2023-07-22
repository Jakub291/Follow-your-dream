import tkinter as tk
from tkinter import messagebox, filedialog

def split_text(text):
    words = text.split()  # Podziel tekst na słowa

    # Utwórz instrukcje INSERT SQL
    sql_statements = []
    for word in words:
        sql_statements.append(f"INSERT INTO words (word) VALUES ('{word}');")

    return sql_statements

def save_as_sql():
    filepath = filedialog.askopenfilename(filetypes=[("Pliki tekstowe", "*.txt")])
    if not filepath:
        return

    try:
        with open(filepath, "r") as file:
            text = file.read()

        sql_statements = split_text(text)

        if len(sql_statements) == 0:
            messagebox.showwarning("Błąd", "Brak słów do zapisania.")
            return

        sql_filepath = filedialog.asksaveasfilename(defaultextension=".sql", filetypes=[("Pliki SQL", "*.sql")])
        if not sql_filepath:
            return

        with open(sql_filepath, "w") as file:
            file.write("\n".join(sql_statements))

        messagebox.showinfo("Sukces", "Plik SQL został pomyślnie zapisany.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd przy zapisywaniu pliku SQL:\n{str(e)}")

def main():
    window = tk.Tk()
    window.title("Podział tekstu na słowa")

    select_file_button = tk.Button(window, text="Wybierz plik", command=save_as_sql)
    select_file_button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
