import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


# =========================================================
# НАСТРОЙКИ
# =========================================================

TOKEN = "8939674951:AAE8XuRnXZmRf_iEVCYViVd7oIcLyvlTalU"

OFFICIAL_SITE = "https://vkusnoitochka.ru/"
MENU_URL = "https://vkusnoitochka.ru/menu"


# =========================================================
# ТОВАРЫ
# =========================================================

PRODUCTS = {
    "big_chicken": {
        "name": "🍔 Биг Чикен Бургер",
        "price": "от 345 ₽",
        "description": (
            "Большой бургер с цельным куриным филе "
            "в хрустящей панировке, сыром, овощами, "
            "соусом и булочкой с кунжутом."
        ),
        "url": "https://vkusnoitochka.ru/menu/burgery-i-rolly"
    },

    "big_hit": {
        "name": "🍔 Биг Хит",
        "price": "от 299 ₽",
        "description": (
            "Бургер с говяжьими котлетами, сыром, "
            "маринованными огурцами, салатом, луком "
            "и фирменным соусом."
        ),
        "url": "https://vkusnoitochka.ru/menu/burgery-i-rolly"
    },

    "nuggets": {
        "name": "🍗 Наггетсы",
        "price": "от 199 ₽",
        "description": (
            "Куриные наггетсы в хрустящей панировке. "
            "Количество и стоимость зависят от выбранной порции."
        ),
        "url": "https://vkusnoitochka.ru/menu"
    },

    "fries": {
        "name": "🍟 Картофель фри",
        "price": "от 99 ₽",
        "description": (
            "Классический картофель фри — хрустящий "
            "снаружи и мягкий внутри."
        ),
        "url": "https://vkusnoitochka.ru/menu"
    },

    "float": {
        "name": "🥤 Флоат апельсиновый",
        "price": "от 183 ₽",
        "description": (
            "Освежающий апельсиновый напиток с "
            "мороженым."
        ),
        "url": "https://vkusnoitochka.ru/menu"
    },

    "ice_deluxe": {
        "name": "🍦 Айс Де Люкс",
        "price": "от 179 ₽",
        "description": (
            "Нежный десерт с мороженым и добавками."
        ),
        "url": "https://vkusnoitochka.ru/menu"
    },

    "set_chicken": {
        "name": "🎁 Сет с Чикенбургером",
        "price": "от 264 ₽",
        "description": (
            "Готовый сет с Чикенбургером. "
            "Состав и стоимость могут зависеть от региона."
        ),
        "url": "https://vkusnoitochka.ru/menu/sety-i-pary_1/"
    },
}


# =========================================================
# КЛАВИАТУРЫ
# =========================================================

def main_menu():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🍔 Меню",
        callback_data="menu"
    )

    builder.button(
        text="🚗 Заказать",
        url=OFFICIAL_SITE
    )

    builder.button(
        text="ℹ️ О компании",
        callback_data="about"
    )

    builder.button(
        text="🌐 Официальный сайт",
        url=OFFICIAL_SITE
    )

    builder.adjust(2, 2)

    return builder.as_markup()


def menu_categories():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🍔 Бургеры",
        callback_data="burgers"
    )

    builder.button(
        text="🍟 Картофель и снеки",
        callback_data="snacks"
    )

    builder.button(
        text="🥤 Напитки",
        callback_data="drinks"
    )

    builder.button(
        text="🍦 Десерты",
        callback_data="desserts"
    )

    builder.button(
        text="🎁 Комбо и сеты",
        callback_data="sets"
    )

    builder.button(
        text="🔙 Назад",
        callback_data="back_main"
    )

    builder.adjust(2, 2, 1, 1)

    return builder.as_markup()


def burgers_menu():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🍔 Биг Чикен Бургер",
        callback_data="product_big_chicken"
    )

    builder.button(
        text="🍔 Биг Хит",
        callback_data="product_big_hit"
    )

    builder.button(
        text="🔙 Назад",
        callback_data="menu"
    )

    builder.adjust(1)

    return builder.as_markup()


def snacks_menu():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🍗 Наггетсы",
        callback_data="product_nuggets"
    )

    builder.button(
        text="🍟 Картофель фри",
        callback_data="product_fries"
    )

    builder.button(
        text="🔙 Назад",
        callback_data="menu"
    )

    builder.adjust(1)

    return builder.as_markup()


def drinks_menu():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🥤 Флоат апельсиновый",
        callback_data="product_float"
    )

    builder.button(
        text="🔙 Назад",
        callback_data="menu"
    )

    builder.adjust(1)

    return builder.as_markup()


def desserts_menu():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🍦 Айс Де Люкс",
        callback_data="product_ice_deluxe"
    )

    builder.button(
        text="🔙 Назад",
        callback_data="menu"
    )

    builder.adjust(1)

    return builder.as_markup()


def sets_menu():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🎁 Сет с Чикенбургером",
        callback_data="product_set_chicken"
    )

    builder.button(
        text="🔙 Назад",
        callback_data="menu"
    )

    builder.adjust(1)

    return builder.as_markup()


