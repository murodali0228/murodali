from aiogram import Router, types,F

rt = Router()


@rt.inline_query(F.query == "gif")
async def inline_gif(query: types.InlineQuery):
    results = [
        types.InlineQueryResultGif(
            id="1",
            gif_url="CgACAgQAAxkBAAIFJ2rMt5lvbhapufHEAAFMUFkAAbKwlcMAArkKAAKUQ6RQvbpsOK_LDRE9BA",
            thumbnail_url="CgACAgQAAxkBAAIFJ2rMt5lvbhapufHEAAFMUFkAAbKwlcMAArkKAAKUQ6RQvbpsOK_LDRE9BA"
        ),
    types.InlineQueryResultGif(
            id="2",
            gif_url="CgACAgQAAxkBAAIFKGrMt5yp_4NiZRyQIUnwL6P7FqXgAALZBQACRCVlUvHNq-nDpX_cPQQ",
            thumbnail_url="CgACAgQAAxkBAAIFKGrMt5yp_4NiZRyQIUnwL6P7FqXgAALZBQACRCVlUvHNq-nDpX_cPQQ"
        ),
    types.InlineQueryResultGif(
            id="3",
            gif_url="CgACAgQAAxkBAAIFJmrMt5F0R5iWmunxoxFkyqIxBh2fAAIaCAACIGykUgtskFFPpEsyPQQ",
            thumbnail_url="CgACAgQAAxkBAAIFJmrMt5F0R5iWmunxoxFkyqIxBh2fAAIaCAACIGykUgtskFFPpEsyPQQ"
        ),
    types.InlineQueryResultGif(
            id="4",
            gif_url="CgACAgIAAxkBAAIFJWrMt48iZEWdysCResZDocWfLIhqAAJYpQACLfrYSFxEt9pu2nG7PQQ",
            thumbnail_url="CgACAgIAAxkBAAIFJWrMt48iZEWdysCResZDocWfLIhqAAJYpQACLfrYSFxEt9pu2nG7PQQ"
        ),
    types.InlineQueryResultGif(
            id="5",
            gif_url="CgACAgIAAxkBAAIFJGrMt4w7EaUh3nR6x-rswrkkcA-jAALVmwACqKIZS_bQFKAT8Rz2PQQ",
            thumbnail_url="CgACAgIAAxkBAAIFJGrMt4w7EaUh3nR6x-rswrkkcA-jAALVmwACqKIZS_bQFKAT8Rz2PQQ"
        ),
    ]

    await query.answer(results, cache_time=1, is_personal=True)
