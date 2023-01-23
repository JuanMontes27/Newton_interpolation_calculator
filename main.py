from tkinter import Tk, Frame, TOP, BOTH, NSEW
from src.view import AppView

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Newton interpolation')

        # Create container view calculator
        container_view = Frame(self)
        container_view.pack(
            side=TOP,
            fill=BOTH,
            expand=True,
        )

        # Responsive configurations
        container_view.grid_columnconfigure(0, weight=1)
        container_view.grid_rowconfigure(0, weight=1)

        AppView(container_view).grid(column=0, row=0, sticky=NSEW)

if __name__ == '__main__':
    app = Manager()
    app.resizable(0, 0)
    app.mainloop()
