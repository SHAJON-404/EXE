import os
import logging
from typing import cast

from dotenv import load_dotenv
from telegram import Update, Message, MessageEntity
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

# ── env ──────────────────────────────────────────────────────────────────────
load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ── logging ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.WARNING,
)
logger = logging.getLogger(__name__)


# ── handlers ──────────────────────────────────────────────────────────────────

async def handle_custom_emoji(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Extract and return the custom emoji ID."""
    msg = cast(Message, update.message)  # non-None guaranteed by MessageHandler

    if not msg.entities:
        return

    custom_emoji_ids = []
    for entity in msg.entities:
        if entity.type == MessageEntity.CUSTOM_EMOJI and entity.custom_emoji_id:
            if entity.custom_emoji_id not in custom_emoji_ids:
                custom_emoji_ids.append(entity.custom_emoji_id)

    if not custom_emoji_ids:
        await msg.reply_text("⚠️ No custom emoji found.")
        return

    # Prepare response: Custom Emoji ID : `12345`
    # Prepare response: using HTML for custom emoji injection
    response_lines = []
    for emoji_id in custom_emoji_ids:
        response_lines.append(
            f'<tg-emoji emoji-id="6260268593196310225">✨</tg-emoji> <b>Custom Emoji ID :</b> <code>{emoji_id}</code>'
        )

    await msg.reply_text(
        "\n".join(response_lines),
        parse_mode="HTML",
    )


async def handle_other(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Reject anything that is not a custom emoji."""
    msg = cast(Message, update.message)  # non-None guaranteed by MessageHandler
    await msg.reply_text(
        "⚠️ Please send a custom emoji.",
    )


# ── entry-point ───────────────────────────────────────────────────────────────

def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not set in .env")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # custom-emoji text filter
    emoji_filter = filters.TEXT & filters.Entity(MessageEntity.CUSTOM_EMOJI)

    app.add_handler(MessageHandler(emoji_filter, handle_custom_emoji))

    # catch-all: everything else gets rejected
    app.add_handler(MessageHandler(filters.ALL, handle_other))

    print("Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
