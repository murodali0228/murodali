from aiogram import Router, filters, types
from keyboards.replyKeyboard.tugmaKeyboard import tugma

rt = Router()


@rt.message(filters.Command("tugma"))
async def button(msg: types.Message):
    await msg.answer("xohlagan tugmangizni bosing!", reply_markup=tugma())


@rt.message()
async def button(msg: types.Message):
    if msg.text == "salom":
        await msg.answer("alik")
    elif msg.text == "qalesan":
        await msg.answer("yaxshi")
    elif msg.text == "dasturchimisan":
        await msg.answer("ha albatta")
    else:
        await msg.answer("mavjud bo'lmagan tugma bosildi")
