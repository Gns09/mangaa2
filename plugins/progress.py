from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from translation import Translation
from config import Config


@Client.on_message(filters.private & filters.text)
def download(bot, update):
    if update.from_user.id != Config.OWNER_ID:
        return
    url = update.text

    update.reply_text(Translation.UPLOAD, quote=True, reply_markup=InlineKeyboardMarkup(Translation.upload_buttons))
