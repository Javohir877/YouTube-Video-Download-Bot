# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.22684706, 
    api_hash=Config.99e594d26bbf56b0a6840b390e6fa0c0, 
    bot_token=Config.7953938944:AAGHVgN0aIIwHsdeERpvXOazp07w6MFhm_k,
    plugins=dict(root="Youtube")
)



# Start the bot
print("Salom men sizga Youtube uchun bemalol sizga videolarni yuklab bera olaman")
app.run()
