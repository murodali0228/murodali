from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo, SwitchInlineQueryChosenChat, CopyTextButton

def query():
    b = InlineKeyboardBuilder()
    b.button(text="assalomu alaykum", callback_data="va alaykum assalom")
    b.button(text="python", url="https://t.me/python_dg")
    b.button(text="admin gurpa", url="https://t.me/+PeR0Ry9zz1tiYzBi")
    b.button(text="instagram", web_app=WebAppInfo(url="https://www.instagram.com"))
    b.button(text="youtube", web_app=WebAppInfo(url="https://www.youtube.com/"))
    b.button(text="ulashish", switch_inline_query="foydalanish tekin")
    b.button(text="faqat kanal", switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(
        query="ushbu kanalga tashlash",
        allow_channel_chats=True,
    ))
    b.button(text="sher", copy_text=CopyTextButton(text="yurtim sen zorsan"))
    b.button(text="card number", copy_text=CopyTextButton(text="9860 6219 8120 1200"))
    b.adjust(1, 2)
    return b.as_markup()
