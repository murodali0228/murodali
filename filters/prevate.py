from aiogram import filters, types


class PrivateFilter(filters.BaseFilter):
    async def __call__(self, msg: types.Message):
        return msg.chat.type in ["private"]
