from aiogram import types, filters, Router, Bot
rt = Router()
kanallar = [-5426920279, -1004289823337,-1003945689423]
@rt.message()
async def majburla(msg: types.Message, bot: Bot):
    tuhfalar = True
    for kanal in kanallar:
        user = await bot.get_chat_member(kanal, msg.from_user.id)
        if user.status in ["creator", "administrator", "member"]:
            tuhfalar=True
            break
        else:
            tuhfalar=False
            break
    if tuhfalar:
        await msg.answer("rahmat, barcha kanalda borsiz!")
    else:
        await msg.answer("botda foydalanish uchun barcha kanllarga a`zo bo'ling!!\n")
        n = "1-kanal👇\n"
        n += "https://t.me/+Pq8E7Du9unFiZDcy\n"
        n += "2-kanal👇\n"
        n += "https://t.me/+815rd6IVB9xjZDgy\n"
        n += "3-guruh👇\n"
        n += "https://t.me/+-BU63lrwfa83MThi\n"
        await msg.answer(n)