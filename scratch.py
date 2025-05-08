import telebot
import random
import apiai
import telegram
import json
import time
token = '592841312:AAEuLRBVXorLpI_2rttwphQeiLon6nQ_AA'
bot = telebot.TeleBot(token)

'''
@bot.message_handler(content_types=["text"])
def resend_all_message(message):
    bot.send_message(message.chat.id, "Well-well, I'm the first!")
'''

@bot.message_handler(commands=["start"]) #bot greets user
def send_start_message(message):
    bot.send_message(message.chat.id, "Good day to you!")

@bot.message_handler(commands=["hinkaliki"]) #sends a location of really good khinkali restaurant
def send_start_message(message):
    bot.send_location(chat_id=message.chat.id, latitude=50.002556, longitude=36.2402947)

@bot.message_handler(commands=["location"]) #sends location of summer school
def send_start_message(message):
    bot.send_location(chat_id=message.chat.id, latitude=49.999019, longitude=36.2498061)

@bot.message_handler(commands=["legends_traditions"]) #describes the legend of the khinkali's origin
def send_start_message(message):
    bot.send_message(message.chat.id, "Long ago, in the misty highlands of the Georgian Khevsureti region, a resourceful shepherd named Giorgi discovered the secret to taming the mountain’s fierce cold winds—and his own rumbling belly. One morning, he took a handful of dough, flattened it, and placed inside a spiced mixture of freshly minced lamb, onions, garlic, and fragrant mountain herbs. He pinched the edges of the dough high into a twisted peak, sealing in the precious juices that would otherwise escape into the snow.")
    bot.send_message(message.chat.id, "When his fellow villagers tasted the steaming parcels, their eyes shone with delight: the rich broth burst like warm sunshine on a winter’s morning, and the tender meat melted on the tongue. They named these little treasures “khinkali,” from the word khini (juices), and passed down the recipe through generations. To this day, each perfectly pleated crown of khinkali honors Giorgi’s ingenuity—and the mountain air that inspired it.")

@bot.message_handler(commands=["features"]) #highlights the peculiarities of cooking
def send_start_message(message):
    bot.send_message(message.chat.id, "Cooking khinkali is an art that balances precision and tradition. The dough must be soft yet strong enough to hold the juicy filling—typically a mixture of minced meat, herbs, and broth—without tearing. Each dumpling is carefully hand-folded into a twisted topknot with 18 to 20 pleats, a point of pride for skilled cooks.")
    bot.send_message(message.chat.id, "Unlike other dumplings, khinkali are boiled, not steamed or fried, in salted water until they float—signaling their readiness. The key is keeping the juice inside; the meat filling is raw when wrapped, so it cooks in its own savory broth during boiling. A perfectly cooked khinkali holds this broth like a pouch—meant to be bitten gently at the side, the liquid sipped first, then the rest devoured, leaving only the tough doughy “kudi,” or topknot, on the plate.")

@bot.message_handler(commands=["types"]) #names the types of khinkali
def send_start_message(message):
    bot.send_message(message.chat.id, "Khinkali come in a variety of delicious forms, each reflecting local tastes and traditions. The classic version is kalakuri, filled with minced meat—usually a mix of beef and pork—blended with herbs, onions, and rich broth. In the mountains, khevsuruli is more traditional: a simpler, spicier filling of lamb and black pepper without herbs.")
    bot.send_message(message.chat.id, "For vegetarians, there’s mushroom khinkali or potato khinkali, often seasoned with fresh cilantro or tarragon. Some modern versions feature cheese or even spinach fillings, while creative kitchens in Tbilisi have begun offering khinkali with seafood or truffle. Though the fillings may vary, the iconic pleated shape and juicy interior remain the heart of every khinkali.")

@bot.message_handler(commands=["Yep"]) #it was a joke about my ex... I guess...
def send_start_message(message):
    bot.send_message(365227046, message.text[3:])
    bot.send_message(message.chat.id, "Ok, I've heard you. Anton'll answer, when he is online again... ❤🌸")

@bot.message_handler(commands=["how_send_message_admin"]) #communication with admins
def send_start_message(message):
    bot.send_message(message.chat.id, "Print /send_message_admin and your text/feedback")

@bot.message_handler(commands=["calc"]) #calories calculator
def send_start_message(message):
    s = message.text
    #command=[]
    #command= s.split(' ')
    command, a = s.split(' ', 1)
    x = 2.346
    c = k * int(a)
    print(command, a)
    print(s)
    bot.send_message(message.chat.id, "Congrats, you've eat " + str(c) + "calories!")

