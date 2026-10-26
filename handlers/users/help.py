from aiogram import Router, filters, types

st = Router()

@st.message(filters.Command("helps"))
async def helps(mseg: types.Message):
    n =  "qanday yordam kerak\n"
    n += "bizda bor funksiyalar:\n"
    n += "/start\n"
    n += "/helps\n"
    n += "/ayiq\n"
    n += "/mushuk\n"
    n += "/koniseg\n"
    n += "/narsa\n"
    n += "/tugma\n"
    n += "/car\n"

    await mseg.answer(n)