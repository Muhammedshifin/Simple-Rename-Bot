from pyrogram import Client
from config import *
from route import web_server
from aiohttp import web
from userbot import User
from main.webcode import bot_run
from os import environ
from aiohttp import web as webserver

PORT_CODE = environ.get("PORT", "8080")


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=10,
        )
    async def start(self):
        await super().start()
        me = await self.get_me()   
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        port = "8080"
        await web.TCPSite(app, bind_address, port).start()   
        print(f"{me.first_name} | @{me.username} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...⚡️")
        await self.send_message(text="Rename Started.. 🔥", chat_id=log_chat)

    async def stop(self, *args):
       await super().stop()      
       print("Bot Restarting........")
       
       client = webserver.AppRunner(await bot_run())
       await client.setup()
       bind_address = "0.0.0.0"
       await webserver.TCPSite(client, bind_address, PORT_CODE).start()

apps = [User]
for app in apps:
    app.start()    
    
bot = Bot()
bot.run()
