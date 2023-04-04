import time
import os
from pyrogram import Client, filters, enums
from config import temp, CAPTION, ADMIN, log_chat
from main.utils import progress_message, humanbytes
from userbot import User
import humanize

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
    media = await client.get_messages(message.chat.id,message.id)
		file = media.document or media.video or media.audio 
    filename = file.file_name
    

@Client.on_message(filters.private & filters.command("rename") & filters.user(ADMIN))             
async def rename_file(bot, msg):
    reply = msg.reply_to_message
    if len(msg.command) < 2 or not reply:
       return await msg.reply_text("Please Reply To An File or video or audio With filename + .extension eg:-(`.mkv` or `.mp4` or `.zip`)")
    media = reply.document or reply.audio or reply.video
    if not media:
       await msg.reply_text("Please Reply To An File or video or audio With filename + .extension eg:-(`.mkv` or `.mp4` or `.zip`)")
    og_media = getattr(reply, reply.media.value)
    new_name = msg.text.split(" ", 1)[1]
    sts = await msg.reply_text("Trying to Downloading.....")
    c_time = time.time()
    downloaded = await reply.download(file_name=new_name, progress=progress_message, progress_args=("Download Started.....", sts, c_time)) 
    filesize = humanbytes(og_media.file_size)                
    if CAPTION:
        try:
            cap = CAPTION.format(file_name=new_name, file_size=filesize)
        except Exception as e:            
            await sts.edit(text=f"Your caption Error unexpected keyword ●> ({e})")
            return
    else:
        cap = f"{new_name}\n\n💽 size : {filesize}"
    raw_thumbnail = temp.THUMBNAIL 
    if raw_thumbnail:
        og_thumbnail = await bot.download_media(raw_thumbnail)
    else:
        og_thumbnail = await bot.download_media(og_media.thumbs[0].file_id)
    await sts.edit("Trying to Uploading")
    c_time = time.time()
    try:
        filw = await User.send_document(log_chat, document=downloaded, thumb=og_thumbnail, caption=cap, progress=progress_message, progress_args=("Uploade Started.....", sts, c_time))    
        from_chat = filw.chat.id
        #gige😑 
        mg_id = filw.id
        await bot.copy_message(msg.from_user.id,from_chat,mg_id)
    except Exception as e:  
        await sts.edit(f"Error {e}") 
        return               
    try:
        os.remove(downloaded)
        os.remove(og_thumbnail)
    except:
        pass
    await sts.delete()
