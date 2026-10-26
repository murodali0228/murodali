
from aiogram import Router, types
rt = Router()

@rt.message()
async def test(msg: types.Message):

    ism = msg.chat.first_name
    if msg.from_user.last_name:
        familya = msg.chat.last_name
    else:
        familya = "mavjud emas"
    n = "siz xaqingizda malumot👇🏻\n"
    n += f"ismingiz: {ism}\n"
    n += f"familyangiz: {familya}\n"
    await msg.answer(n)
    if msg.from_user.username:
        username = msg.from_user.username
    else:
        username = "mavjud emas"
    n = f"username: {username}"
    await msg.answer(n)



