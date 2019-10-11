import telebot
import pyowm

token ="948460085:AAEnFRqUzs2Cs4hbOy9bThfNftufk84S7kk"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "В каком городе тебе показать погодку?")
    bot.register_next_step_handler(city, weath)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! С возвращением! Долгий выдался денек...")
    
@bot.message_handler(content_types=["text"])
def start(message):    
    if message.text.lower() == "привет" or message.text.lower() == "прив":
        bot.send_message(message.chat.id, "Как дела?")
    elif message.text.lower() == "хорошо":
        bot.send_message(message.chat.id, "Рада это слышать)")
    elif message.text.lower() == "плохо" or message.text.lower() == "неочешь" or message.text.lower() == "не очень":
        bot.send_message(message.chat.id, "Что случилось?")
    else:
        bot.send_message(message.chat.id, "Я не понимаю, что ты хочешь(")

@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "В каком городе Вам показать погодку?")
    bot.register_next_step_handler(city, weath)
    
    
    
def weath(message):
    owm = pyowm.OWM('e66f44a7307d861a4f43beacd89239d5', language="ru")
    city = message.text
    weather = owm.weather_at_place(city)
    w = weather.get_weather()
    temperature = w.get_temperature("celsius")["temp"]
    wind = w.get_wind()["speed"]
    hum = w.get_humidity()
    desc = w.get_detailed_status()
    bot.send_message(message.chat.id, "Сейчас в городе " + str(city) + " " + str(desc) + ", температура - " + str(temperature) + "°C, влажность - " + str(hum) + "%, скорость ветра - " +str(wind) + "м/с.")
    

if __name__ == "__main__":
    bot.polling(none_stop=True)