import time
import logging
import asyncio
from aiogram import Bot, Dispatcher, types, executor


token = '5706561932:AAFIw7hXoGsY5kgV8CIVOaS2V2m3ye2edmY'
bot = Bot(token=token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
    user_name = message.from_user.first_name
    logging.info(f'{user_name}{time.asctime()}')
    await message.reply(f'Приветствую тебя {user_name}!!! Этот бот возвращает текст, который вы напишете')

@dp.message_handler()
async def user_echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp)
