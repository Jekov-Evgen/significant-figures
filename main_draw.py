from tkinter import ttk
from tkinter import *
from calculation_of_numbers import Calculation

class MainWindow:
    def __init__(self) -> None:
        pass
    
    
    def draw(self):
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid
        
        ttk.Label(text="Введите ваше число: ", font="30").grid(row=0, column=0, padx=10, pady=10)
        
        self.number = ttk.Entry(width=100)
        self.number.grid(row=1, column=0, padx=10, pady=10)
        
        ttk.Button(text=f"Узнать значущие числа!", 
                   width=100, command=self.processing).grid(row=2, column=0, padx=10, pady=10)
        
        root.mainloop()
        
    def processing(self):
        calculation = Calculation()
        cal_numebr = self.number.get()
            
        result = calculation.counting_significant(cal_numebr)
            
        root = Toplevel()
            
        Label(root, text=f"Ваши значущие цифры: {result}", 
                font="30").grid(row=0, column=0, padx=10, pady=10)
            
        Button(root, text="OK", 
               command=root.destroy, width=100).grid(row=1, column=0, padx=10, pady=10)