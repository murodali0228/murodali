from  aiogram import  filters,types

class GroupFilter(filters.BaseFilter):
    async def __call__(self, msg: types.Message):
        return msg.chat.type in ["supergroup", "group"]