@bot.message_handler(commands=["help"]) #another joke...
def send_start_message(message):
    bot.send_message(message.chat.id, "Just rest in peace, bro :)")

@bot.message_handler(commands=["menu"]) #another joke... x2
def send_start_message(message):
    bot.send_message(message.chat.id, "If need psychological support - call Ivan +380******284")

@bot.message_handler(commands=["credits"]) #names a programmists who wrote this... kind of masterpiece
def send_start_message(message):
    bot.send_message(message.chat.id, "made by Alexanra, Anastasiia and Sophia - participants of STEMCampSchool2018 ")

@bot.message_handler(commands=["schuteechka"]) #jokes randomizer
def send_start_message(message):
    jokes = ['Why did the scarecrow win an award? - Because he was outstanding in his field!',
             'What’s a computer’s favorite snack? - Microchips!',
             'Why don’t scientists trust atoms? - Because they make up everything!',
             'Why did the math book look sad? - It had too many problems.',
             'What do you call fake spaghetti? - An impasta!',
             'Why can’t you give Elsa a balloon? - Because she’ll let it go!',
             'Why did the bicycle fall over? - It was two-tired!']
    n = random.randint(0,len(jokes)-1)
    bot.send_message(message.chat.id, jokes(n))

@bot.message_handler(commands=["recipes"]) #sends links to various cites with khinkali's recipes 
def send_start_message(message):
    recipes = ['https://www.stb.ua/ru/2017/06/07/domashnee-morozhenoe-top-5-prostyyh-retseptov/','https://smachno.ua/posts/vse-bude-smachno/hinkali-retsept-testa-i-fars']
    rrr = random.randint(0, len(recipes) - 1)
    bot.send_message(message.chat.id, recipes[rrr])

'''
@bot.message_handler(commands=[""])
def send_start_message(message):
    bot.send_message(message.chat.id, "")
'''

@bot.message_handler(content_types=["text"]) #simulates communication (AI)
def resend_all_message(message):
    bot.send_chat_action(message.chat.id, telegram.ChatAction.TYPING)
    # bot.send_message(message.chat.id, "OK, I'll deal with it later")
    text = message.text
    request = apiai.ApiAI('47fb7be69b6ca4cae9e2324a0ddea90d9').text_request()  # API-token for Dialogflow
    request.lang = 'ru'  # request's language
    request.session_id = message.chat.id  # ID of dialod session (to teach bot after)
    request.query = message.text  # sending a request to AI with user's message
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']  # unpack JSON and put out an answer (if we have an answer -> sending to user, if not -> bot hasn't understand a request)
    if response:
        bot.send_message(chat_id=message.chat.id, text=response)
    else:
        bot.send_message(message.chat.id, 'Sad but true: bot hasn’t understand your request. Please report this matter to admin through /send_message_admin with a full description')
    print(message.chat.id, message.chat.first_name, message.chat.last_name, message.text)

@bot.message_handler(content_types=["photo"]) #responds to user's requests with photos, memes etc.
def resend_all_message(message):
    bot.send_chat_action(message.chat.id, telegram.ChatAction.TYPING)
    bot.send_message(message.chat.id, "\U0000F311")
    bot.send_chat_action(message.chat.id, telegram.ChatAction.UPLOAD_PHOTO)
    photos = ['C:/Users/111/Downloads/7r0ca4.jpg', 'C:/Users/111/Pictures/maxresdefault.jpg', 'C:/Users/111/Pictures/khinkal1.jpg', 'C:/Users/111/Pictures/3-6.jpg']
    n = random.randint(0, len(photos) - 1)
    bot.send_photo(message.chat.id, photo=open(photos[n], 'rb'))

@bot.message_handler(content_types=["video"]) #responds to user's requests with videos, memes etc.
def resend_all_message(message):
    bot.send_chat_action(message.chat.id, telegram.ChatAction.TYPING)
    bot.send_message(message.chat.id, "OK, I'll deal with it later")
    bot.send_chat_action(message.chat.id, telegram.ChatAction.TYPING)
    bot.send_message(message.chat.id, "But I hope you've send smth fun")
    bot.send_photo(message.chat.id, photo=open('C:/Users/111/Downloads/elchan.jpg', 'rb'))

def main():
    bot.polling(none_stop=True)
main()



