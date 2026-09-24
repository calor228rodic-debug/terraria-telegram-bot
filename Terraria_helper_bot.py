import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


# Главное меню
main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📖 Terraria Wiki",
                url="https://terraria.wiki.gg/"
            )
        ],
        [
            InlineKeyboardButton(
                text="🧩 Моды",
                url="https://steamcommunity.com/app/1281930/workshop/"
            )
        ],
        [
            InlineKeyboardButton(
                text="💬 Reddit",
                url="https://www.reddit.com/r/Terraria/"
            )
        ],
        [
            InlineKeyboardButton(
                text="ℹ️ О боте",
                callback_data="about"
            )
        ]
    ]
)


# Кнопка "Назад"
back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Назад",
                callback_data="back"
            )
        ]
    ]
)


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🎮 <b>Terraria Hub</b>\n\n"
        "Добро пожаловать!\n"
        "Здесь собраны полезные ресурсы по Terraria.\n\n"
        "Выбери нужный раздел:",
        reply_markup=main_keyboard
    )


@dp.callback_query(lambda callback: callback.data == "about")
async def about_handler(callback):
    await callback.message.edit_text(
        "ℹ️ <b>О боте</b>\n\n"
        "Terraria Hub — небольшой Telegram-бот "
        "с полезными ссылками по Terraria.\n\n"
        "🤖 Создан на Python + aiogram.",
        reply_markup=back_keyboard
    )

    await callback.answer()


@dp.callback_query(lambda callback: callback.data == "back")
async def back_handler(callback):
    await callback.message.edit_text(
        "🎮 <b>Terraria Hub</b>\n\n"
        "Выбери нужный раздел:",
        reply_markup=main_keyboard
    )

    await callback.answer()


async def main():
    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())