def product_keyboard(product_id):
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🛒 Заказать на сайте",
        url=PRODUCTS[product_id]["url"]
    )

    builder.button(
        text="🔙 К меню",
        callback_data="menu"
    )

    builder.adjust(1)

    return builder.as_markup()


# =========================================================
# BOT / DISPATCHER
# =========================================================

bot = Bot(token=TOKEN)
dp = Dispatcher()


# =========================================================
# /START
# =========================================================

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🍔 <b>Вкусно — и точка</b>\n\n"
        "Добро пожаловать в демонстрационный Telegram-бот!\n\n"
        "Здесь можно посмотреть категории меню, "
        "информацию о блюдах и перейти на официальный "
        "сайт для заказа.\n\n"
        "⚠️ Это демонстрационный проект. "
        "Бот не является официальным ботом сети.",
        reply_markup=main_menu()
    )


# =========================================================
# ГЛАВНОЕ МЕНЮ
# =========================================================

@dp.callback_query(F.data == "back_main")
async def back_main(callback: CallbackQuery):
    await callback.message.edit_text(
        "🍔 <b>Вкусно — и точка</b>\n\n"
        "Выберите нужный раздел:",
        reply_markup=main_menu()
    )

    await callback.answer()


# =========================================================
# КАТЕГОРИИ
# =========================================================

@dp.callback_query(F.data == "menu")
async def menu_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🍔 <b>Меню</b>\n\n"
        "Выберите категорию:",
        reply_markup=menu_categories()
    )

    await callback.answer()


@dp.callback_query(F.data == "burgers")
async def burgers_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🍔 <b>Бургеры</b>\n\n"
        "Выберите блюдо:",
        reply_markup=burgers_menu()
    )

    await callback.answer()


@dp.callback_query(F.data == "snacks")
async def snacks_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🍟 <b>Картофель и снеки</b>\n\n"
        "Выберите блюдо:",
        reply_markup=snacks_menu()
    )

    await callback.answer()


@dp.callback_query(F.data == "drinks")
async def drinks_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🥤 <b>Напитки</b>\n\n"
        "Выберите напиток:",
        reply_markup=drinks_menu()
    )

    await callback.answer()


@dp.callback_query(F.data == "desserts")
async def desserts_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🍦 <b>Десерты</b>\n\n"
        "Выберите десерт:",
        reply_markup=desserts_menu()
    )

    await callback.answer()


@dp.callback_query(F.data == "sets")
async def sets_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎁 <b>Комбо и сеты</b>\n\n"
        "Выберите набор:",
        reply_markup=sets_menu()
    )

    await callback.answer()


# =========================================================
# ТОВАРЫ
# =========================================================

async def show_product(
    callback: CallbackQuery,
    product_id: str
):
    product = PRODUCTS[product_id]

    text = (
        f"<b>{product['name']}</b>\n\n"
        f"{product['description']}\n\n"
        f"💰 <b>Цена: {product['price']}</b>\n\n"
        "ℹ️ Цена и наличие могут отличаться "
        "в зависимости от региона."
    )

    await callback.message.edit_text(
        text,
        reply_markup=product_keyboard(product_id)
    )

    await callback.answer()


@dp.callback_query(F.data == "product_big_chicken")
async def product_big_chicken(callback: CallbackQuery):
    await show_product(callback, "big_chicken")


@dp.callback_query(F.data == "product_big_hit")
async def product_big_hit(callback: CallbackQuery):
    await show_product(callback, "big_hit")


@dp.callback_query(F.data == "product_nuggets")
async def product_nuggets(callback: CallbackQuery):
    await show_product(callback, "nuggets")


@dp.callback_query(F.data == "product_fries")
async def product_fries(callback: CallbackQuery):
    await show_product(callback, "fries")


@dp.callback_query(F.data == "product_float")
async def product_float(callback: CallbackQuery):
    await show_product(callback, "float")


@dp.callback_query(F.data == "product_ice_deluxe")
async def product_ice_deluxe(callback: CallbackQuery):
    await show_product(callback, "ice_deluxe")


@dp.callback_query(F.data == "product_set_chicken")
async def product_set_chicken(callback: CallbackQuery):
    await show_product(callback, "set_chicken")


# =========================================================
# О КОМПАНИИ
# =========================================================

@dp.callback_query(F.data == "about")
async def about_handler(callback: CallbackQuery):
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🌐 Официальный сайт",
        url=OFFICIAL_SITE
    )

    builder.button(
        text="🔙 Назад",
        callback_data="back_main"
    )

    builder.adjust(1)

    await callback.message.edit_text(
        "ℹ️ <b>О компании</b>\n\n"
        "«Вкусно — и точка» — сеть ресторанов "
        "быстрого обслуживания в России.\n\n"
        "На официальном сайте доступны меню, "
        "информация о продуктах, ресторанах "
        "и сервисах сети.\n\n"
        "⚠️ <b>Важно:</b>\n"
        "Этот Telegram-бот является "
        "демонстрационным учебным проектом "
        "и не является официальным ботом "
        "«Вкусно — и точка».",
        reply_markup=builder.as_markup()
    )

    await callback.answer()


# =========================================================
# ЗАПУСК
# =========================================================

async def main():
    print("🍔 Бот «Вкусно — и точка» запущен!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
