from aiogram import Router, types,F

rt = Router()


@rt.inline_query(F.query == "ovoz")
async def inline_video(query: types.InlineQuery):
    results = [
        types.InlineQueryResultVoice(
            id="1",
            voice_url="AwACAgIAAxkBAAIFT2rMyROqI4uDS-1qbjeyR0XwsOA3AALGpwACp1lpSnDn-YCqr_wmPQQ",
            title="sdv",
        ),
        types.InlineQueryResultVoice(
            id="2",
            voice_url="AwACAgIAAxkBAAIFUWrMyRhJVhSdFlvBlAgpRl7r8KidAALHpwACp1lpSrX0Dql7uYKqPQQ",
            title="fgd",
        ),
        types.InlineQueryResultVoice(
            id="3",
            voise_url="AwACAgIAAxkBAAIFU2rMyRsV0egl97x2YV4eFCYBTM7KAALIpwACp1lpSg_yheXBEDkOPQQ",
            title="fdsdg",
        ),
            types.InlineQueryResultVoice(
            id="4",
            voise_url="AwACAgIAAxkBAAIFVWrMySVx-2SOjrn0FNlMvMKYnq3zAALJpwACp1lpSm88r0Y48uWfPQQ",
            title="fdgd",
        ),
    ]
    await query.answer(results, cache_time=1, is_personal=True)

