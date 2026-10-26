from aiogram import Router, types, filters
from filters.prevate import PrivateFilter

rt = Router()

@rt.message(PrivateFilter(), filters.Command("lichka"))
async def gaplash(msg: types.Message):
    await msg.answer("aliiik")
