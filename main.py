import asyncio
import logging
import random
import os
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# --------------------------------------------------------------------------------
# 1. SOZLAMALAR (TOKEN)
# --------------------------------------------------------------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("XATOLIK: BOT_TOKEN topilmadi! Railway Variables bo'limini tekshiring.")
    sys.exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# --------------------------------------------------------------------------------
# 2. MENYULAR
# --------------------------------------------------------------------------------
def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Montaj ilovalari 📹") # Bu tugma endi ishlaydi
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
# 3. PROMPTLAR (MATNLAR)
# --------------------------------------------------------------------------------
portrait_prompts = [
    """Create a realistic behind-the-scenes selfie on a film set inspired by the HBO series "Game of Thrones"...""",
    """Transform the selfie into a cinematic, moody side-profile portrait inspired by a DJ-style look...""",
    """Surreal Y2K-style action shot of me mid-air in a dramatic leap..."""
]

# --------------------------------------------------------------------------------
# 4. HANDLERS (JAVOBLAR)
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

# --- "MONTAJ ILOVALARI" (1-MENYU) --- 
# Bu yerda ikkita asosiy ilovani birdan tashlaymiz
@dp.message(F.text == "Montaj ilovalari 📹")
async def send_montage_apps(message: types.Message):
    await message.answer("Eng zo'r montaj ilovalari tashlanmoqda...")
    # 1. CapCut
    await message.answer_document(document="FILE_ID_CAPCUT", caption="📥 **CapCut Pro** (Android)")
    # 2. InShot
    await message.answer_document(document="FILE_ID_INSHOT", caption="📥 **InShot Pro** (Android)")

# --- "NOMER ANIQLASH" (Androidga fayl, iPhonega ssilka) ---
@dp.message(F.text == "Nomer aniqlash 🔍")
async def send_caller_id(message: types.Message):
    # Android uchun FAYL
    await message.answer_document(document="FILE_ID_NOMER_ANIQLASH_APK", caption="🤖 **Android uchun: Sync.ME** (Fayl)")
    # iPhone uchun SSILKA
    await message.answer("📱 **iPhone uchun:**\nhttps://apps.apple.com/uz/app/sync-me-caller-id-contacts/id340787494")

# --- QOLGAN FAYLLAR (HAMMASI FAYL BO'LIB BORADI) ---

@dp.message(F.text == "Instagram Mod")
async def send_insta(message: types.Message):
    await message.answer_document(document="FILE_ID_INSTAGRAM_MOD", caption="📥 **Instagram Mod (InstaPro)**")

@dp.message(F.text == "Spotify Mod 🎵")
async def send_spotify(message: types.Message):
    await message.answer_document(document="FILE_ID_SPOTIFY", caption="📥 **Spotify Premium Mod**")

@dp.message(F.text == "TikTok Mod 📹")
async def send_tiktok(message: types.Message):
    await message.answer_document(document="FILE_ID_TIKTOK", caption="📥 **TikTok Mod (Suv belgisiz)**")

@dp.message(F.text == "InShot Pro ✂️")
async def send_inshot(message: types.Message):
    await message.answer_document(document="FILE_ID_INSHOT", caption="📥 **InShot Pro**")

@dp.message(F.text == "VPN Pro versiya 🌐")
async def send_vpn(message: types.Message):
    await message.answer_document(document="FILE_ID_VPN", caption="📥 **AdGuard VPN Mod**")

@dp.message(F.text == "Rasmlarni tiklash ♻️")
async def send_recovery(message: types.Message):
    await message.answer_document(document="FILE_ID_DISK_DIGGER", caption="📥 **DiskDigger Pro** (Rasmlarni tiklash)")

@dp.message(F.text == "Mod O'yinlar 🎮")
async def send_games(message: types.Message):
    await message.answer_document(document="FILE_ID_CLASH", caption="📥 **Clash of Clans Mod**")

@dp.message(F.text == "Cap Cut Pro tekin 📱")
async def send_capcut(message: types.Message):
    await message.answer_document(document="FILE_ID_CAPCUT", caption="📥 **CapCut Pro**")

@dp.message(F.text == "Minusovka ajratish 🎼")
async def send_minus(message: types.Message):
    await message.answer_document(document="FILE_ID_MOISES", caption="📥 **Moises AI** (Minusovka qiluvchi)")

@dp.message(F.text == "Stiker yasash 🧩")
async def send_sticker_app(message: types.Message):
    await message.answer_document(document="FILE_ID_STICKER_MAKER", caption="📥 **Sticker Maker**")

