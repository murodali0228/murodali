from aiogram import Router, filters, types, F, Bot
from aiogram.fsm.context import FSMContext
from states.carState import CarState
from config.settings import CLIC_TOKEN

from keyboards.replyKeyboard.carKeyboard import (
    cars1, colors1, years1,
    car, colors2, year
)

rt = Router()

@rt.message(filters.Command("car"))
async def start(msg: types.Message, state: FSMContext):
    await msg.answer(text="Mashinalardan birini tanlang:", reply_markup=car())
    await state.set_state(CarState.car_name)

@rt.message(CarState.car_name)
async def car2(msg: types.Message, state: FSMContext):
    cars_lower = [str(c).lower().strip() for c in cars1]
    user_input = msg.text.lower().strip()

    if user_input in cars_lower:
        await state.update_data(chosen_car=user_input)

        await msg.answer(text=f"{msg.text} mashinangiz uchun rang tanlang:", reply_markup=colors2())
        await state.set_state(CarState.car_color)
    else:
        await msg.answer("Iltimos, tugmalardan birini bosing!")

@rt.message(CarState.car_color)
async def color_handler(msg: types.Message, state: FSMContext):
    colors_lower = [str(c).lower().strip() for c in colors1]
    user_input = msg.text.lower().strip()

    if user_input in colors_lower:
        await msg.answer(f"Tanlangan rang: {msg.text}. Endi ishlab chiqarilgan yilini tanlang:", reply_markup=year())
        await state.set_state(CarState.car_years)
    else:
        await msg.answer("Iltimos, tugmalardan birini bosing!")

@rt.message(CarState.car_years)
async def year_handler(msg: types.Message, state: FSMContext):
    years_str = [str(y).strip() for y in years1]
    user_input = msg.text.strip()

    if user_input in years_str:
        await msg.answer("Rahmat! Ma'lumotlar qabul qilindi. To'lov schoti tayyorlanmoqda...",
                         reply_markup=types.ReplyKeyboardRemove())

        user_data = await state.get_data()
        chosen_car = user_data.get("chosen_car")

        try:
            if chosen_car == "malibu":
                await msg.answer_invoice(
                    title="Malibu",
                    description="Malibu bu moshina GM dagi eng zor moshinalardan biri!",
                    payload="malibu_pay",
                    prices=[types.LabeledPrice(label="Malibu test narxi", amount=350_000_000_0)],
                    currency="UZS",
                    provider_token=CLIC_TOKEN,
                )
            elif chosen_car == "cobalt":
                await msg.answer_invoice(
                    title="Cobalt",
                    description="Cobalt bu moshina GM dagi eng aqilli mashalardan biri!",
                    payload="cobalt_pay",
                    prices=[types.LabeledPrice(label="Cobalt test narxi", amount=120_000_000_0)],
                    currency="UZS",
                    provider_token=CLIC_TOKEN,
                )
            elif chosen_car == "gentra":
                await msg.answer_invoice(
                    title="Gentra",
                    description="Gentra bu kotta bollarni moshinasi 😎",
                    payload="gentra_pay",
                    prices=[types.LabeledPrice(label="Gentra test narxi", amount=150_000_000_0)],
                    currency="UZS",
                    provider_token=CLIC_TOKEN,
                )
            elif chosen_car == "nexia":
                await msg.answer_invoice(
                    title="Nexia",
                    description="Nexia bu zor moshina !!!",
                    payload="nexia_pay",
                    prices=[types.LabeledPrice(label="Nexia test narxi", amount=70_000_000_0)],
                    currency="UZS",
                    provider_token=CLIC_TOKEN,
                )
            else:
                await msg.answer("Xatolik: Tanlangan mashina topilmadi. Jarayonni boshidan boshlang: /car")
                await state.clear()
                return
            await state.set_state(CarState.car_price)

        except Exception as e:
            await msg.answer("To'lov tizimini yuklashda xatolik yuz berdi.")
            print(f"TO'LOV XATOLIGI: {e}")
            await state.clear()

    else:
        await msg.answer("Iltimos, tugmalardan birini bosing!")


@rt.pre_checkout_query()
async def pre_checkout_handler(pre: types.PreCheckoutQuery):
    await pre.answer(ok=True)

@rt.message(F.successful_payment)
async def success_payment_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Mashinangiz muborak bo'lsin! To'lov muvaffaqiyatli amalga oshirildi. 🎉")
    await state.clear()
