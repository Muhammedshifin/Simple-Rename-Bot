from pyrogram import Client, filters, errors, enums
from pyrogram import idle


API_ID = int(environ.get('API_ID', "18302370"))
API_HASH = environ.get('API_HASH', "03c2cced4dea9b1e96dce87558dd2381")
SESSION = environ.get('SESSION', "")

User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              #Removed
              workers=300
              )

User.start()
print("User Started!")

idle()

User.stop()
print("User Stopped!")
