# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from pyrogram.errors import UserNotParticipant


@StreamBot.on_message(filters.private & ~filters.user(Var.AUTH_USER))
async def unauth(_, m: Message):
        await m.reply_text(
        text='You are not Authorised Users, Msg Me to Be Auth User'
    )

@StreamBot.on_message(filters.command(["start", "help"]))
async def start(c, m: Message):
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="__Something Went Wrong ❌__\n\n  **Contact Dev @LegendAkshay To Report This Error**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""<i></i>""",
                reply_markup=InlineKeyboardMarkup(
                    [[ InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}") ]]
                ),
                parse_mode="HTML"
            )
            return
        except Exception:
            await c.send_message(
                chat_id=m.chat.id,
                text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍʏ ʙᴏss** @Avishkarpatil",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await m.reply(
        f'**Hi {m.from_user.mention(style="md")},\nSend or Forward Me Any File Here Which You Want To Upload Remotely In Streaam.net.**'
    )
