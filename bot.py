import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

API_TOKEN = "8779410844:AAGpvCRBUjlNtaVawiCCauxHkWYL6R9yeJw"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = InlineKeyboardMarkup()
    # رابط ويب مباشر ومضمون للمعاينة
    game_url = "https://info.cern.ch/"
    
    markup.add(
        InlineKeyboardButton(
            text="🚀 افتح التطبيق", 
            web_app=WebAppInfo(url=game_url)
        )
    )
    
    await message.reply(
        "مرحبا عزيز المستخدم في بوت التعدين الخاص بك! ⛏️\nاضغط على الزر أسفله للتجربة:", 
        reply_markup=markup
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
