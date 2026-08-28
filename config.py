"""
Конфигурация NFT Scanner V8.
"""
import os

# ── Telegram ──────────────────────────────────
BOT_TOKEN = os.getenv("BOT_TOKEN", "8777973273:AAHRSyw2ankQNe6wG-fuSFD_RXOkFbIkcaU")
BOT_USERNAME = os.getenv("BOT_USERNAME", "twstseffds_bot")
ADMIN_IDS = [8203437780, 8332982896, 8666132224]
TELEGRAM_API_SERVER = os.getenv("TELEGRAM_API_SERVER", "")

# ── Mini App ──────────────────────────────────
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://ваш-сайт.github.io/")

# ── Обязательная подписка ─────────────────────
REQUIRED_CHANNEL_ID = -1004335386589
REQUIRED_CHANNEL_LINK = "https://t.me/AccountAureum"

# ── БД ────────────────────────────────────────
DB_PATH = os.getenv("DB_PATH", "/data/nft_cache.db")

# ── Скан ──────────────────────────────────────
MAX_CONCURRENT_REQUESTS = 150
REQUEST_TIMEOUT = 5
DELAY_BETWEEN_BATCHES = 0
PROGRESS_UPDATE_INTERVAL = 2  # секунд

# ── Рандомный парсинг ─────────────────────────
RANDOM_COLLECTIONS_COUNT = 5
RANDOM_ITEMS_PER_COLLECTION = 100

# ── Пагинация ────────────────────────────────
GIFTS_PER_PAGE = 8
MODELS_PER_PAGE = 10
BACKDROPS_PER_PAGE = 10
RESULTS_PER_PAGE = 10        # юзеров на страницу (компактно, влезает в TG)
TOTAL_RESULTS = 200          # макс. результатов за скан

# ── Фильтры NFT ──────────────────────────────
#  код: (min, max, label)
NFT_COUNT_RANGES = {
    "1-3":  (1, 3,   "1–3 NFT"),
    "4-10": (4, 10,  "4–10 NFT"),
    "10+":  (10, 999999, "10+ NFT"),
    "any":  (0, 999999, "Любое кол-во"),
}
DEFAULT_NFT_RANGE = "any"
MAX_NFT_HARD_CAP = 999999

# ── Экспорт ──────────────────────────────────
CSV_DIR = os.getenv("CSV_DIR", "/data/exports")
