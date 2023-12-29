import asyncio

from aiogram import types, Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from redirector import manager
from redirector.manager import TELEGRAM

bot = Bot(token=manager.settings[TELEGRAM])
dp = Dispatcher(bot)

markup = InlineKeyboardMarkup()
for row in manager.settings[manager.ECHO_BUTTONS]:
    buttons = []
    for button in row:
        buttons.append(
            InlineKeyboardButton(
                text=button['text'],
                url=button['url']
            )
        )
    markup.row(*buttons)


@dp.message_handler()
async def on_message(message: types.Message):
    await message.reply(
        text=(
            manager.settings[manager.ECHO_TEXT]
            .replace('${user}', message.from_user.full_name)
        ),
        parse_mode=types.ParseMode.MARKDOWN,
        disable_web_page_preview=True,
        reply_markup=markup
    )


def entrypoint():
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())
    loop.run_forever()


if __name__ == '__main__':
    entrypoint()
