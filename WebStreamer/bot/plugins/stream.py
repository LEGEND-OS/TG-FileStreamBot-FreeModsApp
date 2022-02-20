# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import logging
from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from WebStreamer.utils import get_hash, get_name
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant



@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def media_receive_handler(c, m: Message):
     if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status in ["kicked", "banned"]:
                await c.send_message(
                    chat_id=m.chat.id,
                    text="__You are Banned in Our Updates Channel ❌__\n\n  **Contact @LegendAkshay**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""<i>This Is a Private Bot For our Streaam.net Users, You have to Join Our Telegram Channel To Verify You</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [[ InlineKeyboardButton("JOIN", url=f"https://t.me/{Var.UPDATES_CHANNEL}") ]]
                ),
                parse_mode="HTML"
            )
            return
        except Exception:
            await c.send_message(
                chat_id=m.chat.id,
                text="**Something Went Wrong Contact Dev** @LegendAkshay",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = f"{Var.URL}{log_msg.message_id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
    short_link = f"{Var.URL}{get_hash(log_msg)}{log_msg.message_id}"
    logging.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    await log_msg.reply_text(text=f"Requested by [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**User ID:** `{m.from_user.id}`\n**Download Link:** {stream_link}\n**Rapid Link:** {short_link}", disable_web_page_preview=True, parse_mode="Markdown", quote=True)
    await m.reply_text(
        text="<i>Your Remote Upload Link Generated.</i>\n\nLink 🔗 :<code>{}</code>\n\n<b>🔥Copy This Link & Paste In Your Streaam.net Dashboard In Remote Upload to Upload This Video.</b>\n\n💥Contact For Any Help @SID12O".format(
            stream_link, short_link
        ),
        quote=True,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Open", url=stream_link)]]
        ),
    )
