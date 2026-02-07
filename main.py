import asyncio
import logging
import random
import os
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

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
# 2. PROMPTLAR (MATNLAR)
# --------------------------------------------------------------------------------
portrait_prompts = [
    "Create a realistic behind-the-scenes selfie on a film set inspired by the HBO series Game of Thrones...",
    "Transform the selfie into a cinematic, moody side-profile portrait inspired by a DJ-style look...",
    "Surreal Y2K-style action shot of me mid-air in a dramatic leap...",
    "A young man with wearing a drop-shoulder t-shirt and baggy jeans... BMW E46 M3 background...",
    "Mantenha exatamente esse rosto. Um homem confiante, sentado em um luxuoso sofá de couro...",
]

# --------------------------------------------------------------------------------
# 3. YORDAMCHI: SSILKA TUGMASINI YASASH
# --------------------------------------------------------------------------------
def link_btn(text, url):
    kb = InlineKeyboardBuilder()
    kb.button(text=f"📥 {text}ni yuklab olish", url=url)
    return kb.as_markup()

# --------------------------------------------------------------------------------
# 4. ASOSIY MENYULAR (TUGMALAR)
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
# 5. HANDLERLAR (JAVOBLAR)
# --------------------------------------------------------------------------------

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Assalomu alaykum! Ilovame botiga xush kelibsiz.\nKerakli bo'limni tanlang:", reply_markup=main_menu())

@dp.message(F.text == "Keyingi qator ➡️")
async def next_page(message: types.Message):
    await message.answer("Keyingi bo'lim:", reply_markup=second_menu())

@dp.message(F.text == "⬅️ Oldingi qator")
async def prev_page(message: types.Message):
    await message.answer("Asosiy menyu:", reply_markup=main_menu())

# --- 1-MENYU TUGMALARI (PLAY MARKETGA YO'NALTIRISH) ---

@dp.message(F.text == "Montaj ilovalari 📹")
async def send_montage(message: types.Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="📥 CapCut (Play Market)", url="https://play.google.com/store/apps/details?id=com.lemon.lvoverseas")
    kb.button(text="📥 InShot (Play Market)", url="https://play.google.com/store/apps/details?id=com.camerasideas.instashot")
    await message.answer("Montaj uchun eng zo'r ilovalar (Rasmiy):", reply_markup=kb.as_markup())

@dp.message(F.text == "ChatGPT portret 🌅")
async def send_prompt(message: types.Message):
    prompt = random.choice(portrait_prompts)
    await message.answer(f"<b>Prompt (Nusxalab oling):</b>\n\n<code>{prompt}</code>", parse_mode="HTML")

@dp.message(F.text == "Instagram Mod")
async def h_insta(message: types.Message):
    # Instander (Eng ishonchli mod sayti)
    await message.answer("Instagram Mod (Instander) ni yuklab olish:", reply_markup=link_btn("Instander Sayti", "https://thedise.me/instander/"))

@dp.message(F.text == "Spotify Mod 🎵")
async def h_spotify(message: types.Message):
    await message.answer("Spotify Mod (XManager) ni yuklab olish:", reply_markup=link_btn("XManager Sayti", "https://xmanagerapp.com/"))

@dp.message(F.text == "TikTok Mod 📹")
async def h_tiktok(message: types.Message):
    await message.answer("TikTok Mod (Plugin) yuklab olish:", reply_markup=link_btn("TikTok Mod Kanal", "https://t.me/tiktokmod_cloud"))

@dp.message(F.text == "InShot Pro ✂️")
async def h_inshot(message: types.Message):
    await message.answer("InShot yuklab olish:", reply_markup=link_btn("InShot (Play Market)", "https://play.google.com/store/apps/details?id=com.camerasideas.instashot"))

@dp.message(F.text == "VPN Pro versiya 🌐")
async def h_vpn(message: types.Message):
    await message.answer("AdGuard VPN (Tezkor va xavfsiz):", reply_markup=link_btn("AdGuard VPN", "https://play.google.com/store/apps/details?id=com.adguard.vpn"))

@dp.message(F.text == "Nomer aniqlash 🔍")
async def h_nomer(message: types.Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="🤖 Android uchun", url="https://play.google.com/store/apps/details?id=com.syncme.syncmeapp")
    kb.button(text="📱 iPhone uchun", url="https://apps.apple.com/uz/app/sync-me-caller-id-contacts/id340787494")
    await message.answer("Nomer aniqlash ilovasi (Sync.ME):", reply_markup=kb.as_markup())

@dp.message(F.text == "Rasmlarni tiklash ♻️")
async def h_recover(message: types.Message):
    await message.answer("DiskDigger (Rasmlarni tiklash):", reply_markup=link_btn("DiskDigger", "https://play.google.com/store/apps/details?id=com.defianttech.diskdigger"))

@dp.message(F.text == "Mod O'yinlar 🎮")
async def h_games(message: types.Message):
    await message.answer("Clash of Clans va boshqa mod o'yinlar:", reply_markup=link_btn("HappyMod Sayti", "https://happymod.com/"))

# --- 2-MENYU TUGMALARI ---

@dp.message(F.text == "Montaj ilovasi 👌")
async def h_gravity(message: types.Message):
    await message.answer("Gravity (iPhone uchun):", reply_markup=link_btn("Gravity (App Store)", "https://apps.apple.com/uz/app/gravity-augmented-reality/id1400961806"))

