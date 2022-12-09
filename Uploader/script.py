# MIT License

# Copyright (c) 2022 Hash Minner

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    START_TEXT = """
**Hi** {} 

**I ᴀᴍ Pᴏᴡᴇʀғᴜʟ Uʀʟ Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ**
 
"""

    HELP_TEXT = """

# **Sᴇɴᴅ Mᴇ Tʜᴇ Gᴏᴏɢʟᴇ Dʀɪᴠᴇ | Yᴛᴅʟ | Dɪʀᴇᴄᴛ Lɪɴᴋѕ.**

# **Sᴇʟᴇᴄᴛ Tʜᴇ Dᴇѕɪʀᴇᴅ Oᴘᴛɪᴏɴ..**

# **Yᴏᴜʀ Fɪʟᴇ Wɪʟʟ Bᴇ Uᴘʟᴏᴀᴅᴇᴅ Sᴏᴏɴ‌‌..**
 
"""

# give credit to developer

    ABOUT_TEXT = """
<b>♻️ Mʏ Nᴀᴍᴇ</b> : **Uʀʟ Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ**

<b>🌀 Pᴏᴡᴇʀᴇᴅ Bʏ</b> : **@A7_SYR**

<b>📑 Lᴀɴɢᴜᴀɢᴇ :</b> <a href="https://www.python.org/">Python 3.10.5</a>

<b>🇵🇲 Fʀᴀᴍᴇᴡᴏʀᴋ :</b> <a href="https://docs.pyrogram.org/">Pyrogram 2.0.30</a>


"""

    PROGRESS = """
🚀 Sᴘᴇᴇᴅ : {3}/s\n\n
✅ Dᴏɴᴇ : {1}\n\n
💿 Tᴏᴛᴀʟ Sɪᴢᴇ  : {2}\n\n
⏳ Tɪᴍᴇ Lᴇғᴛ : {4}\n\n
"""
    ID_TEXT = """
🆔 Your Telegram ID 𝐢𝐬 :- <code>{}</code>
"""

    INFO_TEXT = """

 🤹 First Name : <b>{}</b>

 🚴‍♂️ Second Name : <b>{}</b>

 🧑🏻‍🎓 Username : <b>@{}</b>

 🆔 Telegram Id : <code>{}</code>

 📇 Profile Link : <b>{}</b>

 📡 Dc : <b>{}</b>

 📑 Language : <b>{}</b>

 👲 Status : <b>{}</b>
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('❓ Hᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('🦊 Aʙᴏᴜᴛ', callback_data='about')
        ], [
            InlineKeyboardButton('📛 Cʟᴏѕᴇ', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏠 Hᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('🦊 Aʙᴏᴜᴛ', callback_data='about')
        ], [
            InlineKeyboardButton('📛 Cʟᴏѕᴇ', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏠 Hᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('❓ Hᴇʟᴘ', callback_data='help')
        ], [
            InlineKeyboardButton('📛 Cʟᴏѕᴇ', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📛 Cʟᴏѕᴇ', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = "**Nᴏᴡ Sᴇʟᴇᴄᴛ Tʜᴇ Dᴇѕɪʀᴇᴅ Fᴏʀᴍᴀᴛѕ**"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "**Tʀʏɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅ**⌛\n\n <i>{} </i>"
    UPLOAD_START = "<i>{} </i>\n\n📤 **Uᴘʟᴏᴀᴅɪɴɢ Pʟᴇᴀѕᴇ Wᴀɪᴛ**"
    RCHD_TG_API_LIMIT = "**Dᴏᴡɴʟᴏᴀᴅᴇᴅ Iɴ** {} Sᴇᴄᴏɴᴅѕ.\nDᴇᴛᴇᴄᴛᴇᴅ Fɪʟᴇ Sɪᴢᴇ: {}\nSᴏʀʀʏ. ʙᴜᴛ, ɪ ᴄᴀɴɴᴏᴛ ᴜᴘʟᴏᴀᴅ ғɪʟᴇѕ ɢʀᴇᴀᴛᴇʀ ᴛʜᴀɴ 2ɢʙ ᴅᴜᴇ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴘɪ ʟɪᴍɪᴛᴀᴛɪᴏɴѕ.."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n\nTʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ\n\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Mᴇᴅɪᴀ Cʟᴇᴀʀᴇᴅ Sᴜᴄᴄᴇѕғᴜʟʟʏ."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_VOID_FORMAT_FOUND = "Eʀʀᴏʀ... <code>{}</code>"
    SLOW_URL_DECED = "Gᴏѕʜ ᴛʜᴀᴛ ѕᴇᴇᴍѕ ᴛᴏ ʙᴇ ᴀ ᴠᴇʀʏ ѕʟᴏᴡ ᴜʀʟ. ѕɪɴᴄᴇ ʏᴏᴜ ᴡᴇʀᴇ ѕᴄʀᴇᴡɪɴɢ ᴍʏ ʜᴏᴍᴇ, ɪ ᴀᴍ ɪɴ ɴᴏ ᴍᴏᴏᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜɪѕ ғɪʟᴇ. ᴍᴇᴀɴᴡʜɪʟᴇ, ᴡʜʏ ᴅᴏɴ'ᴛ ʏᴏᴜ ᴛʀʏ ᴛʜɪѕ:==> https://shrtz.me/PtsVnf6 ᴀɴᴅ ɢᴇᴛ ᴍᴇ ᴀ ғᴀѕᴛ ᴜʀʟ ѕᴏ ᴛʜᴀᴛ ɪ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ, ᴡɪᴛʜᴏᴜᴛ ᴍᴇ ѕʟᴏᴡɪɴɢ ᴅᴏᴡɴ ғᴏʀ ᴏᴛʜᴇʀ ᴜѕᴇʀѕ."
