from aiogram import Router, filters, types
from keyboards.inlineKeyboard.queryKeyboard import query
rt = Router()

@rt.message(filters.Command("shaffof"))
async  def shaffof(msg:types.Message):
    await msg.answer("tugmalardan birini bosing", reply_markup=query())