@dp.message(F.text == "Android ilovalar 🧩")
async def h_android_apps(message: types.Message):
    await message.answer("ZFont (iPhone Emojilari):", reply_markup=link_btn("zFont (Play Market)", "https://play.google.com/store/apps/details?id=com.htetznaing.zfont2"))

@dp.message(F.text == "Telegramda Pul ishlash 🤩")
async def h_money(message: types.Message):
    await message.answer("GenkiMiner (Pul ishlash o'yini):", reply_markup=link_btn("O'yinni boshlash", "https://t.me/GenkiMinerBot/kapkap?startapp=T2xLOZii"))

@dp.message(F.text == "🔊 Dinamika ilovasi")
async def h_volume(message: types.Message):
    await message.answer("Volume Styles (Dinamika):", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=com.tombayley.volumepanel"))

@dp.message(F.text == "AI Video 🎥")
async def h_ai_video(message: types.Message):
    text = "Rasm uchun: https://gemini.google.com/app\nVideo uchun: https://deevid.ai/"
    await message.answer(text, disable_web_page_preview=True)

@dp.message(F.text.in_({"Android sirli ilovasi 🤫", "O'chgan smsni ko'rish 👀"}))
async def h_wamr(message: types.Message):
    await message.answer("WAMR (O'chgan SMSlarni o'qish):", reply_markup=link_btn("WAMR (Play Market)", "https://play.google.com/store/apps/details?id=com.drilens.wamr"))

@dp.message(F.text == "PUL ISHLASH 🤑")
async def h_earn_money(message: types.Message):
    await message.answer("USDT ishlash uchun bot:", reply_markup=link_btn("Boshlash", "https://t.me/GenkiMinerBot/kapkap?startapp=T2xLOZii"))

@dp.message(F.text == "Sharpa Telegram 👻")
async def h_ghost(message: types.Message):
    await message.answer("Aka Messenger (Sharpa rejim):", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=org.aka.messenger"))

@dp.message(F.text == "Android VPN 🌐")
async def h_android_vpn(message: types.Message):
    await message.answer("AdGuard VPN:", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=com.adguard.vpn"))

@dp.message(F.text == "Cap Cut Pro tekin 📱")
async def h_capcut_free(message: types.Message):
    await message.answer("CapCut (So'nggi versiya):", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=com.lemon.lvoverseas"))

@dp.message(F.text == "Minusovka ajratish 🎼")
async def h_moises(message: types.Message):
    await message.answer("Moises (Musiqa ajratish):", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=ai.moises"))

@dp.message(F.text == "Stiker yasash 🧩")
async def h_stickers(message: types.Message):
    await message.answer("Stiker yasash uchun bot: @Stickers (Telegram rasmiy boti)")

@dp.message(F.text == "Spamdan chiqish 🚫")
async def h_spam(message: types.Message):
    await message.answer("Spamdan chiqish uchun: @SpamBot ga kirib yozing.")

@dp.message(F.text == "Kontakt ilova 📞")
async def h_contacts(message: types.Message):
    await message.answer("Google Contacts:", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=com.google.android.contacts"))

@dp.message(F.text == "📱 Boshqa telefonga ulanish")
async def h_anydesk(message: types.Message):
    await message.answer("AnyDesk (Masofadan boshqarish):", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=com.anydesk.anydeskandroid"))

@dp.message(F.text.in_({"Bir daqiqalik parol ✳️", "Telefon blok ilovasi 🔒"}))
async def h_lock(message: types.Message):
    await message.answer("Screen Lock Time Password:", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=com.miragestacks.screenlock.timepassword"))

@dp.message(F.text == "Telefon Zapis 🔴")
async def h_recorder(message: types.Message):
    await message.answer("Call Recorder:", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=com.catalinagroup.callrecorder"))

@dp.message(F.text == "Yolg'on qo'ng'iroq 📞")
async def h_fake_call(message: types.Message):
    await message.answer("Fake Call (Prank):", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=com.fungame.fakecall.prankfriend"))

@dp.message(F.text == "Reklamasiz Instagram ❗️")
async def h_instander(message: types.Message):
    await message.answer("Instander (Reklamasiz Instagram):", reply_markup=link_btn("Yuklab olish", "https://thedise.me/instander/"))

@dp.message(F.text == "O'yin uchun ilova 🎮")
async def h_airconsole(message: types.Message):
    await message.answer("AirConsole:", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=com.airconsole.controller"))

@dp.message(F.text == "“теневой бан”dan chiqish")
async def h_shadowban(message: types.Message):
    await message.answer("Shadow Ban dan chiqish uchun Instagram sozlamalaridan 'Help' -> 'Report a problem' qiling.")

@dp.message(F.text == "O'xshash qiyofa 🤠")
async def h_lookalike(message: types.Message):
    await message.answer("Gradient ilovasi:", reply_markup=link_btn("Yuklab olish", "https://play.google.com/store/apps/details?id=com.ticktick.gradient"))

# --- QOLGANLAR ---
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer("Bu bo'lim tez orada qo'shiladi! 🛠")

# --------------------------------------------------------------------------------
# BOTNI YURGIZISH
# --------------------------------------------------------------------------------
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
