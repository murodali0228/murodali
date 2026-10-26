from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (
WebAppInfo,KeyboardButtonRequestChat,KeyboardButtonRequestUsers
)

def reply_test(): # 1 usage
    b = ReplyKeyboardBuilder()
    b.button(text="you tube", web_app=WebAppInfo(url="https://www.youtube.com/"))
    b.button(text="telefon", request_contact=True)
    b.button(text="lokatsiya", request_location=True)
    b.button(text="user va botlar", request_users=KeyboardButtonRequestUsers(
        request_id=1,
    ))
    b.button(text="user", request_users=KeyboardButtonRequestUsers(
        request_id=2,
        user_is_bot=False
    ))
    b.button(text="bot", request_users=KeyboardButtonRequestUsers(
        request_id=3,
        user_is_bot=True
    ))
    b.button(text="chat", request_chat=KeyboardButtonRequestChat(
        request_id=4,
        chat_is_channel=True
    ))
    b.button(text="gurpa", request_chat=KeyboardButtonRequestChat(
        request_id=5,
        chat_is_channel=False
    ))
    b.button(text="premium", request_users=KeyboardButtonRequestUsers(
        request_id=6,
        user_is_premium=False
    ))
    b.button(text="quantity", request_users=KeyboardButtonRequestUsers(
        request_id=7,
        max_quantity=7
    ))
    b.button(text="username", request_chat=KeyboardButtonRequestChat(
        request_id=8,
        chat_is_channel=False,
        chat_has_username=False
    ))
    b.button(text="member", request_chat=KeyboardButtonRequestChat(
        request_id=10,
        chat_is_channel=False,
        bot_is_member=False
    ))
    b.button(text="created", request_chat=KeyboardButtonRequestChat(
        request_id=10,
        chat_is_channel=False,
        chat_is_created=False
    ))

    b.adjust(3)
    return b.as_markup(resize_keyboard=True)

