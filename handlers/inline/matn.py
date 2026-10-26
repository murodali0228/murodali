from aiogram import Router, types,F

rt = Router()


@rt.inline_query(F.query == "matn")
async def inline_matn(query: types.InlineQuery):
    matn = query.query
    results = [
        types.InlineQueryResultArticle(
            id="1",
            title="berilgan matnni barcha harflarini katta qiladi!",
            input_message_content=types.InputTextMessageContent(
                message_text=matn.upper()
            )
        ),
        types.InlineQueryResultArticle(
            id="2",
            title="bitta harf yozib beradi",
            description="5-indeksdagi yoki 6-belgini yozadi",
            input_message_content=types.InputTextMessageContent(
                message_text=matn[5]
            )
        ),
    ]

    await query.answer(results, cache_time=1, is_personal=True)
