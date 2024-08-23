from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
import random

greetings = ['Hi','Hello','hi',"hello","Привіт",'привіт','пр','здоров','Ку','ку','Пр','Здоров']
Answers = ['Hello! How are you?','Hello! What we gonna do today?',"Привіт! Як справи?","Привіт!",'Здоров!']
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello {message.from_user.full_name} and have a nice day")

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("I`m a simple bot that can greet you. Just type /start to start")

@router.message(F.photo)
async def get_photo(message:Message):
    await message.reply('This is photo but i need some text to help you')

@router.message(F.text == "Hello")
async def answer_hello(message: Message):
    await message.answer("Hello! How are you?")

@router.message(F.text.in_(greetings))
async def answer_hello(message: Message):
    await message.answer(Answers[random.randint(0,4)])