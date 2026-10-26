from aiogram.utils.keyboard import ReplyKeyboardBuilder

cars1 = ["Cobalt", "Nexia", "Malibu", "Gentra"]
colors1 = ["red", "blue", "white", "black"]
years1 = ["2023-2024", "2020-2022", "2015-2019", "2010-2014"]

def car():
    b = ReplyKeyboardBuilder()
    for c in cars1:
        b.button(text=c)
    b.adjust(2)
    return b.as_markup(resize_keyboard=True)

def colors2():
    b = ReplyKeyboardBuilder()
    for col in colors1:
        b.button(text=col)
    b.adjust(2)
    return b.as_markup(resize_keyboard=True)

def year():
    b = ReplyKeyboardBuilder()
    for y in years1:
        b.button(text=y)
    b.adjust(2)
    return b.as_markup(resize_keyboard=True)
