import asyncio
import logging
import random
import os
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# --------------------------------------------------------------------------------
# SOZLAMALAR
# --------------------------------------------------------------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("XATOLIK: BOT_TOKEN topilmadi! Railway Variables bo'limini tekshiring.")
    sys.exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# --------------------------------------------------------------------------------
# MENYULAR
# --------------------------------------------------------------------------------
def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Montaj ilovalari 📹") 
    builder.button(text="ChatGPT portret 🌅")
    builder.button(text="Instagram Mod")
    builder.button(text="Spotify Mod 🎵")
    builder.button(text="TikTok Mod 📹")
    builder.button(text="InShot Pro ✂️")
    builder.button(text="VPN Pro versiya 🌐")
    builder.button(text="Nomer aniqlash 🔍")
    builder.button(text="Rasmlarni tiklash ♻️")
    builder.button(text="Mod O'yinlar 🎮")
    builder.button(text="Keyingi qator ➡️")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def second_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Montaj ilovasi 👌")
    builder.button(text="Android ilovalar 🧩")
    builder.button(text="Telegramda Pul ishlash 🤩")
    builder.button(text="🔊 Dinamika ilovasi")
    builder.button(text="AI Video 🎥")
    builder.button(text="Android sirli ilovasi 🤫")
    builder.button(text="PUL ISHLASH 🤑")
    builder.button(text="O'xshash qiyofa 🤠")
    builder.button(text="Sharpa Telegram 👻")
    builder.button(text="Lokatsiya aniqlash 📍")
    builder.button(text="Android VPN 🌐")
    builder.button(text="Cap Cut Pro tekin 📱")
    builder.button(text="Minusovka ajratish 🎼")
    builder.button(text="Stiker yasash 🧩")
    builder.button(text="Spamdan chiqish 🚫")
    builder.button(text="Kontakt ilova 📞")
    builder.button(text="📱 Boshqa telefonga ulanish")
    builder.button(text="“теневой бан”dan chiqish")
    builder.button(text="Bir daqiqalik parol ✳️")
    builder.button(text="Telefon Zapis 🔴")
    builder.button(text="Yolg'on qo'ng'iroq 📞")
    builder.button(text="Reklamasiz Instagram ❗️")
    builder.button(text="O'chgan smsni ko'rish 👀")
    builder.button(text="Telefon blok ilovasi 🔒")
    builder.button(text="⬅️ Oldingi qator")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

# --------------------------------------------------------------------------------
# PROMPTLAR
# --------------------------------------------------------------------------------
portrait_prompts = [
    """Create a realistic behind-the-scenes selfie on a film set inspired by the HBO series "Game of Thrones"...""",
    """Transform the selfie into a cinematic, moody side-profile portrait inspired by a DJ-style look...""",
    """Surreal Y2K-style action shot of me mid-air in a dramatic leap..."""
]

# --------------------------------------------------------------------------------
# YORDAMCHI: FAYL ID SINI OLIW UCHUN (Faqat siz uchun)
# --------------------------------------------------------------------------------
@dp.message(F.document)
async def get_file_id_handler(message: types.Message):
    # Siz botga fayl tashlasangiz, u sizga ID sini qaytaradi
    file_id = message.document.file_id
    await message.reply(f"✅ <b>Fayl qabul qilindi!</b>\n\nKodni nusxalab oling va kodga qo'ying:\n<code>{file_id}</code>", parse_mode="HTML")

# --------------------------------------------------------------------------------
# ASOSIY HANDLERLAR
# --------------------------------------------------------------------------------

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Assalomu alaykum! Ilovame botiga xush kelibsiz.", reply_markup=main_menu())

# --- NAVIGATSIYA ---
@dp.message(F.text == "Keyingi qator ➡️")
async def next_page(message: types.Message):
    await message.answer("Keyingi bo'lim:", reply_markup=second_menu())

@dp.message(F.text == "⬅️ Oldingi qator")
async def prev_page(message: types.Message):
    await message.answer("Asosiy menyu:", reply_markup=main_menu())

