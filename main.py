import telebot, os, random
import Config_repos as Config
import BenCam, best_mat_ever_py, replacer


iter = {} #{user_id: int}
iterdroch = {}
bot = telebot.TeleBot(os.environ['totoken'])



@bot.message_handler(commands=["help"])
def helpi(message):
    print('help_touch')
    bot.send_message(message.chat.id, """Я бот МясКомаТяжМетов, я страдаю фигней вместе с вами, анимэ! Напиши в чате 'мем', 'гифка', 'войс', 'видео', 'стикер' и я отправлю свои любимые баяны-бабуяны! """)
    bot.send_sticker(message.chat.id, sticker ='CAACAgIAAxkBAAMLYwcjml7zSywTGjFVnScDPmvIzF4AAgwMAALCxIhL8kRAz39V6sspBA')

@bot.message_handler(commands=["benedictus"])
def benedict(message):
  print('bencam')
  bot.send_message(message.chat.id, text= f'Тебя зовут {random.choice(BenCam.first_name)} {random.choice(BenCam.last_name)}', reply_to_message_id=message.id)

@bot.message_handler(commands=["sayID"])
def say_id(message):
    print('sayid')
    bot.send_message(message.chat.id, text= f'ID этого сообщения - {message.id}', reply_to_message_id=message.id)

@bot.message_handler(commands=["dubina"])
def dubina(message):
    print('dub')
    dubper = random.randint(0,101)
    mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
    if message.chat.id%228 ==0:
      bot.send_message(message.chat.id, text = f'ОГО! {mention}, твоя дубина переговоров размером в 100500 cм! Смотри, не ушиби кого-нибудь в чатике!', parse_mode="HTML")
      bot.send_sticker(message.chat.id, sticker='CAACAgUAAxkBAAIQU2UcPVW8t-aMRnbLyUY-AoxB00BJAAJ2CwACmkIpVSYW5BdJY7soMAQ',disable_notification=True)
    elif dubper <= 30:
      if dubper == 0:
        bot.pin_chat_message(message.chat.id, message_id=message.id+1, disable_notification=True)
      bot.send_message(message.chat.id, text = f'Хе-хе. {mention}, твоя дубина переговоров размером всего {dubper} cм! Подрасти бы ей...', parse_mode="HTML")
      bot.send_sticker(message.chat.id, sticker='CAACAgQAAxkBAAII22NcRzpzxAmI9lQs9RR3G0R6Yy2YAAK9CgACASN4UIi-jzd7gB9_KgQ',disable_notification=True)
    elif dubper >30 and dubper <=70:
      bot.send_message(message.chat.id, text = f'Опачки! {mention}, твоя дубина переговоров размером в {dubper} cм! Самое время заняться продуктивностью! ', parse_mode="HTML")
      bot.send_sticker(message.chat.id, sticker='CAACAgQAAxkBAAII2mNcRzoVNu1cULJQHxknuHOFrhuEAAK8CQACNlF4UGLVMngNFC6CKgQ',disable_notification=True)
    elif dubper >70 and dubper <100:
      bot.send_message(message.chat.id, text = f'ОГО! {mention}, твоя дубина переговоров размером в {dubper} cм! Смотри, не ушиби кого-нибудь в чатике!', parse_mode="HTML")
      bot.send_sticker(message.chat.id, sticker='CAACAgQAAxkBAAII2WNcRzkMhCa0H2r82YSCHf1eMVOTAALtBwACoOl4UG-wtSe6nlLSKgQ',disable_notification=True)
    elif dubper == 100:
      bot.send_message(message.chat.id, text = f'ВОТ ЭТО ДА! Никогда такого не было и вот опять {mention} выкинул дубину переговоров размером в {dubper} cм! Я бы не стал спорить с обладателем такой дубины', parse_mode="HTML")
      bot.send_sticker(message.chat.id, sticker='CAACAgUAAxkBAAIN62PQ50MeLsqbol-QurdOpbCMzN6RAAKBBgAC-DgoVp3lbgvtlJY6LQQ', disable_notification=True)
      bot.pin_chat_message(message.chat.id, message_id=message.id+1, disable_notification=True)

@bot.message_handler(commands=["textfrombot"])
def Text(message):
  print('textfrombot')
  if message.chat.type == 'private':
      meseg=bot.send_message(message.chat.id,'Что ты хочешь написать в сообщении?')
      bot.register_next_step_handler(meseg, Mytext)

def Mytext(message):
  bot.send_message(int(os.environ['genshin_chat']),text = f'{message.text}' )

@bot.message_handler(commands=["pinfrombot"])
def Text_to_pin(message):
  print('pinfrombot')
  if message.chat.type == 'private':
      meseg=bot.send_message(message.chat.id,'Что ты хочешь написать в сообщении?')
      bot.register_next_step_handler(meseg, Mytext_to_pin)

