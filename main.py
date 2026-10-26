import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import location
from config.settings import BOT_TOKEN
from handlers.users.start import rt as start
from handlers.users.help import st as helps
from handlers.users.mujburlash import rt as majburlash
from handlers.users.lichka import rt as lichka
from handlers.users.admin import rt as admin
from handlers.groups.gaplash_group import rt as gaplash_group
from handlers.users.tolov import rt as tolov
from handlers.inline.rasm import rt as rasm
from handlers.inline.locatsya import rt as location
from handlers.inline.t import rt as t
from handlers.inline.matn import rt as matn
from handlers.inline.gif import rt as gif
# from handlers.users.telefon import rt as phone
# from handlers.users.query import rt as query
# from handlers.users.replyTest import rt as test
from handlers.users.car import rt as car
# from handlers.users.narsalar import rt as narsa
from handlers.users.button import rt as tugma
# from handlers.users.info import rt as info
# from handlers.groups.aniqlaGroup import rt as aniqlaGroup
from handlers.groups.reklama import rt as reklama
# from handlers.users.test import rt as test

dp = Dispatcher()

async def main():
    bot = Bot(BOT_TOKEN)

    dp.include_router(start)
    dp.include_router(helps)
    # dp.include_router(majburlash)
    # dp.include_router(admin)
    # dp.include_router(lichka)
    # dp.include_router(gaplash_group)
    # dp.include_router(tolov)
    # dp.include_router(rasm)
    # dp.include_router(location)
    # dp.include_router(t)
    # dp.include_router(matn)
    # dp.include_router(gif)
    # dp.include_router(test)
    # dp.include_router(phone)
    # dp.include_router(query)
    # dp.include_router(car)
    # dp.include_router(mashina)
    # dp.include_router(narsa)
    dp.include_router(tugma)
    # dp.include_router(info)
    # dp.include_router(reklama)
    # dp.include_router(aniqlaGroup)
    # dp.include_router(test)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        print("start bot")
        asyncio.run(main())
    except KeyboardInterrupt :
        print("bot toxtadi !")
