from aiogram import Router, filters, types
from keyboards.replyKeyboard.replyTestKeyboard import reply_test
rt = Router()

@rt.message(filters.Command("test"))
async def reply_test1(msg: types.Message):
    await msg.answer("xoxlagan tugmani bosing!", reply_markup=reply_test())