def Mytext_to_pin(message):
  bot.send_message(int(os.environ['genshin_chat']),text = f'{message.text}')
    #bot.pin_chat_message(message.chat.id, message_id=message.id, disable_notification=True)

@bot.message_handler(content_types=["text"])
def trigger_text(message):
    if message.text.casefold() == 'мем':
      print('mem')
      bot.send_photo(message.chat.id, photo = random.choice(Config.photolist), reply_to_message_id=message.id, disable_notification=True)
    elif message.text.casefold() == 'гифка':
      bot.send_animation(message.chat.id, animation = random.choice(Config.giflist), reply_to_message_id=message.id, disable_notification=True)
      print('gif')
    elif message.text.casefold() == 'стикер':
      bot.send_sticker(message.chat.id, sticker=random.choice(Config.stickerlist), reply_to_message_id=message.id, disable_notification=True)
      print('sticker')
    elif message.text.casefold() == 'видео':
      bot.send_video(message.chat.id, video= random.choice(Config.videolist), reply_to_message_id=message.id, disable_notification=True)
      print('video')
    elif message.text.casefold() == 'войс':
      if message.id%7 == 5:
        bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAIMV2OJzpVAVAP65NqHURqMNg0LzE5eAALhDQACwhD4SBWdPCADM4csKwQ', reply_to_message_id=message.id, disable_notification=True)
      else:
        bot.send_voice(message.chat.id, voice= random.choice(Config.voicelist), reply_to_message_id=message.id, disable_notification=True)
      print('voice')
    elif 'кек' in message.text.casefold():
      if message.id%3==0:
        bot.send_sticker(message.chat.id, sticker=random.choice(Config.keklist), reply_to_message_id=message.id, disable_notification=True)
      else:
        bot.send_message(message.chat.id, 'Лол', reply_to_message_id=message.id, disable_notification=True)
      print('kek')
    elif 'срач' in message.text.casefold():
      bot.send_sticker(message.chat.id, sticker='CAACAgEAAxkBAANLYw8RmuS6uzd2oQIj3AGvCr0FoJEAApsAA6fegQABQCWEmcdK9F4pBA', reply_to_message_id=message.id)
      print('srach')
    elif message.text.casefold() == 'пчел ты':
      bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAM4Yw23OBpsVo0m8wETFmsDHFQdeS0AAmUeAAITnCBK_n6-hmq8D3IpBA', reply_to_message_id=message.id)
      print('pchelty')
    elif message.text.casefold() == 'опрос':
      print('poll')
      bot.send_poll(message.chat.id, question = 'Какой ты сегодня?', options=random.sample(Config.options_list,5 ), is_anonymous=False, allows_multiple_answers=True, reply_to_message_id=message.id, disable_notification=True)
    elif message.text.casefold() == 'пизда':
      print('pizd')
      bot.send_message(message.chat.id, 'Джигурда', reply_to_message_id=message.id)
    elif 'красивое' in message.text.casefold():
      print('kras')
      bot.send_photo(message.chat.id, photo = 'https://texterra.ru/upload/img/02-08-2021/2/1.jpg', reply_to_message_id=message.id, disable_notification=True)
    elif message.text.casefold() == 'шакал' or message.text.casefold() == 'саня-шакал':
      print('jackal')
      bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAPOY0gRToknARfClSJ4qM9ZVdvKinsAArofAAKlGzlJlW-u-gtutWQqBA', reply_to_message_id=message.id, disable_notification=True)
    elif message.text.casefold() == 'пошел нахуй':
      print('posil')
      bot.send_message(message.chat.id, 'Сам пошел!', reply_to_message_id=message.id)
      bot.send_sticker(message.chat.id, sticker=random.choice(Config.bad_list), disable_notification=True)
    elif message.text.casefold() == 'шутки сайно':
      print('shutki')
      bot.send_photo(message.chat.id, photo=random.choice(Config.cyno_jokes_list), reply_to_message_id=message.id)
    elif 'Моя' in message.text or 'Мое' in message.text or 'Мой' in message.text or 'Мои' in message.text:
      if 'Моя' in message.text:
        bot.send_photo(message.chat.id, photo = Config.moe_dict['моя'], reply_to_message_id=message.id)
      if 'Мое' in message.text:
        bot.send_photo(message.chat.id, photo = Config.moe_dict['мое'], reply_to_message_id=message.id)     
      if 'Мой' in message.text:
        bot.send_photo(message.chat.id, photo = Config.moe_dict['мой'], reply_to_message_id=message.id)
      if 'Мои' in message.text:
        bot.send_photo(message.chat.id, photo = Config.moe_dict['мои'], reply_to_message_id=message.id)
      print('moe')
    elif message.text.casefold() == 'ф' or message.text.casefold() == 'f':
      bot.send_photo(message.chat.id, photo = random.choice(Config.flist), reply_to_message_id=message.id, disable_notification=True)
      print('f')
    elif message.chat.id == int(os.environ['genshin_chat']) and message.id%10000==0:
      bot.send_message(message.chat.id, f'ПОЗДРАВЛЯЮ. ЭТО {message.id} СООБЩЕНИЕ В ЧАТИКЕ! С НОВЫМ КРУГОМ СПАМА!', reply_to_message_id=message.id)
    elif 'мат' in message.text.casefold() :
      bot.send_message(message.chat.id, text = replacer.replacer_mat(message.text), disable_notification=True)
      bot.send_sticker(message.chat.id, sticker = random.choice(Config.f_ck_list), disable_notification=True)
      print('mat')
    elif 'хер' in message.text.casefold():
      bot.send_message(message.chat.id, text = replacer.replacer_her(message.text), disable_notification=True)
      bot.send_sticker(message.chat.id, sticker = random.choice(Config.f_ck_list), disable_notification=True)
      print('her')
    elif 'скуш' in message.text.casefold():
      bot.send_message(message.chat.id, text = replacer.replacer_skush(message.text), disable_notification=True)
      bot.send_sticker(message.chat.id, sticker = random.choice(Config.f_ck_list), disable_notification=True)
      print('skush')
    elif 'скара' in message.text.casefold():
      global iter
      iter[message.from_user.id] = iter.get(message.from_user.id, 0) + 1
      mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
      bot.send_message(message.chat.id, text = f'{mention}, ты затриггеришь Скарасрач, это твое {iter[message.from_user.id]} упоминание в чате после перезапуска!', disable_notification=True, parse_mode="HTML")
      bot.send_sticker(message.chat.id, sticker = random.choice(Config.raiden_list), disable_notification=True)
      print('skara')
    elif 'ахуенная тема'  in message.text.casefold():
      bot.send_sticker(message.chat.id, sticker = random.choice(Config.svin_list), disable_notification=True, reply_to_message_id=message.id)
      print('svin')
    elif 'юзхуй' in message.text.casefold():
      iterdroch[message.from_user.id] = iterdroch.get(message.from_user.id, 0) + 1
      mention = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
      bot.send_message(message.chat.id,text=f'{mention}, ты успешно вздрочнул. На счету {iterdroch[message.from_user.id]} дрочка!', disable_notification=True, parse_mode="HTML")
    elif message.text.casefold() == 'жаба инфо':
      answer = f"🏃‍♂️:Отправить на работу можно будет через {random.randint(0, 23)}ч:{random.randint(0, 59)}м\n🍭:Можно покормить через {random.randint(0, 23)}ч:{random.randint(0, 59)}м\n(Откормить через {random.randint(0, 23)}ч:{random.randint(0, 59)}м)\n\n🔪:{random.choice(Config.duel_list)}\n☠️:{random.choice(Config.dunge_list)}\n⚔️:{random.choice(Config.arena_list)}\n\n💃:{random.choice(Config.tusa_list)}\n💘:{random.choice(BenCam.first_name)} и {random.choice(BenCam.first_name)}\n\U0001F977: Вы не участвуете в ограблении"
      bot.send_message(message.chat.id, text = answer, reply_to_message_id=message.id)
    '''
    for i in range(0, len(Config.filterlist)):
        if
            if  Config.filterlist[i] in message.text.casefold():
                bot.send_photo(message.chat.id, photo = 'AgACAgIAAxkBAANFYw4KBHk8YPfVCAt3ziZrtjNHlPcAAuG9MRtra3FIcOUQ95-qWGkBAAMCAAN4AAMpBA', reply_to_message_id=message.id)
   '''
