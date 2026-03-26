import os

# ================== TELEGRAM API CONFIG ==================

API_ID = int(os.getenv("API_ID", "1234567"))
API_HASH = os.getenv("API_HASH", "YOUR_API_HASH_HERE")
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")


# ================== REDIS DATABASE CONFIG ==================

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "6379"))
PASSWORD = os.getenv("PASSWORD", None)


# ================== BOT SETTINGS ==================

PRIVATE_CHAT_ID = int(os.getenv("PRIVATE_CHAT_ID", "-1000000000000"))

ADMINS = list(
    map(int, os.getenv("ADMINS", "803003146").split(","))
)

ADMIN_ID = int(os.getenv("ADMIN_ID", "803003146"))


# ================== TERABOX API ==================

TERABOX_API_BASE = os.getenv(
    "TERABOX_API_BASE",
    "https://api.ntm.com/api/terabox"
)

TERABOX_API_TOKEN = os.getenv(
    "TERABOX_API_TOKEN",
    "NTMPASS"
)

TERABOX_API_TEMPLATE = (
    f"{TERABOX_API_BASE}?key={TERABOX_API_TOKEN}&url={{url}}"
)
