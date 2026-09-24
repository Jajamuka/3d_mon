from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router_form = Router()

class Form(StatesGroup):
    name = State()
    age = State()
    phone = State()

@router_form.message(Command('form'))
async def start_form(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer('Как вас зовут?')

@router_form.message(Form.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(Form.age)
    await message.answer('Сколько вам лет?')

@router_form.message(Form.age)
async def get_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Возраст должен быть числом.')
        return

    await state.update_data(age=message.text)

    await state.set_state(Form.phone)
    await message.answer('Введите свой номер телефона:')

@router_form.message(Form.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)

    data = await state.get_data()

    await message.answer(
        f"Анкета заполнена!\n\n"
        f"Имя: {data['name']}\n"
        f"Возраст: {data['age']}\n"
        f"Телефон: {data['phone']}"
    )

    await state.clear()

@router_form.message(Command('cancel'))
async def cancel_form(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Анкета отменена.')