@bot.message_handler(content_types=["sticker"])
def stckmes(message):
    if message.sticker.set_name == 'myashhh_by_fStikBot':
      bot.send_sticker(message.chat.id, sticker=message.sticker.file_id, reply_to_message_id=message.id, disable_notification=True)
      print('sticker')
    elif message.sticker.set_name =='Trash_amirMS19':
      bot.send_sticker(message.chat.id, sticker=message.sticker.file_id, reply_to_message_id=message.id, disable_notification=True)
      print('sticker')
   #    bot.send_message(message.chat.id, "Моя твоя не понимать")
   #    bot.send_sticker(message.chat.id, sticker ='CAACAgIAAx0CZ4LuFAACRf1jBzUpN0mJZhkmcmLlu7hXcizJgQACpxEAAtW2AUsFwb3PlpBVpykE')
    elif message.chat.id == int(os.environ.get('me')):

      bot.send_message(chat_id = int(os.environ.get('me')), text = f'{message.sticker.file_id}')

@bot.message_handler(content_types=["photo"])
def photomes(message):
    if message.chat.id == int(os.environ.get('me')):
      photo = max(message.photo, key=lambda x: x.height)
      file_id = photo.file_id
      bot.send_message(int(os.environ['me']), text = f'{file_id}')

reflask.keep_alive()
bot.polling(non_stop=True)
