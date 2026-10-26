from aiogram import Router,types, F
rt = Router()

@rt.inline_query(F.query == "location")
async def lokatsiya_mode(query: types.InlineQuery):
    results = [
        types.InlineQueryResultLocation(
            id="1",
            latitude=40.54385020637419,
            longitude=71.06121928311175,
            title="al-fargoniy"
        ),
        types.InlineQueryResultLocation(
            id="2",
            latitude=40.54320452443433,
            longitude=71.06154188026935,
            title="29-maktab"
        )
    ]

    await query.answer(results=results, cache_time=1, is_personal=True)
