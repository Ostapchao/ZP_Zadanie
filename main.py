import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def spusti_program():
    # Generovanie náhodného poľa
    original_numbers = [random.randint(0, 100) for _ in range(30)]
    filtered_numbers = [num for num in original_numbers if 30 <= num <= 70]

    # Výsledky zobrazené v okne
    result_text.set(f"Generované čísla: {original_numbers}\n"
                    f"Filtrované čísla (30-70): {filtered_numbers}")

    # Zobrazenie grafu
    plt.figure(figsize=(8, 4))
    plt.bar(range(len(filtered_numbers)), filtered_numbers, color='#4caf50', alpha=0.8)
    plt.title("Filtrované čísla (30-70)", fontsize=14)
    plt.xlabel("Index", fontsize=12)
    plt.ylabel("Hodnota", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    fig = plt.gcf()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, pady=20)


# Generovaný návrh z Tkinter Designer
window = tk.Tk()
window.title("Programovacie techniky")
window.geometry("800x600")
window.configure(bg="#f0f4f8")  # Jemné svetlé pozadie

# Hlavička
tk.Label(window, text="Programovacie techniky", font=("Helvetica", 20, "bold"), bg="#f0f4f8", fg="#2c3e50").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 columnspan=2,
                                                                                                                 pady=20)

# Podnadpis
tk.Label(window, text="Ostap Hryniv", font=("Helvetica", 12), bg="#f0f4f8", fg="#34495e").grid(row=1, column=0,
                                                                                                  columnspan=2)
tk.Label(window, text="Zadanie úlohy: Vygenerovať a spracovať náhodné čísla", font=("Helvetica", 12), bg="#f0f4f8",
         fg="#34495e").grid(row=2, column=0, columnspan=2, pady=5)

# Tlačidlo na spustenie
tk.Button(window, text="Spustiť program", command=spusti_program, font=("Helvetica", 14), bg="#3498db", fg="white",
          relief="flat", width=20, height=2, bd=0, padx=10, pady=5).grid(row=3, column=0, columnspan=2, pady=30)

# Výsledky
result_text = tk.StringVar()
tk.Label(window, textvariable=result_text, font=("Helvetica", 10), wraplength=600, justify="left", bg="#f0f4f8",
         fg="#2c3e50").grid(row=4, column=0, columnspan=2)

# Spustenie aplikácie
window.mainloop()
