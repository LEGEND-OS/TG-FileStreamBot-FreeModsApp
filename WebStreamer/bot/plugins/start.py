# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from pyrogram.errors import UserNotParticipant


@StreamBot.on_message(filters.private & filters.command(["start", "help"]))
async def unauth(_, m: Message):
 if m.from_user.id not in Var.AUTH_USERS:
  await m.reply_text("**This Bot is Only For Authorised Users of Streaam.net**\n\n__Contact @LegendAkshay Or @SID12O__")
 if m.from_user.id in Var.AUTH_USERS:
  await m.reply_text(
        f'**Hi {m.from_user.mention(style="md")},\nSend or Forward Me Any File Here Which You Want To Upload Remotely In Streaam.net.**'
    )