# --- MONTAJ ILOVALARI (CapCut va InShot birdan ketadi) ---
@dp.message(F.text == "Montaj ilovalari 📹")
async def send_montage_apps(message: types.Message):
    await message.answer("Ilovalar yuklanmoqda... ⏳")
    
    # DIQQAT: Pastdagi "BQACAg..." larni o'rniga o'zingiz olgan ID larni qo'ying!
    
    # 1. CapCut
    try:
        await message.answer_document(document="FILE_ID_CAPCUT_QUYING", caption="📥 **CapCut Pro** (Android)\nSuv belgisiz va barcha effektlar ochiq.")
    except:
        await message.answer("❌ CapCut fayli hali yuklanmagan (ID noto'g'ri).")

    # 2. InShot
    try:
        await message.answer_document(document="FILE_ID_INSHOT_QUYING", caption="📥 **InShot Pro** (Android)\nReklamasiz to'liq versiya.")
    except:
        await message.answer("❌ InShot fayli hali yuklanmagan (ID noto'g'ri).")


# --- QOLGAN FAYLLAR ---

@dp.message(F.text == "Instagram Mod")
async def send_insta(message: types.Message):
    try:
        await message.answer_document(document="FILE_ID_INSTA_QUYING", caption="📥 **Instagram Mod (InstaPro)**")
    except:
        await message.answer("❌ Fayl topilmadi, IDni tekshiring.")

@dp.message(F.text == "Spotify Mod 🎵")
async def send_spotify(message: types.Message):
    await message.answer_document(document="FILE_ID_SPOTIFY_QUYING", caption="📥 **Spotify Premium Mod**")

@dp.message(F.text == "TikTok Mod 📹")
async def send_tiktok(message: types.Message):
    await message.answer_document(document="FILE_ID_TIKTOK_QUYING", caption="📥 **TikTok Mod (Suv belgisiz)**")

@dp.message(F.text == "InShot Pro ✂️")
async def send_inshot_single(message: types.Message):
    await message.answer_document(document="FILE_ID_INSHOT_QUYING", caption="📥 **InShot Pro**")

@dp.message(F.text == "VPN Pro versiya 🌐")
async def send_vpn(message: types.Message):
    await message.answer_document(document="FILE_ID_VPN_QUYING", caption="📥 **AdGuard VPN Mod**")

@dp.message(F.text == "Rasmlarni tiklash ♻️")
async def send_recovery(message: types.Message):
    await message.answer_document(document="FILE_ID_RECOVERY_QUYING", caption="📥 **DiskDigger Pro** (Rasmlarni tiklash)")

@dp.message(F.text == "Mod O'yinlar 🎮")
async def send_games(message: types.Message):
    await message.answer_document(document="FILE_ID_GAMES_QUYING", caption="📥 **Clash of Clans Mod**")

@dp.message(F.text == "Nomer aniqlash 🔍")
async def send_caller_id(message: types.Message):
    # Android uchun fayl
    await message.answer_document(document="FILE_ID_NOMER_QUYING", caption="🤖 **Android uchun: Sync.ME** (Fayl)")
    # iPhone uchun ssilka
    await message.answer("📱 **iPhone uchun:**\nhttps://apps.apple.com/uz/app/sync-me-caller-id-contacts/id340787494")

@dp.message(F.text == "Android sirli ilovasi 🤫")
async def send_secret_app(message: types.Message):
    await message.answer_document(document="FILE_ID_WAMR_QUYING", caption="📥 **WAMR** (O'chgan SMSlarni o'qish)")

# --- MATNLAR VA SSILKALAR ---
@dp.message(F.text == "ChatGPT portret 🌅")
async def send_ai_prompt(message: types.Message):
    selected_prompt = random.choice(portrait_prompts)
    await message.answer(f"<b>Prompt nusxalab oling:</b>\n<code>{selected_prompt}</code>", parse_mode="HTML")

@dp.message(F.text == "Montaj ilovasi 👌")
async def send_gravity(message: types.Message):
    await message.answer("<b>Gravity (iPhone):</b>\n<a href='https://apps.apple.com/uz/app/gravity-augmented-reality/id1400961806'>Yuklab olish</a>", parse_mode="HTML")

# --- Catch-All (Boshqa hamma tugmalar uchun) ---
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer("Bu bo'lim tez orada qo'shiladi! 🛠 Yoki fayl ID si xato kiritilgan.")

# --------------------------------------------------------------------------------
# BOTNI YURGIZISH
# --------------------------------------------------------------------------------
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
