import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event):
    code = combobox.get()
    name = dict_names[code]
    c_label.config(text=name)


def exchange():
    code = combobox.get()
    if code:

        try:
            answer = requests.get('https://open.er-api.com/v6/latest/USD')
            answer.raise_for_status()
            data = answer.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                c_name = dict_names[code]
                mb.showinfo(title='Курс обмена', message=f'Курс: {exchange_rate:.2f} {c_name} за 1$')
            else:
                mb.showerror(title='ОШИБКА!', message=f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror(title='ОШИБКА!', message=f'Произошла ошибка: {e}')
    else:
        mb.showwarning(title='ВНИМАНИЕ!', message='Введите код валюты!')


dict_names = {
    'RUB': 'Российский рубль',
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
window.geometry('360x180')

Label(text='Выберите код валюты').pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(dict_names.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind('<<ComboboxSelected>>', update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

Button(text='Получить курс обмена в долларах', command=exchange).pack(padx=10, pady=10)

window.mainloop()
