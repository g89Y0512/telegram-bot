from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = '7754020557:AAErfSMbFpCMLLIbLsq7fUGv4p91ah-rcbo'
ADMINS = ['Yurii_Bolotian', 'lilbarbiee']
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdBxBbGws2-gVubk-mtzjDFfDoau5wDX1hMv8W2njDvtiXV_A/viewform?usp=header'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Заповнити заявку", url=FORM_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("👋 Привіт! Натисни кнопку нижче, щоб заповнити заявку:", reply_markup=reply_markup)

    user = update.effective_user.username
    if user and user not in ADMINS:
        for admin in ADMINS:
            try:
                await context.bot.send_message(chat_id=f"@{admin}", text=f"👀 @{user} відкрив форму.")
            except:
                pass

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
