from aiogram import Router, filters, types
rt = Router()

@rt.message()
async def reklama(msg: types.Message):
    if msg.caption_entities:
        reklamalar = ["mention", "url"]
        for i in msg.caption_entities:
            if i.type in reklamalar:
                await msg.delete()
            if msg.new_chat_members[0].first_name:
                print(msg.new_chat_members)
                ism1 = msg.new_chat_members[0].first_name
                await msg.answer(f" {ism1} iltimos reklama tarqatmang")
                return
    if msg.caption:
        reklama = ["mention", "url"]
        for i in msg.caption:
            if i.type  in reklama:
                await msg.delete()
            if msg.new_chat_members[0].first_name:
                print(msg.new_chat_members)
                ism1 = msg.new_chat_members[0].first_name
                await msg.answer(f" {ism1} iltimos reklama tarqatmang")
                return
