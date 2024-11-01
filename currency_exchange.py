import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event):
    code = t_combobox.get()
    name = dict_names[code]
    c_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    if t_code and b_code:
        try:
            answer = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            answer.raise_for_status()
            data = answer.json()
            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_name = dict_names[t_code]
                b_name = dict_names[b_code]
                mb.showinfo(title='Курс обмена', message=f'Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}')
            else:
                mb.showerror(title='ОШИБКА!', message=f'Валюта {t_code} не найдена')
        except Exception as e:
            mb.showerror(title='ОШИБКА!', message=f'Произошла ошибка: {e}')
    else:
        mb.showwarning(title='ВНИМАНИЕ!', message='Введите код валюты!')


dict_names = {
    'RUB': 'Российский рубль',
    'USD': 'Американский доллар',
    'EUR': 'Евро',
    'GBP': 'Британский фунт стерлингов',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахский тенге',
    'UZS': 'Узбекский сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар'}

window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x280')

Label(text='Базовая валюта').pack(padx=10, pady=10)

b_combobox = ttk.Combobox(values=list(dict_names.keys()))
b_combobox.pack(padx=10, pady=10)

Label(text='Целевая валюта').pack(padx=10, pady=10)

t_combobox = ttk.Combobox(values=list(dict_names.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind('<<ComboboxSelected>>', update_c_label)


c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

Button(text='Получить курс обмена', command=exchange).pack(padx=10, pady=10)

window.mainloop()
