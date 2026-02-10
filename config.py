import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token (from environment variables)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8301752824:AAGfi3h-o3WpDv_IXQT-nNwpUEAtok26_84")

# Channel and link configuration
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL", "https://t.me/KINGBET9AUD")
FREE_SPIN_URL = os.getenv("FREE_SPIN_URL", "https://kingbet9bet.com/RFKINGBETBOT")
FREE_CREDIT_URL = os.getenv("FREE_CREDIT_URL", "https://kingbet9bet.com/RFKINGBETBOT")

# Promotional images (local file paths - hardcoded in code)
FREE_SPIN_IMAGE_PATH = "public/free_spin.jpg"
HOT_GAME_TIPS_IMAGE_PATH = "public/hot_game_tips.jpg"

# Bot information
BOT_NAME = "Kingbet9 Promo Bot"
BOT_DESCRIPTION = "Kingbet9 Marketing Assistant - Provides latest promotions and event information"
