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
                split_args = args.split()

                if len(split_args) == 2:
                    email, guid = split_args
                    email_match = re.match(Config.email_regular, email)
                    guid_match = re.match(Config.guid_regular, guid)

                    if not email_match:
                        await message.answer(Config.line_is_not_email)
                    elif not guid_match:
                        await message.answer(Config.line_is_not_guid)
                    else:                        
                        response = requests.post(
                            Config.student_url,
                            json={
                                "email": email,
                                "telegram": str(message.from_user.id),
                                "guid": guid,
                            },
                            headers={
                                "Authorization": f"Basic {base64.b64encode(Config.user_authorization.encode()).decode()}"
                            },
                        )
                        if response.status_code != 200:
                            if response.status_code == 401:
                                await message.answer(Config.wrong_guid)
                            else:
                                await message.answer(Config.binding_error)
                else:
                    await message.answer(Config.not_enough_arguments)
            else:
                await message.answer(Config.arguments_not_specified)

    await dispatcher.start_polling(bot)


def run() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    Config.load_config()
    asyncio.run(main())
