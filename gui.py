import tkinter as tk
from tkinter import ttk
from api import get_rates
from converter import convert
from config import base_currency

def run_app():
    root = tk.Tk()
    root.title("Currency  Converter")

    tk.Label(root, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
    entry_amount = tk.Entry(root)
    entry_amount.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="From:").grid(row=1, column=0, padx=5, pady=5)
    combo_from = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY"])
    combo_from.set("USD")
    combo_from.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="To:").grid(row=2, column=0, padx=5, pady=5)
    combo_to = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY"])
    combo_to.set("EUR")
    combo_to.grid(row=2, column=1, padx=5, pady=5)

    label_result = tk.Label(root, text="Result:")
    label_result.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    def on_convert():
        try:
            amount = float(entry_amount.get())
            from_cur = combo_from.get()
            to_cur = combo_to.get()
            rates = get_rates(base_currency)
            result = convert(amount, from_cur, to_cur, rates, base_currency)

            if result is not None:
                label_result.config(text = f"{amount}, {from_cur} = {result:.2f} {to_cur}")
            
            else:
                label_result.config(text = "Error with convertation.")

        except ValueError:
            label_result.config(text = "Incorrect sum")

    btn_convert = tk.Button(root, text="Convert", command=on_convert)
    btn_convert.grid(row=3, column=3, columnspan=2, pady=10)

    root.mainloop()