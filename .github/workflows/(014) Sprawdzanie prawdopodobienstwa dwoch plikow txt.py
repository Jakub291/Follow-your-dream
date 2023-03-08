import string
import tkinter as tk
from tkinter import filedialog, messagebox

# Funkcja do wczytywania zawartości pliku
def load_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        return text

# Funkcja do usuwania znaków interpunkcyjnych i białych znaków z tekstu
def clean_text(text):
    text = text.lower() # zamiana wszystkich liter na małe
    text = text.translate(str.maketrans("", "", string.punctuation)) # usunięcie znaków interpunkcyjnych
    text = text.replace(" ", "") # usunięcie białych znaków
    return text

# Funkcja do obliczenia procentowego stopnia podobieństwa między dwoma tekstami
def calculate_similarity(text1, text2):
    clean_text1 = clean_text(text1)
    clean_text2 = clean_text(text2)
    
    # Obliczenie liczby słów występujących w obu tekstach
    common_words = len(set(clean_text1.split()) & set(clean_text2.split()))
    
    # Obliczenie stopnia podobieństwa jako procent wspólnych słów z całkowitej liczby słów
    similarity = common_words / ((len(clean_text1.split()) + len(clean_text2.split())) / 2) * 100
    return similarity

# Funkcja do wywołania okna dialogowego do wyboru plików
def choose_file(text_widget):
    file_path = filedialog.askopenfilename(title="Wybierz plik")
    if file_path:
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, load_file(file_path))

# Funkcja do obliczenia stopnia podobieństwa i wyświetlenia wyniku
def calculate_button():
    file1 = text1.get("1.0", tk.END)
    file2 = text2.get("1.0", tk.END)
    similarity = calculate_similarity(file1, file2)
    messagebox.showinfo("Wynik", "Stopień podobieństwa wynosi {:.2f}%".format(similarity))

# Stworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Porównanie plików tekstowych")

# Dodanie przycisków i pól tekstowych
label1 = tk.Label(root, text="Plik 1")
label1.grid(row=0, column=0, padx=5, pady=5)
text1 = tk.Text(root, width=50, height=10)
text1.grid(row=1, column=0, padx=5, pady=5)

label2 = tk.Label(root, text="Plik 2")
label2.grid(row=0, column=1, padx=5, pady=5)
text2 = tk.Text(root, width=50, height=10)
text2.grid(row=1, column=1, padx=5, pady=5)

button1 = tk.Button(root, text="Wybierz plik 1", command=lambda: choose_file(text1))
button1.grid(row=2, column=0, padx=5, pady=5)

button2 = tk.Button(root, text="Wybierz plik 2", command=lambda: choose_file(text2))
button2.grid(row=2, column=1, padx=5, pady=5)

button3 = tk.Button(root, text="Oblicz podobieństwo", command=calculate_button)
button3.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
