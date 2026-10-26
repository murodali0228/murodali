from aiogram import Router, types,F

rt = Router()


@rt.inline_query(F.query == "video")
async def inline_video(query: types.InlineQuery):
    results = [
        types.InlineQueryResultVideo(
            id="1",
            video_url="BAACAgIAAxkBAAIFQWrMwxPBDR6yUyR4xJLJJJjACkvGAAJqtwACBjYgSrD8VsAmljx6PQQ",
            thumbnail_url="BAACAgIAAxkBAAIFQWrMwxPBDR6yUyR4xJLJJJjACkvGAAJqtwACBjYgSrD8VsAmljx6PQQ",
            mime_type="sdfg",
            title="sfg"
        ),
        types.InlineQueryResultVideo(
            id="2",
            video_url="BAACAgIAAxkBAAIFQ2rMw6es-qcU87p8TkUYL-Qn8b8cAAKYpwACp1lpSoAb-f5WcnvpPQQ",
            thumbnail_url="BAACAgIAAxkBAAIFQ2rMw6es-qcU87p8TkUYL-Qn8b8cAAKYpwACp1lpSoAb-f5WcnvpPQQ",
            mime_type="dhg",
            title="dsf"
        ),
        types.InlineQueryResultVideo(
            id="3",
            video_url="BAACAgIAAxkBAAIFRWrMw67jkTzktUuODrD2q9gdquyUAAKZpwACp1lpSvuID_HrpxiBPQQ",
            thumbnail_url="BAACAgIAAxkBAAIFRWrMw67jkTzktUuODrD2q9gdquyUAAKZpwACp1lpSvuID_HrpxiBPQQ",
            mime_type="gr",
            title="ffg"

        ),
    ]
    await query.answer(results, cache_time=1, is_personal=True)