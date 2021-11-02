from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#кнопки стартового меню
btn_go = InlineKeyboardButton('Погнали!', callback_data='go')
btn_no = InlineKeyboardButton('Пройду в следующий раз!', callback_data='no')
start_menu = InlineKeyboardMarkup().row(btn_go).row(btn_no)

#кнопка для связи с менеджером
btn_meneger = InlineKeyboardButton('Связаться с менеджером', url='https://t.me/ekomzalov')
meneger = InlineKeyboardMarkup().row(btn_meneger)

#кнопки первого задания
btn1_vopros1 = InlineKeyboardButton('[1, 2, 3]', callback_data='1')
btn2_vopros1 = InlineKeyboardButton('[1, 2, 2]', callback_data='1well')
btn3_vopros1 = InlineKeyboardButton('[1, 2, 2, 3]', callback_data='1')
btn4_vopros1 = InlineKeyboardButton('Ошибка', callback_data='1')
vse_btn_1 = InlineKeyboardMarkup().row(btn1_vopros1).row(btn2_vopros1).row(btn3_vopros1).row(btn4_vopros1)

#кнопки второго задания
btn1_vopros2 = InlineKeyboardButton('0', callback_data='2')
btn2_vopros2 = InlineKeyboardButton('1', callback_data='2')
btn3_vopros2 = InlineKeyboardButton('Ошибка', callback_data='2well')
vse_btn_2 = InlineKeyboardMarkup().row(btn1_vopros2, btn2_vopros2).row(btn3_vopros2)

#кнопки третьего задания
btn1_vopros3 = InlineKeyboardButton('foobar', callback_data='3')
btn2_vopros3 = InlineKeyboardButton('barfoo', callback_data='3well')
btn3_vopros3 = InlineKeyboardButton('fobar', callback_data='3')
btn4_vopros3 = InlineKeyboardButton('Ошибка', callback_data='3')
vse_btn_3 = InlineKeyboardMarkup().row(btn1_vopros3, btn2_vopros3).row(btn3_vopros3, btn4_vopros3)








#Электронки
#electronki_menu = InlineKeyboardMarkup().row(*[InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(1,4)])\
#.row(*[InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(4,7)])\
#.row(*[InlineKeyboardButton(str(i), callback_data=str(i)) for i in range(7,10)])\