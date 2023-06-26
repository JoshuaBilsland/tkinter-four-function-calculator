import tkinter as tk

class Calculator:
    def __init__(self):
        self.__window = tk.Tk()
        
        self.__window.title("Four Function Calculator")
        self.__window.configure(bg="black")
        self.__window.minsize(250,400)
       
        self.__display = tk.Entry(self.__window, width=20, font=("Montserrat", 16))
        self.__display.grid(row=0, column=0, columnspan=4, sticky="NSEW")
        
        # Set the parameters each button will have
        #-----------------------------------------
        # Default parameters
        defaultWidth = 3
        defaultColSpan = 1
        sticky = "NSEW"
        
        # Digit specific ones
        digitBg = "gray10"
        digitFg = "ghost white"
        
        # Operator specific ones
        operatorBg = "gray30"
        operatorFg = "ghost white"
        
        # Equals specific ones
        equalsBg = "lime green"
        equalsFg = "ghost white"
        equalsColSpan = 2
        
        buttonParameters = {
            "+": [1, 0, operatorBg, operatorFg, defaultWidth, defaultColSpan, sticky],
            "-": [1, 1, operatorBg, operatorFg, defaultWidth, defaultColSpan, sticky],
            "*": [1, 2, operatorBg, operatorFg, defaultWidth, defaultColSpan, sticky],
            "/": [1, 3, operatorBg, operatorFg, defaultWidth, defaultColSpan, sticky],
            "7": [2, 0, digitBg, digitFg, defaultWidth, defaultColSpan, sticky],
            "8": [2, 1, digitBg, digitFg, defaultWidth, defaultColSpan, sticky],
            "9": [2, 2, digitBg, digitFg, defaultWidth, defaultColSpan, sticky],
            ".": [2, 3, operatorBg, operatorFg, defaultWidth, defaultColSpan, sticky],
            "4": [3, 0, digitBg, digitFg, defaultWidth, defaultColSpan, sticky],
            "5": [3, 1, digitBg, digitFg, defaultWidth, defaultColSpan, sticky],
            "6": [3, 2, digitBg, digitFg, defaultWidth, defaultColSpan, sticky],
            "(": [3, 3, operatorBg, operatorFg, defaultWidth, defaultColSpan, sticky],
            "1": [4, 0, digitBg, digitFg, defaultWidth, defaultColSpan, sticky],
            "2": [4, 1, digitBg, digitFg, defaultWidth, defaultColSpan, sticky],
            "3": [4, 2, digitBg, digitFg, defaultWidth, defaultColSpan, sticky],
            ")": [4, 3, operatorBg, operatorFg, defaultWidth, defaultColSpan, sticky],
            "0": [5, 0, digitBg, digitFg, defaultWidth, defaultColSpan, sticky],
            "CLR": [5, 3, operatorBg, operatorFg, defaultWidth, defaultColSpan, sticky],
            "=": [5, 1, equalsBg, equalsFg, defaultWidth, equalsColSpan, sticky]
        }

        # Create the grid
        #----------------
        for button in buttonParameters:
            parameters = buttonParameters[button]
            self.makeButton(button, *parameters)
        
        # Set weights
        #------------
        self.__window.grid_columnconfigure(0, weight=1)
        self.__window.grid_columnconfigure(1, weight=1)
        self.__window.grid_columnconfigure(2, weight=1)
        self.__window.grid_columnconfigure(3, weight=1)

        self.__window.grid_rowconfigure(0, weight=1)
        self.__window.grid_rowconfigure(1, weight=1)
        self.__window.grid_rowconfigure(2, weight=1)
        self.__window.grid_rowconfigure(3, weight=1)
        self.__window.grid_rowconfigure(4, weight=1)      
        self.__window.grid_rowconfigure(5, weight=1)             
        
    def makeButton(self, text, row, column, bg, fg, width, col_span, sticky):
        button = tk.Button(text=text, bg=bg, fg=fg, width=width)
        button.grid(row=row, column=column, columnspan=col_span, sticky=sticky)
        
    def display(self):
        self.__window.mainloop()
        
if __name__ == "__main__":    
    calculator = Calculator()
    calculator.display()