import logging
import time
from telegram import Update,  ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

custom_keyboard1 = [['Узнать больше 🌳'],
                    ['Играть дальше 🌳']]

custom_keyboard2 = [['Узнать больше 📸'],
                    ['Играть дальше 📸']]

custom_keyboard2question = [['Криминалистом', 'Фотографом',],
                            ['Химиком', 'Музыкантом']]

# Настроить ведение журнала
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Определить функции для обработки команды «/start»
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Приветствую вас! Я тестовый бот, созданный для квеста по Белграду. Начнем? Напишите /startkvest чтобы начать квест.')

# Определить функции для обработки команды «/startkvest»
async def startkvest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='*Платан*', parse_mode='MarkdownV2')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://file.notion.so/f/f/68dec92b-935e-4624-927a-e64dd1c00acb/cb2eca8b-55f8-4e9b-b8ad-1581136a819f/%D0%9F%D0%BB%D0%B0%D1%82%D0%B0%D0%BD.png?id=6539290e-2bd3-44f5-8e75-020a2622e90c&table=block&spaceId=68dec92b-935e-4624-927a-e64dd1c00acb&expirationTimestamp=1710446400000&signature=Vu3MuHqCoGNh8DGOcQBE80S-V0yvmCJeLb229oDknhk&downloadName=%D0%9F%D0%BB%D0%B0%D1%82%D0%B0%D0%BD.png')
    time.sleep(1)
    reply_markup = ReplyKeyboardMarkup(custom_keyboard1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Хотите узнать об этом месте больше?', reply_markup=reply_markup)

# Определить функции для обработки команд «/message_handle»
async def message_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Платан 🌳
    if update.message.text == 'Узнать больше 🌳':
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Перед Вами один из самых крупных и красивых платанов в Европе. А ещё он очень старый. Ранее считалось, что дерево было посажено одновременно со строительством усадьбы Милоша Обреновича, то есть где-то в 1830-х годах. Но инженер-лесотехник Светислав Владисавлевич нашел в архивах информацию, что дерево было привезено из Вены и посажено в парке только в 1866 году. Так или иначе, но уже в 1881 году у платана появилась первая подпорка. Благодаря этому своевременному решению ветви смогли раскинуться настолько широко. Самая большая ветвь имеет длину около 20 метров, размах кроны – более 50 метров, а площадь создаваемой деревом тени – почти 2000 м². Платан быстро растёт, легко переносит грязный городской воздух и не сильно страдает даже в самые суровые зимы.')
    elif update.message.text == 'Играть дальше 🌳':
        reply_markup=ReplyKeyboardRemove()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Какое количество металлических вертикальных опор поддерживают платан?', reply_markup=reply_markup)
    elif update.message.text == '17':
        reply_markup=ReplyKeyboardRemove()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Верно! Двигаемся дальше!', reply_markup=reply_markup)
        time.sleep(1)
        # Памятник Рудольфу Арчибальду Рейссу 📸
        await context.bot.send_message(chat_id=update.effective_chat.id, text='*Памятник Рудольфу Арчибальду Рейссу*', parse_mode='MarkdownV2')
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://file.notion.so/f/f/68dec92b-935e-4624-927a-e64dd1c00acb/066f6c33-b0ec-4e5f-91fc-8397201a8b1d/%D0%9F%D0%B0%D0%BC%D1%8F%D1%82%D0%BD%D0%B8%D0%BA_%D0%A0%D0%B5%D0%B9%D1%81%D1%83.png?id=062add3c-b0d6-4196-8a8b-4d90e9c66a85&table=block&spaceId=68dec92b-935e-4624-927a-e64dd1c00acb&expirationTimestamp=1710446400000&signature=5rNp8evhqNXjysBmVMNLNY0MHGled9qvGG1x_hJYVkg&downloadName=%D0%9F%D0%B0%D0%BC%D1%8F%D1%82%D0%BD%D0%B8%D0%BA+%D0%A0%D0%B5%D0%B9%D1%81%D1%83.png')
        time.sleep(1)
        reply_markup = ReplyKeyboardMarkup(custom_keyboard2)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Хотите узнать об этом месте больше?', reply_markup=reply_markup)
    elif update.message.text == 'Узнать больше 📸':
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Рудольф Арчибальд Рейсс - немецкий и швейцарский криминалист, судебный эксперт, педагог, профессор, доктор химии, фотограф. Один из основоположников криминалистики. Внёс значительный вклад в совершенствование системы словесного портрета (освидетельствование и идентификацию личности). В 1902 впервые в университете ввёл курс лекций «Судебная фотография». С 1906 — стал профессором криминалистики Лозаннского университета, в котором возглавил уголовное отделение на юридическом факультете. В 1908 создал при Лозаннском университете Институт криминалистики, который существует и по сей день. В связи с этим университет начал готовить дипломированных криминалистов. В Институте проходили стажировку криминалисты из Российской империи, Румынии, Сербии, Греции, Люксембурга и Бразилии. Во время Первой мировой войны, в 1914—1915 по приглашению правительства Сербии занимался расследованием преступлений австро-венгерской, немецкой и болгарской армии по отношению к мирным жителям. Через швейцарскую прессу сообщил миру о военных преступлениях, совершенных в Сербии. В 1915 году вступил в сербскую армию, сопровождал её во время отступления через Албанию, вернулся с ней, последние дни войны провел в Белграде. Был известен как большой друг Сербии и сербского народа, после окончания войны жил в Сербии.')
    elif update.message.text == 'Играть дальше 📸':
        reply_markup = ReplyKeyboardMarkup(custom_keyboard2question)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Кем не был Рудольф Арчибальд Рейссу?', reply_markup=reply_markup)
    elif update.message.text == 'Музыкантом':
        reply_markup=ReplyKeyboardRemove()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Верно! Двигаемся дальше!', reply_markup=reply_markup)
        time.sleep(1)
        # Плакучая ива
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Что ищем')
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://file.notion.so/f/f/68dec92b-935e-4624-927a-e64dd1c00acb/d0c2f239-c0db-49d6-aead-7ef5f18e57b8/%D0%9F%D0%BB%D0%B0%D0%BA%D1%83%D1%87%D0%B0%D1%8F_%D0%B8%D0%B2%D0%B01.png?id=f8696633-3511-400c-829c-669dd9851240&table=block&spaceId=68dec92b-935e-4624-927a-e64dd1c00acb&expirationTimestamp=1710446400000&signature=emhfSaSnbCKV3xsIJdsVahZY41Q3Ik-PpvdBG0Fuo7U&downloadName=%D0%9F%D0%BB%D0%B0%D0%BA%D1%83%D1%87%D0%B0%D1%8F+%D0%B8%D0%B2%D0%B01.png')
        time.sleep(1)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Где ищем')
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://file.notion.so/f/f/68dec92b-935e-4624-927a-e64dd1c00acb/500f775c-c856-4e1c-bd48-2156c0499d6d/%D0%9F%D0%BB%D0%B0%D0%BA%D1%83%D1%87%D0%B0%D1%8F_%D0%B8%D0%B2%D0%B02.png?id=a494178b-945f-4990-89e8-8cd2fc860787&table=block&spaceId=68dec92b-935e-4624-927a-e64dd1c00acb&expirationTimestamp=1710446400000&signature=WYVzh6HzhWapC6aVXHByd8HUtKwU3bXqjhb8qQiafJw&downloadName=%D0%9F%D0%BB%D0%B0%D0%BA%D1%83%D1%87%D0%B0%D1%8F+%D0%B8%D0%B2%D0%B02.png')
        time.sleep(1)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='||*Плакучая ива*||', parse_mode='MarkdownV2')
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Для изготовления какого лекарства в 1899 году был использован ингредиент коры ивы? В ответе напишите слово с большой буквы.')
    elif update.message.text == 'Аспирин':
        reply_markup=ReplyKeyboardRemove()
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Верно! Двигаемся дальше!', reply_markup=reply_markup)
        time.sleep(1)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Неправильно! Попробуйте еще раз!')

# Определить функции для обработки команды «/help»
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Чем могу помочь?')

# Определить функции для обработки неизвестных команд
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Извините, я вас не понимаю. Напишите /help чтобы открыть меню комманд.')

if __name__ == '__main__':

    # Настроить Telegram-бот
    application = ApplicationBuilder().token('6417479179:AAFvwk4PeiTKAFJPLd6Sszx6BGy6eZYp_pE').build()
    
    # Добавить обработчик команды «/start»
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Добавить обработчик команды «/startkvest»
    startkvest_handler = CommandHandler('startkvest', startkvest)
    application.add_handler(startkvest_handler)

    # Добавить обработчик команды «/help»
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    # Добавить обработчик текстовых сообщений «/message_handle»
    application.add_handler(MessageHandler(filters.TEXT, message_handle))

    # Добавить неизвестный обработчик команд
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    # Запустить робота и ждать прихода сообщения
    application.run_polling()
