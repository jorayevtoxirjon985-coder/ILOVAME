import asyncio
import logging
import random
import os
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# --------------------------------------------------------------------------------
# 1. SOZLAMALAR
# --------------------------------------------------------------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("XATOLIK: BOT_TOKEN topilmadi! Railway Variables bo'limini tekshiring.")
    sys.exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# --------------------------------------------------------------------------------
# 2. FAYL IDLARI (ENG MUHIM JOYI)
# Botga fayl tashlab, olingan ID larni shu yerga qo'shtirnoq ichiga yozing.
# --------------------------------------------------------------------------------
FILE_IDS = {
    "capcut": "",       # Masalan: "BQACAgIAAxkBAAI..."
    "inshot": "",
    "instagram": "",
    "spotify": "",
    "tiktok": "",
    "vpn": "",
    "nomer_apk": "",
    "diskdigger": "",
    "clash": "",
    "wamr": "",
    "instander": "",
    "fake_call": "",
    "call_recorder": "",
    "lock_app": "",
    "aka_messenger": "",
}

# --------------------------------------------------------------------------------
# 3. PROMPTLAR
# --------------------------------------------------------------------------------
portrait_prompts = [
    "Create a realistic behind-the-scenes selfie on a film set inspired by the HBO series Game of Thrones...",
    "Transform the selfie into a cinematic, moody side-profile portrait inspired by a DJ-style look...",
    "Surreal Y2K-style action shot of me mid-air in a dramatic leap...",
    "A young man with wearing a drop-shoulder t-shirt and baggy jeans... BMW E46 M3 background...",
    "Mantenha exatamente esse rosto. Um homem confiante, sentado em um luxuoso sofá de couro...",
]

# --------------------------------------------------------------------------------
# 4. MENYULAR
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
# 5. ID OLISH FUNKSIYASI (SIZ UCHUN)
# --------------------------------------------------------------------------------
@dp.message(F.document)
async def get_file_id_handler(message: types.Message):
    # Siz botga fayl tashlasangiz, u ID sini beradi
    file_id = message.document.file_id
    await message.reply(f"✅ **Fayl ID:**\n<code>{file_id}</code>\n\nNusxalab oling va kodning tepasidagi FILE_IDS ichiga qo'ying!", parse_mode="HTML")

# --------------------------------------------------------------------------------
# 6. ASOSIY START VA NAVIGATSIYA
# --------------------------------------------------------------------------------
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Assalomu alaykum! Ilovame botiga xush kelibsiz.", reply_markup=main_menu())

@dp.message(F.text == "Keyingi qator ➡️")
async def next_page(message: types.Message):
    await message.answer("Keyingi bo'lim:", reply_markup=second_menu())

@dp.message(F.text == "⬅️ Oldingi qator")
async def prev_page(message: types.Message):
    await message.answer("Asosiy menyu:", reply_markup=main_menu())

# --------------------------------------------------------------------------------
# 7. FAYL YUBORADIGAN HANDLERLAR
# --------------------------------------------------------------------------------

async def send_my_file(message, key, caption):
    """Fayl ID bor bo'lsa fayl tashlaydi, yo'q bo'lsa ogohlantiradi"""
    file_id = FILE_IDS.get(key)
    if file_id and len(file_id) > 5:
        await message.answer_document(document=file_id, caption=caption)
    else:
        await message.answer(f"⚠️ {caption}\n\nBu fayl hali bazaga yuklanmagan. Adminga xabar bering.")

# --- 1-MENYU ---

@dp.message(F.text == "Montaj ilovalari 📹")
async def send_montage(message: types.Message):
    await message.answer("Montaj ilovalari yuklanmoqda...")
    # CapCut
    await send_my_file(message, "capcut", "📥 **CapCut Pro** (Android)")
    # InShot
    await send_my_file(message, "inshot", "📥 **InShot Pro** (Android)")

@dp.message(F.text == "ChatGPT portret 🌅")
async def send_prompt(message: types.Message):
    prompt = random.choice(portrait_prompts)
    await message.answer(f"<b>Prompt:</b>\n\n<code>{prompt}</code>", parse_mode="HTML")

@dp.message(F.text == "Instagram Mod")
async def h_insta(message: types.Message):
    await send_my_file(message, "instagram", "📥 **Instagram Mod** (Instander)")

@dp.message(F.text == "Spotify Mod 🎵")
async def h_spotify(message: types.Message):
    await send_my_file(message, "spotify", "📥 **Spotify Premium**")

@dp.message(F.text == "TikTok Mod 📹")
async def h_tiktok(message: types.Message):
    await send_my_file(message, "tiktok", "📥 **TikTok Mod** (Suv belgisiz)")

@dp.message(F.text == "InShot Pro ✂️")
async def h_inshot(message: types.Message):
    await send_my_file(message, "inshot", "📥 **InShot Pro**")

@dp.message(F.text == "VPN Pro versiya 🌐")
async def h_vpn(message: types.Message):
    await send_my_file(message, "vpn", "📥 **AdGuard VPN**")

@dp.message(F.text == "Nomer aniqlash 🔍")
async def h_nomer(message: types.Message):
    await send_my_file(message, "nomer_apk", "🤖 **Android uchun: Sync.ME**")
    await message.answer("📱 **iPhone uchun:**\nhttps://apps.apple.com/uz/app/sync-me-caller-id-contacts/id340787494")

@dp.message(F.text == "Rasmlarni tiklash ♻️")
async def h_recover(message: types.Message):
    await send_my_file(message, "diskdigger", "📥 **DiskDigger Pro**")

