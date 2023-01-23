from tkinter import Entry, Listbox, Label, messagebox, END
from .newton_interpolation import calculate_newton_interpolation

class AppFunctions:
    _x_entry_ref:Entry = None
    _fx_entry_ref:Entry = None
    _list_ref:Listbox = None
    _find_x_entry_ref:Entry = None
    _result_ref:Label = None

    @classmethod
    def get_references(cls,
        x_entry=None,
        fx_entry=None,
        list_box:Listbox=None,
        find_x=None,
        result_label=None,
        ) -> None:
        if x_entry: cls._x_entry_ref = x_entry
        if fx_entry: cls._fx_entry_ref = fx_entry
        if list_box: cls._list_ref = list_box
        if find_x: cls._find_x_entry_ref = find_x
        if result_label: cls._result_ref = result_label

    @classmethod
    def add_values_list(cls) -> None:
        '''
        Add values from entries introduced by user in list
        '''
        try:
            x = float(cls._x_entry_ref.get())
            fx = float(cls._fx_entry_ref.get())
        except ValueError:
            messagebox.showerror('Error', 'Please enter numeric values')
            return
        cls._list_ref.insert(END, f'{x} - {fx}')
        cls._x_entry_ref.delete(0, END)
        cls._fx_entry_ref.delete(0, END)

    @classmethod
    def take_values(cls) -> None:
        '''
        Take the values to calculate interpolation
        '''
        values = cls._list_ref.get(0, END)
        if not values or not len(values) >= 3:
            messagebox.showwarning('Warning', 'Not enough values to perform the operation')
            return
        try:
            find_value = int(cls._find_x_entry_ref.get())
        except Exception as e:
            messagebox.showerror('Error', 'Please enter the value you want to search for')
            return
        x, fx = zip(*[map(float, value.split(' - ')) for value in values])
        x, fx = list(x), list(fx)
        res = calculate_newton_interpolation(find_value, x, fx)
        cls._result_ref.configure(text=f'Approach: {res}')
        