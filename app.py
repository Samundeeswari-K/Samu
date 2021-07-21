from telegram.ext import Updater, MessageHandler,Filters
from Adafruit_IO import Client
import os
aio = Client('Samundeeswari',os.getenv('Samundeeswari'))

def demo1(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://image.shutterstock.com/image-vector/ok-hand-lettering-handmade-calligraphy-260nw-669965602.jpg'
  bot.message.reply_text('I am fine')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo2(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://i1.wp.com/allislandsinspections.com/wp-content/uploads/2014/08/lamp_3.jpg'
  bot.message.reply_text('LIGHT is turned ON')
  aio.send('bedroom-light', 1)
  data1 = aio.receive('bedroom-light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo3(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://image.shutterstock.com/image-photo/light-bulb-turned-off-over-260nw-162882104.jpg'
  bot.message.reply_text('LIGHT is turned OFF')
  aio.send('bedroom-light', 0)
  data1 = aio.receive('bedroom-light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo4(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://www.warnerservice.com/hs-fs/hubfs/ceiling-fan.jpg?width=1000&name=ceiling-fan.jpg'
  bot.message.reply_text('FAN is turned ON')
  aio.send('bedroom-fan', 1)
  data2 = aio.receive('bedroom-fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo5(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://www.chanish.org/wp-content/uploads/2019/06/ceiling_fan_light_wont_turn_on_ceiling_fan_light_wont_turn_off_2.jpg'
  bot.message.reply_text('FAN is turned OFF')
  aio.send('bedroom-fan', 0)
  data2 = aio.receive('bedroom-fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a == "how are you?":
    demo1(bot,update)
  elif a =="light on" or a=="turn on light":
    demo2(bot,update)
  elif a =="light off" or a=="turn off light":
    demo3(bot,update)
  elif a =="switch on the fan" or a=="turn on fan":
    demo4(bot,update)
  elif a =="switch of the fan" or a=="turn off fan":
    demo5(bot,update)
  else:
    bot.message.reply_text('Invalid Text')
BOT_TOKEN = os.getenv('BOT_TOKEN')
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
