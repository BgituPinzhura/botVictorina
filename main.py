from aiogram import Bot, Dispatcher
import asyncio
import Dialogs
from Config import config


async def main():
    dp = Dispatcher()
    dp.include_router(Dialogs.router)
    bot = Bot(config.bot_token.get_secret_value())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
