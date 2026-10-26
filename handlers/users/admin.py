from aiogram import Router, types, filters
from filters.admin import AdminFilter

rt = Router()

@rt.message(AdminFilter(), filters.Command("admin"))
async def gaplash(msg: types.Message):
    await msg.answer("admin ekansiz aa😁")