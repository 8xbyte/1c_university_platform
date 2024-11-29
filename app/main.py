from app.config import Config

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message

import requests
import asyncio
import logging
import base64
import sys
import re


async def main() -> None:
    bot = Bot(token=Config.bot_token)
    dispatcher = Dispatcher()

    @dispatcher.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        await message.answer(Config.start_command)

    @dispatcher.message(Command("link"))
    async def command_link_handler(message: Message, command: CommandObject) -> None:
        args = command.args

        if not message.from_user:
            await message.answer(Config.get_user_error)
        else:
            if args:
                match = re.match(Config.email_regular, args)

                if match:
                    response = requests.post(
                        Config.student_url,
                        json={"email": args, "telegram": str(message.from_user.id)},
                        headers={
                            "Authorization": f"Basic {base64.b64encode(Config.user_authorization.encode()).decode()}"
                        },
                    )
                    if response.status_code != 200:
                        await message.answer(Config.binding_error)
                else:
                    await message.answer(Config.line_is_not_email)
            else:
                await message.answer(Config.email_not_specified)

    await dispatcher.start_polling(bot)


def run() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    Config.load_config()
    asyncio.run(main())
