import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# --------------------------------------------------------------------------------
# TOKEN
# --------------------------------------------------------------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("XATOLIK: BOT_TOKEN topilmadi!")
    sys.exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# --------------------------------------------------------------------------------
# FAYL IDLARI (MANA SHU YERGA IDLARNI YOZASIZ)
# --------------------------------------------------------------------------------
# Hozircha bo'sh turibdi. Botga fayl tashlab, ID sini olib, shu yerga qo'yasiz.
FILE_IDS = {
    "capcut": "BU_YERGA_CAPCUT_ID_QUYING",
    "inshot": "BU_YERGA_INSHOT_ID_QUYING",
    "instagram": "BU_YERGA_INSTAGRAM_ID_QUYING",
    "tiktok": "BU_YERGA_TIKTOK_ID_QUYING",
    "vpn": "BU_YERGA_VPN_ID_QUYING"
}

# --------------------------------------------------------------------------------
# YORDAMCHI: FAYL ID SINI OLISH (ENG MUHIM JOYI)
# --------------------------------------------------------------------------------
@dp.message(F.document)
async def get_file_id_handler(message: types.Message):
    # Siz botga fayl tashlasangiz, u sizga ID sini qaytaradi
    file_id = message.document.file_id
    await message.reply(f"✅ **Fayl ID si olindi!**\n\nKodni nusxalab oling:\n<code>{file_id}</code>\n\nEndi buni main.py dagi 'BU_YERGA...' degan joyga almashtiring.", parse_mode="HTML")

# --------------------------------------------------------------------------------
# MENYULAR
# --------------------------------------------------------------------------------
def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Montaj ilovalari 📹") 
    builder.button(text="Instagram Mod")
    builder.button(text="TikTok Mod 📹")
    builder.button(text="VPN Pro versiya 🌐")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Fayl ID sini olish uchun menga kerakli faylni (APK) yuboring.", reply_markup=main_menu())

# --------------------------------------------------------------------------------
# TUGMALAR ISHLASHI
# --------------------------------------------------------------------------------

@dp.message(F.text == "Montaj ilovalari 📹")
async def send_montage(message: types.Message):
    # CapCut
    capcut_id = FILE_IDS["capcut"]
    if "BU_YERGA" not in capcut_id:
        await message.answer_document(document=capcut_id, caption="📥 **CapCut Pro**")
    else:
        await message.answer("❌ CapCut fayli hali kiritilmagan.")

    # InShot
    inshot_id = FILE_IDS["inshot"]
    if "BU_YERGA" not in inshot_id:
        await message.answer_document(document=inshot_id, caption="📥 **InShot Pro**")
    else:
        await message.answer("❌ InShot fayli hali kiritilmagan.")

@dp.message(F.text == "Instagram Mod")
async def send_insta(message: types.Message):
    insta_id = FILE_IDS["instagram"]
    if "BU_YERGA" not in insta_id:
        await message.answer_document(document=insta_id, caption="📥 **Instagram Mod**")
    else:
        await message.answer("❌ Instagram fayli hali kiritilmagan.")

# --------------------------------------------------------------------------------
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
