import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def exchange():
    code = combobox.get()
    if code:

        try:
            answer = requests.get('https://open.er-api.com/v6/latest/USD')
            answer.raise_for_status()
            data = answer.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                mb.showinfo(title='Курс обмена', message=f'Курс: {exchange_rate:.2f} за 1$')
            else:
                mb.showerror(title='ОШИБКА!', message=f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror(title='ОШИБКА!', message=f'Произошла ошибка: {e}')
    else:
        mb.showwarning(title='ВНИМАНИЕ!', message='Введите код валюты!')


window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x180')

Label(text='Выберите код валюты').pack(padx=10, pady=10)

list_codes = ['RUB', 'EUR', 'GBP', 'JPY', 'CNY', 'KZT', 'UZS', 'CHF', 'AED', 'CAD']
combobox = ttk.Combobox(values=list_codes)
combobox.pack(padx=10, pady=10)

Button(text='Получить курс обмена в долларах', command=exchange).pack(padx=10, pady=10)

window.mainloop()
