from aiogram import Router, filters, types
from keyboards.replyKeyboard.narsaKeyboard import narsa

rt = Router()


@rt.message(filters.Command("narsa"))
async def narsalar(msg: types.Message):
    await msg.answer("xohlagan tugmangizni bosing!", reply_markup=narsa())


@rt.message()
async def narsalar(msg: types.Message):
    if msg.text == "olma":
        await msg.answer("qizil")
    elif msg.text == "banan":
        await msg.answer("sariq")
    elif msg.text == "nech pul":
        await msg.answer("10.000")
    else:
        await msg.answer("mavjud bo'lmagan tugma bosildi")