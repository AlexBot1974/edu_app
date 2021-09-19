#edu_help_bot telegram
#Let s import libs
import pandas as pd
import re  #for regular expression
import pickle
import telebot
#!pip install PyTelegramBotAPI if nessesery

TOKEN_RE = re.compile(r'[\w\d]+')  #regular expression to start with

def tokenize_text_simple_regex(txt, min_token_size=2):
    """ This func tokenize text with TOKEN_RE applied ealier """
    txt = txt.lower()
    all_tokens = TOKEN_RE.findall(txt)
    return [token for token in all_tokens if len(token) >= min_token_size]

#let s load our model, make sure that model file in the same dir with this py file
loaded_model = pickle.load(open('model_edu_01.pickle', 'rb'))


bot = telebot.TeleBot('put token bot here')

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    start_message='''✌️✌️✌️✌️✌️Это бот-помошник в обучении.\n
                 Какие курсы мне нужно пройти, чтобы стать программистом?\n
                 Как стать разработчиком на Python,Си?\n
                 Это и много другое я уже знаю!✌️✌️✌️✌️✌️\n
                 Напишите мне запрос на русском или английском языке\n'''
    bot.reply_to(message,start_message)

courses_dict = {
    0:'Repeat please in other words. Перефразируйте пожалуйста вопрос.',
    1:'https://stepik.org/course/67/promo',  #python1'
    'python2':'https://stepik.org/course/512/promo',
    'sql':'https://stepik.org/course/551/promo',
    'ml':'https://stepik.org/course/80782/syllabus',
    'r':'https://stepik.org/course/129/syllabus',
    'git':'https://stepik.org/course/3145/syllabus',
    'cv':'https://stepik.org/course/50352/promo',
    'nlp':'https://stepik.org/course/54098/promo',
    'linux1':'https://stepik.org/course/73/promo',
    'iot':'https://stepik.org/course/71759/promo',
    'hadoop':'https://stepik.org/course/150/promo',
    2:'https://stepik.org/course/187/promo',  #java1
    'java2':'https://stepik.org/course/146/promo',
    'java3':'https://stepik.org/course/186/promo',
    'spring':'https://stepik.org/course/90739/promo',
    7:'https://stepik.org/course/5703/promo',  #android
    3:'https://stepik.org/course/54403/promo',  #golang
    4:'https://stepik.org/course/62383/promo',  #php
    5:'https://stepik.org/course/16243/promo',   #scala
    6:'https://stepik.org/course/13929/promo',   #javascript
    'react':'https://stepik.org/course/3050/promo', 
    'html':'https://stepik.org/course/52164/promo',
    'css':'https://stepik.org/course/52164/promo',
    'kotlin':'https://stepik.org/course/4792/promo',
    8:'https://stepik.org/course/3278/promo',  #ios
    'objective-c':'https://intuit.ru/studies/courses/4811/1058/info',
    9:'https://stepik.org/course/363/promo',  #'cpp'
    10:'https://stepik.org/course/51198/promo', #'c sharp1'
    'c sharp2':'https://stepik.org/course/84983/promo',
    'english':'https://stepik.org/course/6891/promo',
    'stat':'https://stepik.org/course/701/promo',
    'algo':'https://stepik.org/course/217/promo',
    11:'https://stepik.org/course/1612/syllabus',  #'docker'

}
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    token=message.text
    answer=loaded_model.predict([str(token)])[0]  #get data from model
    answer = courses_dict[int(answer)]  #get course
    user=str(message.from_user.username)
    print('Telegram user :',user)
    print('Vopros: ',token)    #we print that for debiging
    print(type(answer))
    print('Otvet: ',end=' ')
    print(answer)
    bot.send_message(message.chat.id, str(answer))
    del answer  #we del variable in order not to use extra memory

#start bot
if __name__ == '__main__':
    print('bot started.')
    bot.polling(none_stop=True)



