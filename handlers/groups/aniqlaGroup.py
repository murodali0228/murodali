from aiogram import filters, Router, types
rt = Router()

@rt.message()
async def aniqla(msg: types.Message):
    if msg.group_chat_created:
        print(msg.group_chat_created)
        ism = msg.from_user.first_name
        await msg.answer(f"{ism} guruh yaratdi")
    elif msg.new_chat_members[0].first_name:
        print(msg.new_chat_members)
        ism1 = msg.new_chat_members[0].first_name
        await msg.answer(f"{ism1} guruhga qo'shildi")
    elif msg.left_chat_member.first_name:
        print(msg.left_chat_member)
        ism2 = msg.left_chat_member[0].first_name
        await msg.answer(f"{ism2} guruhdan chiqardi")
    elif msg.new_chat_title:
        print(msg.new_chat_title)
        ism3 = msg.from_user.first_name
        await msg.answer(f"{ism3} guruhni nomini o'zgartirdi")
    elif msg.new_chat_photo:
        print(msg.new_chat_photo)
        rasm1 = msg.from_user.first_name
        await msg.answer(f"{rasm1} gruhni glavniysini o'zgartirdi")
    elif msg.delete_chat_photo:
        print(msg.delete_chat_photo)
        rasm  = msg.from_user.first_name
        await msg.answer(f"{rasm} guruhni glavniysini o'chirdi")
