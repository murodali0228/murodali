from aiogram import Router, filters, types
from states.info_States import InfoState
from aiogram.fsm.context import FSMContext

rt = Router()

@rt.message(filters.Command("info"))
async def info(msg: types.Message, state: FSMContext):
    await msg.answer("anketa to'liq xushi kelibsiz!")
    await msg.answer("Ismingizni kiriting")
    await state.set_state(InfoState.ism)

@rt.message(InfoState.ism)
async def ism(msg: types.Message, state: FSMContext):
    await msg.answer("ism qabul qilindi, endi familyangizni kiriting: ")
    await state.set_state(InfoState.familya)
    await state.update_data(ism=msg.text)

@rt.message(InfoState.familya)
async def familya(msg: types.Message, state: FSMContext):
    await msg.answer("familyangiz qabul qilindi, endi yoshingizni kiriting: ")
    await state.set_state(InfoState.yosh)
    await state.update_data(familya=msg.text)

@rt.message(InfoState.yosh)
async def yosh(msg: types.Message, state: FSMContext):
    await msg.answer("yoshingiz qabul qilindi.")
    await msg.answer("barcha ma'lumotlaringizni qabul qiling:")
    await state.update_data(yosh=msg.text)
    data = await state.get_data()
    await state.clear()

    ism2 = data["ism"]
    familya2 = data["familya"]
    yosh2 = data["yosh"]
    n = f"ism: {ism2} \n"
    n += f"familya: {familya2} \n"
    n +=  f"yosh: {yosh2} \n"
    await msg.answer(n)