from aiogram.utils.keyboard import ReplyKeyboardBuilder

def tugma():
    b = ReplyKeyboardBuilder()
    b.button(text="salom")
    b.button(text="qalesan")
    b.button(text="dasturchimisan")
    b.button(text="telefon nomer" , request_contact=True)
    b.button(text="lakatsya tashlash" , request_location=True)
    b.adjust(3)

    return b.as_markup(resize_keyboard=True)