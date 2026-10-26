from aiogram.utils.keyboard import InlineKeyboardBuilder

def telefon():
    b = InlineKeyboardBuilder()
    telefonlar = ["ayfon", "samsung", "poco", "redmi"]
    for telefon in telefonlar:
        b.button(text=telefon, callback_data="telefon")
    b.adjust(2)
    return b.as_markup()
def rang():
    b = InlineKeyboardBuilder()
    ranglar = ["oq", "qora", "kok", "qora", "qizil", "sabzi rang🗿"]
    for rang in ranglar:
        b.button(text=rang, callback_data="rang")
    b.adjust(3)
    return b.as_markup()
def narxi():
    b = InlineKeyboardBuilder()
    narxlar = ["200$", "500$", "1000$", "700$"]
    for narx in narxlar:
        b.button(text=narx, callback_data="narxi")
    b.adjust(2)
    return b.as_markup()
def yili():
    b = InlineKeyboardBuilder()
    yillar = ["2020", "2022", "2023", "2024", "2025", "2026"]
    for yil in yillar:
        b.button(text=yil, callback_data="yili")
    b.adjust(3)
    return b.as_markup()
def end():
    b = InlineKeyboardBuilder()
    tugash = ["xaridingiz uchun raxmat!"]
    for endd in tugash:
        b.button(text=endd, callback_data="end")
    b.adjust(1)
    return b.as_markup()