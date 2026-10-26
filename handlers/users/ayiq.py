from aiogram import Router, filters, types
rt = Router()

@rt.message(filters.Command("ayiq"))
async def ayiq(msg: types.Message):
    await msg.answer("salom")
    await msg.answer_photo("https://th.bing.com/th/id/R.2e93ffea201a0cdc4f391639546e1e16?rik=g2VDs9F9uOE96Q&pid=ImgRaw&r=0")