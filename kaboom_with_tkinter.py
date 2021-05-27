import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        # We are inheriting methods from the 
        # tkinter.Frame class and passing it the root as an arg
        super().__init__(master)
        self.widgets = []
        self.setup()
        # Pack Application object onto the window
        self.pack()

    def setup(self) -> None:
        """ Method for setting up objects"""
        death_button = tk.Button(self, text="DONT PRESS THIS BUTTON!", bg='red', fg='white', command=self.explosion)
        self.widgets.append(death_button)
        for widget in self.widgets:
            widget.pack()

    @staticmethod
    def explosion():
        """ This method explodes"""
        print("KABOOM!")


if __name__ == "__main__":
    # Create window and set it to root
    root = tk.Tk()
    # Create Application object
    app = Application(root)
    # Run mainloop method from the tkinter.Frame superclass of the Application class
    app.mainloop()
