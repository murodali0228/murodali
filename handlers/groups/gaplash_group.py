from aiogram import Router, types, filters
from filters.group import GroupFilter

rt = Router()

@rt.message(GroupFilter(), filters.Command("sozla"))
async def gaplash(msg: types.Message):
    await msg.answer("saloom")
