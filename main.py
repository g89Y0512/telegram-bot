from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@crmonebox_shebo"
ADMIN_IDS = [883527189, 630765479]
FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSdBxBbGws2-gVubk-mtzjDFfDoau5wDX1hMv8W2njDvtiXV_A/viewform"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text_post(message: types.Message):
    kb = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Заповнити заявку", callback_data="form_click")
    )
    await bot.send_message(chat_id=CHANNEL_ID, text=message.text, reply_markup=kb)
    await message.reply("Пост опубліковано.")

@dp.callback_query_handler(lambda c: c.data == "form_click")
async def handle_click(callback_query: types.CallbackQuery):
    user = callback_query.from_user
    username = f"@{user.username}" if user.username else user.full_name
    await bot.send_message(user.id, f"{FORM_LINK}")
    for admin_id in ADMIN_IDS:
        await bot.send_message(admin_id, f"{username} натиснув кнопку")
    await callback_query.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
