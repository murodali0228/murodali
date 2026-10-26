from aiogram import Router, types, filters, F
from keyboards.inlineKeyboard.telefon_inline import telefon, rang, narxi, yili,end

rt = Router()

@rt.message(filters.Command("oqish"))
async def oquv(msg: types.Message):
    await msg.answer("o`zingiz fan tanlang", reply_markup=telefon())

@rt.callback_query(F.data == "telefon")
async def phone_rang(call: types.CallbackQuery):
    await call.answer("telefon muvaffaqiyatli tanlandi")
    await call.message.edit_text("endi rang tanlang", reply_markup=rang())

@rt.callback_query(F.data == "rang")
async  def phone_narx(call: types.CallbackQuery):
    await call.answer("rang muvaffaqqiyatli tanlandi")
    await call.message.edit_text("endi telefoningiz yilini tanlang", reply_markup=narxi())

@rt.callback_query(F.data == "narxi")
async  def phone_narxr(call: types.CallbackQuery):
    await call.answer("narx muvaffaqqiyatli tanlandi")
    await call.message.edit_text("endi telefoningiz yilini tanlang", reply_markup=yili())

@rt.callback_query(F.data == "yili")
async def phone_yili(call: types.CallbackQuery):
    await call.answer("yili muvaffaqiyatli tanlandi")
    await call.message.edit_text("endi buyurtmani olsangiz boldi!", reply_markup=end())

@rt.callback_query(F.data == "end")
async def phone_end(call: types.CallbackQuery):
    await call.answer("barcha narsa tanlandi")
    await call.message.edit_text("barcha ma'lumotlar operatorga yuborildi o'zimiz aloqaga chiqamiz")
