from aiogram import Router, F, types
rt = Router()
#
# @rt.message(F.video)
# async def get_video_id(message: types.Message):
#     video_id = message.video.file_id
#     print(f"Video ID: {video_id}")
#     await message.reply(f"Siz yuborgan Video ID:\n`{video_id}`", parse_mode="MarkdownV2")
#
# @rt.message(F.video_note)
# async def get_video_note_id(message: types.Message):
#     video_note_id = message.video_note.file_id
#     print(f"Kruglyash ID: {video_note_id}")
#     await message.reply(f"Siz yuborgan dumaloq video ID:\n`{video_note_id}`", parse_mode="MarkdownV2")

# @rt.message(F.photo)
# async def get_photo_id(message: types.Message):
#     photo_id = message.photo[-1].file_id
#     print(f"Rasm ID: {photo_id}")
#     await message.reply(f"Siz yuborgan rasm ID:\n`{photo_id}`", parse_mode="MarkdownV2")

# @rt.message(F.voice)
# async def get_voice_id(message: types.Message):
#     voice_id = message.voice.file_id
#     print(f"Ovozli xabar ID: {voice_id}")
#     await message.reply(f"Ovozli xabar ID:\n`{voice_id}`", parse_mode="MarkdownV2")
#
# @rt.message(F.audio)
# async def get_audio_id(message: types.Message):
#     audio_id = message.audio.file_id
#     print(f"Audio fayl ID: {audio_id}")
#     await message.reply(f"Audio/Musiqa ID:\n`{audio_id}`", parse_mode="MarkdownV2")

@rt.message(F.animation)
async def get_gif_id(message: types.Message):
    gif_id = message.animation.file_id
    print(f"GIF ID: {gif_id}")
    await message.reply(f"Siz yuborgan GIF ID:\n`{gif_id}`", parse_mode="MarkdownV2")
