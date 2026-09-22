from aiogram import F, Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from decouple import config
from datetime import datetime
import asyncio
import logging
import random
from aiogram.types import Message, FSInputFile

token_bot = config("TOKEN")
#print(token_bot)

bot = Bot(token=token_bot)
dp = Dispatcher()

router_main = Router()

dp.include_router(router=router_main)

@router_main.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(text='Привет')

@router_main.message(Command('help'))
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


@router_main.message(Command('time'))
async def time_hanler(message: Message):
    current_time = datetime.now()
    await message.answer(text=f'Сейчас: {current_time}')

@router_main.message(Command('random'))
async def random_handler(message: Message):
    number = random.randint(1, 100)
    await message.answer(text=f'Твое случайное число: {number}')


jokes = ['Колобок повесился XD',
         'Русалка села на шпагат LOL',
         'Прикинь я проиграл. Прикинь чуть-чуть не хватило(',
         'Прикинь если бы у горчицы появился разум',
         'Книга братан иди-ка сюда']

@router_main.message(Command('joke'))
async def joke_handler(message: Message):
    joke = random.choice(jokes)
    await message.answer(text=joke)


@router_main.message(F.text == 'привет')
async def hello_text_handler(message: Message):
    await message.answer('hello')


memes = ['media/image1.png',
         'media/image2.png',
         'media/image3.png',
         'media/image4.png']
@router_main.message(Command('mem'))
async def mem_handler(message: Message):
    photo_mem = random.choice(memes)
    await message.answer_photo(photo=FSInputFile(photo_mem))


@router_main.message(Command('sticker'))
async def sticker_handler(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAMParJxjW6aD_yOovebOGaP3yCF1KQAAt99AAKfHMlIsl9fy9ch00Y9BA')

@router_main.message(F.sticker)
async def get_sticker_id_handler(message: Message):
    await message.answer(f'ID этого стикера - {message.sticker.file_id}')


@router_main.message(F.text)
async def echo_handler(message: Message):
    await message.answer(f'Такой команды нет - {message.text}')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))