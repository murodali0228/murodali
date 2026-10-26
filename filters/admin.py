from aiogram import filters, types, Bot
from config.settings import ADMINS

class AdminGroupFilter(filters.BaseFilter):
    async def __call__(self, msg: types.Message, bot: Bot):
        if not msg.from_user:
            return False
        try:
            user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
            return user.status in ["administrator", "creator"]
        except Exception:
            return False

class AdminFilter(filters.BaseFilter):
    async def __call__(self, msg: types.Message):
        if not msg.from_user:
            return False
        return str(msg.from_user.id) in ADMINS
