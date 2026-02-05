import asyncio
import logging
import random
import os
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# --------------------------------------------------------------------------------
# 1. SOZLAMALAR (RAILWAYDAN O'QISH)
# --------------------------------------------------------------------------------
# Railway "Variables" bo'limidan tokenni oladi
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Agar token topilmasa, xato berib o'chadi
if not BOT_TOKEN:
    print("XATOLIK: BOT_TOKEN topilmadi! Railway Variables bo'limini tekshiring.")
    sys.exit(1)

# MAJBURIY OBUNA UCHUN KANAL (Boshida @ belgisini qo'ying)
CHANNEL_USERNAME = "@muhammadjonov_world" 
CHANNEL_LINK = "https://t.me/muhammadjonov_world"

# Botni ishga tushiramiz
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# --------------------------------------------------------------------------------
# 2. YORDAMCHI FUNKSIYALAR (OBUNA TEKSHIRISH)
# --------------------------------------------------------------------------------
async def check_sub_channel(user_id):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        # Agar a'zo bo'lsa, admin yoki yaratuvchi bo'lsa - True qaytaradi
        if member.status in ['creator', 'administrator', 'member']:
            return True
        return False
    except Exception as e:
        # Agar bot kanalga admin qilinmagan bo'lsa, xato beradi
        logging.error(f"Kanalni tekshirishda xatolik: {e}")
        return False

def sub_inline_keyboard():
    # Obuna bo'lish tugmasi
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📢 Kanalga a'zo bo'lish", url=CHANNEL_LINK)],
        [InlineKeyboardButton(text="✅ A'zo bo'ldim (Tekshirish)", callback_data="check_subscription")]
    ])
    return keyboard

# --------------------------------------------------------------------------------
# 3. MENYULAR (TUGMALAR)
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
# 4. MA'LUMOTLAR VA PROMPTLAR
# --------------------------------------------------------------------------------
portrait_prompts = [
    """Create a realistic behind-the-scenes selfie on a film set inspired by the HBO series "Game of Thrones"...""",
    """Transform the selfie into a cinematic, moody side-profile portrait inspired by a DJ-style look...""",
    """Surreal Y2K-style action shot of me mid-air in a dramatic leap..."""
]

# --------------------------------------------------------------------------------
# 5. HANDLERS (JAVOBLAR)
# --------------------------------------------------------------------------------

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Obunani tekshirish
    is_subscribed = await check_sub_channel(message.from_user.id)
    if not is_subscribed:
        await message.answer(
            f"❌ <b>Botdan foydalanish uchun kanalimizga a'zo bo'lishingiz shart!</b>\n\nIltimos, pastdagi tugma orqali {CHANNEL_USERNAME} kanaliga qo'shiling va 'A'zo bo'ldim' tugmasini bosing.",
            reply_markup=sub_inline_keyboard(),
            parse_mode="HTML"
        )
        return

    await message.answer("Assalomu alaykum! Ilovame botiga xush kelibsiz.\nSizga kerakli xizmatni tanlang:", reply_markup=main_menu())

# --- OBUNA TEKSHIRISH TUGMASI BOSILGANDA ---
@dp.callback_query(F.data == "check_subscription")
async def callback_check_sub(callback: CallbackQuery):
    is_subscribed = await check_sub_channel(callback.from_user.id)
    
    if is_subscribed:
        await callback.message.delete() # Eski xabarni o'chirish
        await callback.message.answer("✅ Rahmat! Siz muvaffaqiyatli a'zo bo'ldingiz.\nMarhamat, menyudan foydalaning:", reply_markup=main_menu())
    else:
        await callback.answer("❌ Siz hali kanalga a'zo bo'lmadingiz!", show_alert=True)

