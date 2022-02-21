# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils import user_in_streaam


@StreamBot.on_message(filters.command(["start", "help"]))
async def unauth(_, m: Message):
  if await user_in_streaam(m.chat.id):
    await m.reply_text(
          f'**Hi {m.from_user.mention(style="md")},\nSend or Forward Me Any File Here Which You Want To Upload Remotely In Streaam.net.**'
      )
  else:
    await m.reply_text(
        text="You don't have Account in Streaam.net "
    )
