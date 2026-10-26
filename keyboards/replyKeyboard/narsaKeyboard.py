from aiogram.utils.keyboard import ReplyKeyboardBuilder

def narsa():
    b = ReplyKeyboardBuilder()
    b.button(text="olma")
    b.button(text="banan")
    b.button(text="nech pul")
    b.adjust(3)

    return b.as_markup(resize_keyboard=True)