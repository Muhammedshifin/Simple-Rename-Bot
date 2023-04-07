from pyrogram import Client, filters, errors, enums
from pyrogram import idle
from config import *

API_ID = int(environ.get('API_ID', "18302370"))
API_HASH = environ.get('API_HASH', "03c2cced4dea9b1e96dce87558dd2381")
SESSION = environ.get('SESSION', "BQCjLnL8egVI1vOcV0GE8JfJPMYSHIWWSXjl1V2d8JPhkQIXPuCis4xek4hhOaK3FBLB9d1XUkcjgzdoImdcekCLarcWkdqXnLuYlW4KKAd8YL9xYBDt3y9FQFLD5MlHKyIWUsfMOWo8TRhoovJ_SF17G-egyPtvW_1L65gcp-Uz1l3dn2Ac4cZ3dl6hX5-RZkOz_iEharA8nVyjFWy5hPPoA8RTmc4kSi1PjF701HKP2OgMWV3uBRsl-D3BD-NXzmzbcY8FlPRol1inPbN-vWy9lTM5Yg7hqtJvO3dL9wHEVhOVJMOY48XsBOtMjB7C63jo--HBlYyTWYL1AmRYJcjaAAAAAU2Yx_4A")

User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              #Removed
              workers=300
              )