# --- NAVIGATSIYA ---
@dp.message(F.text == "Keyingi qator ➡️")
async def next_page(message: types.Message):
    if not await check_sub_channel(message.from_user.id):
        return await message.answer("Botdan foydalanish uchun kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer("Keyingi bo'lim:", reply_markup=second_menu())

@dp.message(F.text == "⬅️ Oldingi qator")
async def prev_page(message: types.Message):
    if not await check_sub_channel(message.from_user.id):
        return await message.answer("Botdan foydalanish uchun kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer("Asosiy menyu:", reply_markup=main_menu())

# --- APK FAYLLAR (FILE ID'LARNI TO'LDIRIB CHIQING) ---
@dp.message(F.text == "Instagram Mod")
async def send_insta(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    # FILE ID QUYING
    await message.answer_document(document="FILE_ID_INSTAGRAM_MOD", caption="📥 **Instagram Mod (InstaPro)**")

@dp.message(F.text == "Spotify Mod 🎵")
async def send_spotify(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer_document(document="FILE_ID_SPOTIFY", caption="📥 **Spotify Premium Mod**")

@dp.message(F.text == "TikTok Mod 📹")
async def send_tiktok(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer_document(document="FILE_ID_TIKTOK", caption="📥 **TikTok Mod (No Watermark)**")

@dp.message(F.text == "InShot Pro ✂️")
async def send_inshot(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer_document(document="FILE_ID_INSHOT", caption="📥 **InShot Pro**")

@dp.message(F.text == "VPN Pro versiya 🌐")
async def send_vpn(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer_document(document="FILE_ID_VPN", caption="📥 **AdGuard VPN Mod**")

@dp.message(F.text == "Rasmlarni tiklash ♻️")
async def send_recovery(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer_document(document="FILE_ID_DISK_DIGGER", caption="📥 **DiskDigger Pro**")

@dp.message(F.text == "Mod O'yinlar 🎮")
async def send_games(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer_document(document="FILE_ID_CLASH", caption="📥 **Clash of Clans Mod**")

@dp.message(F.text == "Cap Cut Pro tekin 📱")
async def send_capcut(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer_document(document="FILE_ID_CAPCUT", caption="📥 **CapCut Pro**")

@dp.message(F.text == "Minusovka ajratish 🎼")
async def send_minus(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer_document(document="FILE_ID_MOISES", caption="📥 **Moises AI**")

@dp.message(F.text == "Stiker yasash 🧩")
async def send_sticker_app(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer_document(document="FILE_ID_STICKER_MAKER", caption="📥 **Sticker Maker**")

# --- SSILKALAR VA MATNLAR ---

@dp.message(F.text == "Nomer aniqlash 🔍")
async def send_caller_id(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    text = """<b>Nomer aniqlash:</b>\n📱 iPhone: <a href="https://apps.apple.com/uz/app/sync-me-caller-id-contacts/id340787494">Yuklab olish</a>\n🤖 Android: <a href="https://play.google.com/store/apps/details?id=com.syncme.syncmeapp">Yuklab olish</a>"""
    await message.answer(text, parse_mode="HTML", disable_web_page_preview=True)

@dp.message(F.text == "Telegramda Pul ishlash 🤩")
async def send_money_bot(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer("<b>GenkiMinerBot:</b>\n👉 <a href='https://t.me/GenkiMinerBot/kapkap?startapp=T2xLOZii'>O'yinni boshlash</a>", parse_mode="HTML")

@dp.message(F.text == "Sharpa Telegram 👻")
async def send_proxy(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer("<b>Proxy:</b>\n<a href='https://t.me/proxy?server=...'>Ulanish uchun bosing</a>", parse_mode="HTML")

@dp.message(F.text == "Spamdan chiqish 🚫")
async def send_spam_info(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer("<b>Spamdan chiqish:</b> @SpamBot ga kirib 'Bu xato' deb yozing.", parse_mode="HTML")

@dp.message(F.text == "Bir daqiqalik parol ✳️")
async def send_temp_mail(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer("Vaxtinchalik email: https://temp-mail.org/")

@dp.message(F.text == "ChatGPT portret 🌅")
async def send_ai_prompt(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    selected_prompt = random.choice(portrait_prompts)
    await message.answer(f"<b>Prompt:</b>\n<code>{selected_prompt}</code>", parse_mode="HTML")

@dp.message(F.text == "AI Video 🎥")
async def send_ai_video_tools(message: types.Message):
    if not await check_sub_channel(message.from_user.id): return await message.answer("Kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer("Rasm: https://gemini.google.com/app\nVideo: https://deevid.ai/", parse_mode="HTML")

# --- QOLGANLAR ---
@dp.message()
async def echo_handler(message: types.Message):
    if not await check_sub_channel(message.from_user.id):
        return await message.answer("Botdan foydalanish uchun kanalga a'zo bo'ling!", reply_markup=sub_inline_keyboard())
    await message.answer("Tez orada qo'shiladi! 🛠")

# --------------------------------------------------------------------------------
# BOTNI YURGIZISH
# --------------------------------------------------------------------------------
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
