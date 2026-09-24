


from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from config import bot
from datetime import datetime
import asyncio
import logging
import random

ruoter_commands = Router()

@ruoter_commands.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(text=f'Привет, твой id {message.from_user.id}')

@ruoter_commands.message(Command('help'))
async def help_handler(message: Message):
    await bot.send_message(chat_id=message.chat.id, text='Это первый бот Айжамал!\n'
                                                        'Выберите команду:\n'
                                                        '/start - запустить бота\n'
                                                        '/help - список команд\n'
                                                        '/time - текущая дата и время\n'
                                                        '/random - случайное число от 1 до 20\n'
                                                        '/joke - случайная шутка\n'
                                                        '/mem - случайный мем\n'
                                                        '/sticker - случайный стикер (мне стало лень, стикер один)')


@ruoter_commands.message(Command('time'))
async def time_hanler(message: Message):
    current_time = datetime.now()
    await message.answer(text=f'Сейчас: {current_time}')

@ruoter_commands.message(Command('random'))
async def random_handler(message: Message):
    number = random.randint(1, 100)
    await message.answer(text=f'Твое случайное число: {number}')


jokes = ['Колобок повесился XD',
         'Русалка села на шпагат LOL',
         'Прикинь я проиграл. Прикинь чуть-чуть не хватило(',
         'Прикинь если бы у горчицы появился разум',
         'Книга братан иди-ка сюда']

@ruoter_commands.message(Command('joke'))
async def joke_handler(message: Message):
    joke = random.choice(jokes)
    await message.answer(text=joke)


@ruoter_commands.message(F.text == 'привет')
async def hello_text_handler(message: Message):
    await message.answer('hello')


memes = ['media/image1.png',
         'media/image2.png',
         'media/image3.png',
         'media/image4.png']
@ruoter_commands.message(Command('mem'))
async def mem_handler(message: Message):
    photo_mem = random.choice(memes)
    await message.answer_photo(photo=FSInputFile(photo_mem))


@ruoter_commands.message(Command('sticker'))
async def sticker_handler(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAMParJxjW6aD_yOovebOGaP3yCF1KQAAt99AAKfHMlIsl9fy9ch00Y9BA')

