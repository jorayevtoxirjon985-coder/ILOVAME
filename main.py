import asyncio
import os
import sys
from aiogram import Bot, Dispatcher, types, F

# Tokenni Railwaydan oladi
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    sys.exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# SIZ FAYL TASHLASANGIZ, BU KOD SIZGA ID SINI QAYTARADI
@dp.message(F.document)
async def get_id(message: types.Message):
    file_id = message.document.file_id
    file_name = message.document.file_name
    
    # Sizga javob qaytaradi
    await message.reply(f"📁 <b>{file_name}</b>\n\n🆔 ID: <code>{file_id}</code>", parse_mode="HTML")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
