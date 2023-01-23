from tkinter import Frame, Label, Entry, Button, Listbox
from .functions import AppFunctions

class AppView(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_view()

    def create_view(self) -> None:
        '''
        Create the app view
        '''
        Label(self, text='Newton interpolation').grid(column=0, row=0, columnspan=2)
        Label(self, text='x:').grid(column=0, row=1)
        x = Entry(self)
        x.grid(column=0, row=2)
        AppFunctions.get_references(x_entry=x)
        Label(self, text='f(x):').grid(column=1, row=1)
        fx = Entry(self)
        fx.grid(column=1, row=2)
        AppFunctions.get_references(fx_entry=fx)
        Button(self, text='Add values', command=AppFunctions.add_values_list).grid(column=0, row=3)
        list_valours = Listbox(self, justify='center')
        list_valours.grid(column=0, row=4, columnspan=2)
        AppFunctions.get_references(list_box=list_valours)
        Label(self, text='Find value:').grid(column=0, row=5)
        find_value = Entry(self)
        find_value.grid(column=1, row=5)
        AppFunctions.get_references(find_x=find_value)
        Button(self, text='Calculate', command=AppFunctions.take_values).grid(column=0, row=6, columnspan=2)
        result = Label(self, text='Approach:')
        result.grid(column=0, row=7, columnspan=2)
        AppFunctions.get_references(result_label=result)
