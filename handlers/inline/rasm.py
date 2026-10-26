from aiogram import Router, types,F

rt = Router()


@rt.inline_query(F.query == "rasm")
async def inline_video(query: types.InlineQuery):
    results = [
        types.InlineQueryResultPhoto(
            id="1",
            photo_url="AgACAgIAAxkBAAIFR2rMxjfxgaQmwyC_zwy7UaO-ktnNAAKlJGsbjdZoSsSxTHAwgrqfAQADAgADeQADPQQ",
            thumbnail_url="AgACAgIAAxkBAAIFR2rMxjfxgaQmwyC_zwy7UaO-ktnNAAKlJGsbjdZoSsSxTHAwgrqfAQADAgADeQADPQQ",
        ),
        types.InlineQueryResultPhoto(
            id="2",
            photo_url="AgACAgIAAxkBAAIFSWrMxknn8e5drXaWL79IAurhRKhAAAKkJGsbjdZoSloNSm4mLn9_AQADAgADeQADPQQ",
            thumbnail_url="AgACAgIAAxkBAAIFSWrMxknn8e5drXaWL79IAurhRKhAAAKkJGsbjdZoSloNSm4mLn9_AQADAgADeQADPQQ",
        ),
        types.InlineQueryResultPhoto(
            id="3",
            photo_url="AgACAgIAAxkBAAIFS2rMxl5X2DXGxiDYO9e1KtHNjvuKAAKNJGsbjdZoSv1UcRxnYGqfAQADAgADeQADPQQ",
            thumbnail_url="AgACAgIAAxkBAAIFS2rMxl5X2DXGxiDYO9e1KtHNjvuKAAKNJGsbjdZoSv1UcRxnYGqfAQADAgADeQADPQQ",
        ),
            types.InlineQueryResultPhoto(
            id="4",
            photo_url="AgACAgIAAxkBAAIFTWrMxm62ED0lg9wgkhVca6uB2YnJAAJGJGsbjdZoSsFGjBmdTcFjAQADAgADeQADPQQ",
            thumbnail_url="AgACAgIAAxkBAAIFTWrMxm62ED0lg9wgkhVca6uB2YnJAAJGJGsbjdZoSsFGjBmdTcFjAQADAgADeQADPQQ",
        ),
    ]
    await query.answer(results, cache_time=1, is_personal=True)

