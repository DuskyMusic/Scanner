# Copyright (Β©οΈ) @KIRITO_1240
# By : KIRITO

from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Chat, Message, User

from Scanner.vars import SUPPORT_CHAT
from Scanner import ubot

@ubot.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: ubot, message: Message):
  await ubot.send_message(message.chat.id,f"Hey π I'm The Assistant Of π©ββ πΏππππβππππππ ββπͺ, Didn't Have A Time To Talk With You π So Kindly Join @{SUPPORT_CHAT} For Getting Support.")
  return