@dp.message(F.text == "Android sirli ilovasi 🤫")
async def send_secret_app(message: types.Message):
    await message.answer_document(document="FILE_ID_WAMR", caption="📥 **WAMR** (O'chgan SMSlarni o'qish)")

@dp.message(F.text == "O'chgan smsni ko'rish 👀")
async def send_wamr_direct(message: types.Message):
    await message.answer_document(document="FILE_ID_WAMR", caption="📥 **WAMR** (O'chgan SMSlarni ko'rish)")

@dp.message(F.text == "Telefon blok ilovasi 🔒")
async def send_lock_app(message: types.Message):
    await message.answer_document(document="FILE_ID_LOCK_APP", caption="📥 **Time Password** (Har daqiqa o'zgaradigan parol)")

@dp.message(F.text == "Telefon Zapis 🔴")
async def send_call_recorder(message: types.Message):
    await message.answer_document(document="FILE_ID_CALL_RECORDER", caption="📥 **Call Recorder** (Zapis qilish)")

@dp.message(F.text == "Yolg'on qo'ng'iroq 📞")
async def send_fake_call(message: types.Message):
    await message.answer_document(document="FILE_ID_FAKE_CALL", caption="📥 **Fake Call** (Yolg'on qo'ng'iroq)")

@dp.message(F.text == "Reklamasiz Instagram ❗️")
async def send_instander(message: types.Message):
    await message.answer_document(document="FILE_ID_INSTANDER", caption="📥 **Instander** (Reklamasiz Instagram)")

@dp.message(F.text == "O'yin uchun ilova 🎮")
async def send_game_tool(message: types.Message):
    await message.answer_document(document="FILE_ID_GAME_TOOL", caption="📥 **AirConsole** (Telefonda o'yin o'ynash)")

@dp.message(F.text == "Sharpa Telegram 👻")
async def send_ghost_telegram(message: types.Message):
    await message.answer_document(document="FILE_ID_AKA_MESSENGER", caption="📥 **Aka Messenger** (Sharpa rejim)")

@dp.message(F.text == "Android VPN 🌐")
async def send_android_vpn(message: types.Message):
    await message.answer_document(document="FILE_ID_VPN", caption="📥 **AdGuard VPN**")

# --- SSILKALAR ---
# (Fayli yo'q, faqat ssilka bo'lishi shart bo'lganlar)

@dp.message(F.text == "Telegramda Pul ishlash 🤩")
async def send_money_bot(message: types.Message):
    await message.answer("<b>GenkiMinerBot:</b>\n👉 <a href='https://t.me/GenkiMinerBot/kapkap?startapp=T2xLOZii'>O'yinni boshlash</a>", parse_mode="HTML")

@dp.message(F.text == "PUL ISHLASH 🤑")
async def send_money_bot_2(message: types.Message):
    await message.answer("<b>GenkiMinerBot (USDT ishlash):</b>\n👉 <a href='https://t.me/GenkiMinerBot/kapkap?startapp=T2xLOZii'>Boshlash</a>", parse_mode="HTML")

@dp.message(F.text == "Spamdan chiqish 🚫")
async def send_spam_info(message: types.Message):
    await message.answer("<b>Spamdan chiqish:</b>\n@SpamBot ga kirib 'Bu xato' (This is a mistake) tugmasini bosing.", parse_mode="HTML")

@dp.message(F.text == "Bir daqiqalik parol ✳️")
async def send_temp_mail(message: types.Message):
    await message.answer("Vaxtinchalik email sayti: https://temp-mail.org/")

@dp.message(F.text == "ChatGPT portret 🌅")
async def send_ai_prompt(message: types.Message):
    selected_prompt = random.choice(portrait_prompts)
    await message.answer(f"<b>Prompt nusxalab oling:</b>\n<code>{selected_prompt}</code>", parse_mode="HTML")

@dp.message(F.text == "AI Video 🎥")
async def send_ai_video_tools(message: types.Message):
    await message.answer("Rasm: https://gemini.google.com/app\nVideo: https://deevid.ai/", parse_mode="HTML")

@dp.message(F.text == "Montaj ilovasi 👌")
async def send_gravity(message: types.Message):
    await message.answer("<b>Ilova faqat iPhone uchun:</b>\n<a href='https://apps.apple.com/uz/app/gravity-augmented-reality/id1400961806'>Gravity - Yuklab olish</a>", parse_mode="HTML")

# --- QOLGANLAR ---
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer("Tez orada qo'shiladi! 🛠")

# --------------------------------------------------------------------------------
# BOTNI YURGIZISH
# --------------------------------------------------------------------------------
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