@dp.message(F.text == "Mod O'yinlar 🎮")
async def h_games(message: types.Message):
    await send_my_file(message, "clash", "📥 **Clash of Clans Mod**")

# --- 2-MENYU ---

@dp.message(F.text.in_({"Android sirli ilovasi 🤫", "O'chgan smsni ko'rish 👀"}))
async def h_wamr(message: types.Message):
    await send_my_file(message, "wamr", "📥 **WAMR** (O'chgan SMSlarni o'qish)")

@dp.message(F.text == "Sharpa Telegram 👻")
async def h_ghost(message: types.Message):
    await send_my_file(message, "aka_messenger", "📥 **Aka Messenger** (Sharpa rejim)")

@dp.message(F.text == "Android VPN 🌐")
async def h_android_vpn(message: types.Message):
    await send_my_file(message, "vpn", "📥 **AdGuard VPN**")

@dp.message(F.text == "Cap Cut Pro tekin 📱")
async def h_capcut_free(message: types.Message):
    await send_my_file(message, "capcut", "📥 **CapCut Pro**")

@dp.message(F.text.in_({"Bir daqiqalik parol ✳️", "Telefon blok ilovasi 🔒"}))
async def h_lock(message: types.Message):
    await send_my_file(message, "lock_app", "📥 **Time Password**")

@dp.message(F.text == "Telefon Zapis 🔴")
async def h_recorder(message: types.Message):
    await send_my_file(message, "call_recorder", "📥 **Call Recorder**")

@dp.message(F.text == "Yolg'on qo'ng'iroq 📞")
async def h_fake_call(message: types.Message):
    await send_my_file(message, "fake_call", "📥 **Fake Call**")

@dp.message(F.text == "Reklamasiz Instagram ❗️")
async def h_instander(message: types.Message):
    await send_my_file(message, "instander", "📥 **Instander**")

@dp.message(F.text == "O'yin uchun ilova 🎮")
async def h_airconsole(message: types.Message):
    await message.answer("<b>AirConsole:</b>\n<a href='https://play.google.com/store/apps/details?id=com.airconsole.controller'>Yuklab olish</a>", parse_mode="HTML")

@dp.message(F.text == "Montaj ilovasi 👌")
async def h_gravity(message: types.Message):
    await message.answer("<b>Gravity (iPhone):</b>\n<a href='https://apps.apple.com/uz/app/gravity-augmented-reality/id1400961806'>Yuklab olish</a>", parse_mode="HTML")

@dp.message(F.text == "Android ilovalar 🧩")
async def h_android_apps(message: types.Message):
    await message.answer("<b>ZFont:</b>\n<a href='https://play.google.com/store/apps/details?id=com.htetznaing.zfont2'>Yuklab olish</a>", parse_mode="HTML")

@dp.message(F.text == "Telegramda Pul ishlash 🤩")
async def h_money(message: types.Message):
    await message.answer("<b>GenkiMiner:</b>\n👉 <a href='https://t.me/GenkiMinerBot/kapkap?startapp=T2xLOZii'>O'yinni boshlash</a>", parse_mode="HTML")

@dp.message(F.text == "PUL ISHLASH 🤑")
async def h_earn_money(message: types.Message):
    await message.answer("<b>GenkiMiner:</b>\n👉 <a href='https://t.me/GenkiMinerBot/kapkap?startapp=T2xLOZii'>Boshlash</a>", parse_mode="HTML")

@dp.message(F.text == "🔊 Dinamika ilovasi")
async def h_volume(message: types.Message):
    await message.answer("<b>Volume Styles:</b>\n<a href='https://play.google.com/store/apps/details?id=com.tombayley.volumepanel'>Yuklab olish</a>", parse_mode="HTML")

@dp.message(F.text == "AI Video 🎥")
async def h_ai_video(message: types.Message):
    await message.answer("Rasm: https://gemini.google.com/app\nVideo: https://deevid.ai/", parse_mode="HTML")

@dp.message(F.text == "Minusovka ajratish 🎼")
async def h_moises(message: types.Message):
    await message.answer("<b>Moises:</b>\n<a href='https://play.google.com/store/apps/details?id=ai.moises'>Yuklab olish</a>", parse_mode="HTML")

@dp.message(F.text == "Stiker yasash 🧩")
async def h_stickers(message: types.Message):
    await message.answer("Bot: @Stickers")

@dp.message(F.text == "Spamdan chiqish 🚫")
async def h_spam(message: types.Message):
    await message.answer("Bot: @SpamBot ga yozing.")

@dp.message(F.text == "Kontakt ilova 📞")
async def h_contacts(message: types.Message):
    await message.answer("<b>Google Contacts:</b>\n<a href='https://play.google.com/store/apps/details?id=com.google.android.contacts'>Yuklab olish</a>", parse_mode="HTML")

@dp.message(F.text == "📱 Boshqa telefonga ulanish")
async def h_anydesk(message: types.Message):
    await message.answer("<b>AnyDesk:</b>\n<a href='https://play.google.com/store/apps/details?id=com.anydesk.anydeskandroid'>Yuklab olish</a>", parse_mode="HTML")

@dp.message(F.text == "“теневой бан”dan chiqish")
async def h_shadowban(message: types.Message):
    await message.answer("Instagram sozlamalaridan 'Report a problem' qiling.")

@dp.message(F.text == "O'xshash qiyofa 🤠")
async def h_lookalike(message: types.Message):
    await message.answer("Gradient ilovasini Play Marketdan oling.")

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
