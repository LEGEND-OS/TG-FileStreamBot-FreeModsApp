# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from pyrogram.errors import UserNotParticipant


@StreamBot.on_message(filters.private)
async def unauth(_, m: Message):
 if m.from_user.id not in Var.AUTH_USERS:
  await m.reply_text("You are not Authorized User, Msg Me To Be Auth Users")

async def start(c, m: Message):
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
    await m.reply(
        f'**Hi {m.from_user.mention(style="md")},\nSend or Forward Me Any File Here Which You Want To Upload Remotely In Streaam.net.**'
    )

