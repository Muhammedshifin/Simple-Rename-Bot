from pyrogram import Client, filters, errors, enums
from pyrogram import idle
from config import *

API_ID = int(environ.get('API_ID', "18302370"))
API_HASH = environ.get('API_HASH', "03c2cced4dea9b1e96dce87558dd2381")
SESSION = environ.get('SESSION', "BQAcUG3cdKOCZ_u28YDsK057xGPtV1DfkD5_B3oTDgJcPrDH2tkxcFLdoh8zaFQqy81scqWFl6nVnZgR_zmbl11u1wYKvLXFr8w7sxEWvi-bk7o0ZH38sGvuljMOGBetcKpsLq6P09KxJhhGHDE7h-SBtpM6RWfhDGttzjlHlW0lokOmQIf3wCtyojgeYLTvLKQ9pNHakViwSfjSF7xaz6SudbSbUY7hdsjv2Lg0coOQUMf06Jn6P5yTfxCzXu_i7g-At_SJgKQl9pWduMZ6lKpwpyLnEuxYfDdxmufs3LV0qNHITEF0LZ1VpeR4xEgJBn88CnbNehivfFeEEbhOiwA0AAAAAXOcqTkA")

User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              #Removed
              workers=300
              )

