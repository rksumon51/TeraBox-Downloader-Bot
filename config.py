import os

# TELEGRAM
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ADMINS
ADMINS = list(map(int, os.getenv("ADMINS").split(",")))

# TERABOX (xAPIverse)
TERABOX_API_KEY = os.getenv("TERABOX_API_KEY")
