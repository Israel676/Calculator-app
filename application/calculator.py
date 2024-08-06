import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        
        self.expression = ""
        
        self.input_text = tk.StringVar()
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(expand=True, fill='both')
        
        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=30, insertwidth=4, width=14, justify='right')
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(expand=True, fill='both')
        
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(expand=True, fill='both')
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]
        
        i = 0
        for row in range(4):
            for col in range(4):
                button = tk.Button(self.buttons_frame, text=buttons[i], font=('arial', 18, 'bold'), bd=1, relief='ridge', command=lambda x=buttons[i]: self.on_button_click(x))
                button.grid(row=row, column=col, sticky='nsew')
                i += 1
                
        for row in range(4):
            self.buttons_frame.grid_rowconfigure(row, weight=1)
        for col in range(4):
            self.buttons_frame.grid_columnconfigure(col, weight=1)
        
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set(self.expression)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.input_text.set("")
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
