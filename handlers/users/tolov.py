from aiogram import Router, types, F,Bot
from config.settings import CLIC_TOKEN

rt = Router()

kompyuterlar = ["lenovo", "acer", "macbook"]

@rt.message(F.text == "noutbuk")
async def tolov(msg: types.Message):
    await msg.answer_invoice(
        title="lenovo noutbook",
        description="bu qogondagi bunker kompyuter markazining ishonchli noutbooklaridan",
        payload="lenovo",
        prices=[
            types.LabeledPrice(
                label="lenovo noutbook (label)",
                amount=4_000_000_00
            )
        ],
        currency="UZS",
        provider_token=CLIC_TOKEN,

    )
    await msg.answer_invoice(
        title="aser noutbook",
        description="bun noutbuk dokonimizdagi zor notbuklardan",
        payload="aser",
        prices=[
            types.LabeledPrice(
                label="aser noutbook (label)",
                amount=7_000_000_00
            )
        ],
        currency="UZS",
        provider_token=CLIC_TOKEN,
    )
    await msg.answer_invoice(
        title="macbook",
        description="macbook dokonimizdagi zor notbuklardan",
        payload="mac",
        prices=[
            types.LabeledPrice(
                label="macbook (label)",
                amount=12_000_000_000
            )
        ],
        currency="UZS",
        provider_token=CLIC_TOKEN,
    )
@rt.pre_checkout_query()
async def pre2(pre: types.PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(
        pre_checkout_query_id=pre.id,
        ok=True
    )
