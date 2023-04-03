from pyrogram import Client, filters, errors, enums
from pyrogram import idle
from config import *

API_ID = int(environ.get('API_ID', "18302370"))
API_HASH = environ.get('API_HASH', "03c2cced4dea9b1e96dce87558dd2381")
SESSION = environ.get('SESSION', "BQDimrUAKQC-vbs2RIbp245-hLmJUUjqnloUomagXSZ20ekgt4C9qnLNp9s99WWk8SABL7sbOdhCop4I9ab3lrIpIBagtGulYi2jQKRpDdCj0emF0ivf8VE56wgvgX1EJHJ3uP7pyAOLpc-ws63mvNp_k9s8atng2SbiLTpkM5FobBDQ4dYUQtm3zMk1lBfem1QyhxgQ-EDOoPZa0Bmibod7SKFB1OrupuxM4HLNuFjNGLyT0qboaqsvn4dB14bxvUMFK_zq2hvPTj96Sv1V2dGOLs6vGk0jYVe5fS89TFPGPb__8d5rbi_W75r6Pc0S0b6S5NA63gjsj-64dasMf_4doLNOXwAAAAFSdMRBAA")

User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              #Removed
              workers=300
              )

User.start()
print("User Started!")

