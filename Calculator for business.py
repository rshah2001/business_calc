import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import datetime

class ProfitCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Profit Calculator")
        self.geometry("600x600")
        self.configure(bg="#f0f0f0")  # Set background color

        # Create a custom style for buttons
        self.style = ttk.Style()
        self.style.configure("Custom.TButton", font=("Helvetica", 12))

        self.starting_balance = 0.0
        self.balance = self.starting_balance
        self.money_in = 0.0
        self.money_out = 0.0
        self.current_input = ""
        self.operation_history = []

        self.result_var = tk.StringVar()
        self.money_in_var = tk.StringVar()
        self.money_out_var = tk.StringVar()

        self.result_var.set(f"Balance: ${self.balance:.2f}")
        self.money_in_var.set(f"Money In: ${self.money_in:.2f}")
        self.money_out_var.set(f"Money Out: ${self.money_out:.2f}")

        self.create_ui()
        self.bind("<KeyPress>", self.on_key_press)

    def create_ui(self):
        # Main Frame
        main_frame = ttk.Frame(self, padding=20)
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title Label
        result_label = ttk.Label(main_frame, textvariable=self.result_var, font=("Helvetica", 24, "bold"), background="#f0f0f0")
        result_label.grid(row=0, column=0, columnspan=4, pady=(10, 20))

        # Money In Label
        money_in_label = ttk.Label(main_frame, textvariable=self.money_in_var, font=("Helvetica", 14), background="#f0f0f0")
        money_in_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

        # Money Out Label
        money_out_label = ttk.Label(main_frame, textvariable=self.money_out_var, font=("Helvetica", 14), background="#f0f0f0")
        money_out_label.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky=tk.W)

        # Buttons Frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=4, pady=20)

        # Create a grid of buttons
        buttons = [
            ("1", 1), ("2", 2), ("3", 3),
            ("4", 4), ("5", 5), ("6", 6),
            ("7", 7), ("8", 8), ("9", 9),
            ("   ", ""), ("0", 0),
        ]

        row, col = 0, 0
        for (text, value) in buttons:
            if text == "   ":
                ttk.Label(button_frame, text=text, width=5, style="Custom.TButton").grid(row=row, column=col, padx=5, pady=5)
            else:
                ttk.Button(button_frame, text=text, width=5, style="Custom.TButton",
                           command=lambda v=value: self.on_number_click(v)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Operator Buttons
        ttk.Button(button_frame, text="Add", width=5, style="Custom.TButton", command=self.add_money).grid(row=3, column=0, padx=5, pady=5)
        ttk.Button(button_frame, text="Subtract", width=7, style="Custom.TButton", command=self.subtract_money).grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(button_frame, text="Clear", width=5, style="Custom.TButton", command=self.clear).grid(row=3, column=2, padx=5, pady=5)
        ttk.Button(button_frame, text="Backspace", width=7, style="Custom.TButton", command=self.backspace).grid(row=3, column=3, padx=5, pady=5)

        # Total Buttons
        ttk.Button(button_frame, text="Total Profit", width=12, style="Custom.TButton", command=self.show_total_profit).grid(row=4, column=0, padx=5, pady=10)
        ttk.Button(button_frame, text="Total Money Out", width=12, style="Custom.TButton", command=self.show_total_money_out).grid(row=4, column=1, columnspan=2, padx=5, pady=10)
        ttk.Button(button_frame, text="End Day", width=12, style="Custom.TButton", command=self.end_day).grid(row=4, column=3, padx=5, pady=10)

        # Starting Balance Entry
        ttk.Label(main_frame, text="Starting Balance: $", font=("Helvetica", 14), background="#f0f0f0").grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky=tk.W)
        self.starting_balance_entry = ttk.Entry(main_frame, width=10, font=("Helvetica", 14))
        self.starting_balance_entry.grid(row=5, column=2, padx=5, pady=10, sticky=tk.W)
        ttk.Button(main_frame, text="Set Starting Balance", width=18, style="Custom.TButton", command=self.set_starting_balance).grid(row=5, column=3, padx=5, pady=10, sticky=tk.W)

        # Calculate Money In Button
        ttk.Button(main_frame, text="Money In", width=20, style="Custom.TButton", command=self.calculate_money_in_today).grid(row=6, column=0, columnspan=4, padx=5, pady=10)

    def on_number_click(self, number):
        if number == "   ":
            return
        elif number == "0" and self.current_input == "0":
            return
        self.current_input += str(number)
        self.update_display()

    def on_key_press(self, event):
        key = event.char
        if key.isdigit() or key == '.':
            self.current_input += key
            self.update_display()
        elif key == 'a':
            self.add_money()
        elif key == 's':
            self.subtract_money()
        elif key == 'c':
            self.clear()
        elif key == 'b':
            self.backspace()

    def update_display(self):
        if not self.current_input:
            self.result_var.set(f"Balance: ${self.balance:.2f}")
        else:
            self.result_var.set(f"Balance: ${self.current_input}")

    def add_money(self):
        try:
            amount = float(self.current_input)
            self.money_in += amount
            self.balance += amount
            self.operation_history.append(f"+{amount:.2f}")
            self.current_input = ""
            self.update_display()
            self.update_money_in_out()
        except ValueError:
            pass

    def subtract_money(self):
        try:
            amount = float(self.current_input)
            self.money_out += amount
            self.balance -= amount
            self.operation_history.append(f"-{amount:.2f}")
            self.current_input = ""
            self.update_display()
            self.update_money_in_out()
        except ValueError:
            pass

    def clear(self):
        self.operation_history = []
        self.balance = self.starting_balance
        self.money_in = 0.0
        self.money_out = 0.0
        self.current_input = ""
        self.update_display()
        self.update_money_in_out()

    def backspace(self):
        if self.current_input:
            self.current_input = self.current_input[:-1]
            self.update_display()

    def update_money_in_out(self):
        self.money_in_var.set(f"Money In: ${self.money_in:.2f}")
        self.money_out_var.set(f"Money Out: ${self.money_out:.2f}")

    def set_starting_balance(self):
        try:
            starting_balance = float(self.starting_balance_entry.get())
            self.starting_balance = starting_balance
            self.balance = starting_balance
            self.clear()
            self.starting_balance_entry.delete(0, 'end')
        except ValueError:
            pass

    def show_total_profit(self):
        total_profit = self.money_in - self.money_out
        tkinter.messagebox.showinfo("Total Profit", f"Total Profit: ${total_profit:.2f}")

    def show_total_money_out(self):
        tkinter.messagebox.showinfo("Total Money Out", f"Total Money Out: ${self.money_out:.2f}")

    def end_day(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = f"profit_data_{current_date}.txt"

        with open(filename, "a") as file:
            file.write(f"Date: {current_date}\n")
            file.write(f"Starting Balance: {self.starting_balance:.2f}\n")
            file.write(f"Operations: {', '.join(self.operation_history)}\n")
            file.write(f"Total Profit: {self.money_in - self.money_out:.2f}\n\n")

        tkinter.messagebox.showinfo("End Day", "Day ended. Data saved.")

    def calculate_money_in_today(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        starting_balance_today = self.starting_balance
        money_in_today = 0.0

        for operation in self.operation_history:
            if operation.startswith("+"):
                money_in_today += float(operation[1:])

        tkinter.messagebox.showinfo("Money In Today", f"Money In Today ({current_date}): ${money_in_today - starting_balance_today:.2f}")


if __name__ == "__main__":
    app = ProfitCalculator()
    app.mainloop()
