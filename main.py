import codecs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InputFile, Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboard import *


api = '1949798555:AAEI76epvCeDOaU0UdOilg3Cz60ED8vIF9I'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kolvo_good = 0

#начальное сообщение
@dp.message_handler(commands = ['start'])
async def starter(message: types.Message):
	start_photo = InputFile("start_photo.png")
	await message.answer(f'Добро пожаловать! Предлагаю пройти тест и узнать насколько хорошо ты знаешь основы языка программирования Python')
	await bot.send_photo(chat_id=message.chat.id, photo=start_photo, reply_markup=start_menu)


#первый вопрос, проверка ответа, прибавление к переменной, переход на следующий вопрос
@dp.callback_query_handler(text_contains='go')
async def fff (callback_query: types.CallbackQuery):
	first_photo = InputFile("vopros1.png")
	await bot.send_message(callback_query.from_user.id, 'Первый вопрос. Что напечатает следующий код: ')
	await bot.send_photo(callback_query.from_user.id, photo=first_photo, reply_markup=vse_btn_1)


@dp.callback_query_handler(text_contains='1well')
async def fff (callback_query: types.CallbackQuery):
	global kolvo_good
	kolvo_good += 1
	await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
	second_pgoto = InputFile("vopros2.png")
	await bot.send_message(callback_query.from_user.id, 'Переходим ко второму вопросу, что напечатает следующий код: ')
	await bot.send_photo(callback_query.from_user.id, photo=second_pgoto, reply_markup=vse_btn_2)

@dp.callback_query_handler(text_contains='1')
async def fff (callback_query: types.CallbackQuery):
	second_pgoto = InputFile("vopros2.png")
	await bot.send_message(callback_query.from_user.id, 'Переходим ко второму вопросу, что напечатает следующий код: ')
	await bot.send_photo(callback_query.from_user.id, photo=second_pgoto, reply_markup=vse_btn_2)

@dp.callback_query_handler(text_contains='2well')
async def fff (callback_query: types.CallbackQuery):
	global kolvo_good
	kolvo_good += 1
	await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
	third_photo = InputFile("vopros3.png")
	await bot.send_message(callback_query.from_user.id, 'Переходим к третьему вопросу, что напечатает следующий код: ')
	await bot.send_photo(callback_query.from_user.id, photo=third_photo, reply_markup=vse_btn_3)

@dp.callback_query_handler(text_contains='2')
async def fff (callback_query: types.CallbackQuery):
	second_pgoto = InputFile("vopros3.png")
	await bot.send_message(callback_query.from_user.id, 'Переходим к третьему вопросу, что напечатает следующий код: ')
	await bot.send_photo(callback_query.from_user.id, photo=second_pgoto, reply_markup=vse_btn_3)

@dp.callback_query_handler(text_contains='3well')
async def fff (callback_query: types.CallbackQuery):
	global kolvo_good
	kolvo_good += 1
	await bot.answer_callback_query(callback_query.id, text='Верно!', show_alert=True)
	await bot.send_message(callback_query.from_user.id, f'Отлично, ты ответил на {kolvo_good} из 3 вопросов правильно!', reply_markup=None)
	if kolvo_good <= 2:
		await bot.send_message(callback_query.from_user.id, 'Напиши свою электронную почту и я направлю материалы, где ты можешь подтянуть свои знания! ')
	elif kolvo_good == 3:
		await bot.send_message(callback_query.from_user.id, 'Напиши свою электронную почту и я направлю материалы, где ты можешь продолжать совершенствовать свои знания! ')

@dp.callback_query_handler(text_contains='3')
async def fff (callback_query: types.CallbackQuery):
	global kolvo_good
	await bot.send_message(callback_query.from_user.id, f'Ты ответил на {kolvo_good} из 3 вопросов правильно!', reply_markup=None)
	if kolvo_good <= 2:
		await bot.send_message(callback_query.from_user.id, 'Напиши свою электронную почту и я направлю материалы, где ты можешь подтянуть свои знания! ')
	elif kolvo_good == 3:
		await bot.send_message(callback_query.from_user.id, 'Напиши свою электронную почту и я направлю материалы, где ты можешь продолжать совершенствовать свои знания! ')


@dp.message_handler()
async def starter(message: types.Message):

	msg = message['text']
	if '@gmail.com' in msg or '@yandex.ru' in msg or '@easypro.academy' in msg or '@mail.ru' in msg:
		await message.answer('Уже отправляю!\nСпасибо что прошли тест!\nХорошего Вам дня!')
		file = codecs.open('link.txt', "r", "utf_8_sig")
		text2 = file.read()
		text3 = str(text2)
		text = text3
		mssg = MIMEMultipart()
		from_email = 'komzalovtest@gmail.com'
		password = 'zhenia2009200'
		to_email = message['text']
		mssg['Subject'] = 'Программирование - наше всё!'
		message = text
		mssg.attach(MIMEText(message, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com: 587')
		server.starttls()
		server.login(from_email, password)
		server.sendmail(from_email, to_email, mssg.as_string())
		server.quit()
	else:
		await message.answer('К сожалению, я не понимаю, обратитесь к менеджеру с Вашей проблемой', reply_markup=meneger)



if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	executor.start_polling(dp)

