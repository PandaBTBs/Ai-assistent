import json, pyaudio
from urllib import response
from vosk import Model, KaldiRecognizer
import webbrowser
import datetime
import os
from num2t4ru import num2text
import time
import utils.tts

space = " "
model = Model("#")#VOSK MODEL
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,
                frames_per_buffer=8000)

stream.start_stream()

def lisen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']
                        
print('\n Задайте вопрос... \n @браузер / @время / @стим.запусти стим / @запись.зпись экрана / @снимок экрана.запусти снимок \n @история / @синий.зпусти синий / @общение.друзья \n @погода @закрыть.выключение')
        
        
for text in lisen():
            
    print(f'user: {text}')
    
    if text == "команда" or text == "команды":
        response()
        
    elif text == "браузер":
        webbrowser.open("https://www.google.ru/?hl=ru")
        
    elif text == "время" or text == "текущее время" or text == "сейчас времени" or text == "который час":
        now = datetime.datetime.now()
        text = "В данный момент " + num2text(now.hour) + ":"  + num2text(now.minute)
        utils.tts.va_speak(text)
        
    elif text == 'синий' or text == "запусти синий":
        os.startfile('D:\steamT1\steam.exe')
        utils.tts.va_speak('Открываю стим')
        utils.tts.va_speak('открыла') 
        
    elif text == "запись" or text == "запись экрана":
        webbrowser.open("steam://rungameid/1905180")
        utils.tts.va_speak('Открываю')
        utils.tts.va_speak('открыла')
        
    elif text == "снимок экрана" or text == "запусти снимок":
        os.startfile(r'D:/steamT1/steamapps/common/ShareX/ShareX_Launcher')
        utils.tts.va_speak('Открываю')
        utils.tts.va_speak('открыла') 
        
    elif text == 'история':
        
        utils.tts.va_speak('Хорошо, активирован, навык, истории, Какую историю, Вы, хотите выбрать?')
        print('pls input History: hs1, hs2, hs3, hs4')
        
        hs = str(input())
        
        if hs == 'hs1':
            print('---------------------history-1---------------------')
            text = 'Хорошо, давайте, придумаем занимательную историю,'
            text+= 'Объяснительная, об, опоздании'
            utils.tts.va_speak(text)
        
        
            utils.tts.va_speak('Для начала, скажи, куда мы опоздали')
            locally_1 = str(input(f'1. Место 1: {space}'))
        
            utils.tts.va_speak('теперь, назови животное, мужского рода')
            genus_m = str(input(f'2. Животное мужского рода: {space}'))
        
            utils.tts.va_speak('теперь, назови, животное, женского рода')
            genus_w = str(input(f'3. Животное женского рода: {space}'))
        
            utils.tts.va_speak('где?')
            locally_2 = str(input(f'4. Место 2: {space}'))
        
            utils.tts.va_speak('животное, во множественном, числе')
            animals = str(input(f'5. Животное во множественном числе: {space}'))
        
            utils.tts.va_speak('куда?')
            locally_3 = str(input(f'6. Куда?: {space}'))
        
            utils.tts.va_speak('и, на последок, скажи, имя, твоего знакомого')
            input_us = str(input(f'7. Имя твоего знакомого: {space}'))
            
            print('loading...')
            utils.tts.va_speak(f'И так, объяснительная, сегодня когда я шёл {locally_1}, \
            на меня внезапно свалился мокрый {genus_m}, я закричал как {genus_w},\
            и потерял сознание, очнулся я в {locally_2}, и сказал, отвезите меня {locally_1},\
            мне очень надо, но эти мои {animals}, почему то, отвезли меня {locally_3},\
            и от туда, я шёл пешком, пока меня не подвёз пьяный {input_us}. Вот, почему я опоздал\
             {locally_1}. Мне кажется, получилось прикольно.')
   
        if hs == 'hs2':
            print('---------------------history-2---------------------')
            text = 'Отлично,'
            text+= 'Текст про, цирк'
            utils.tts.va_speak(text)
            
            utils.tts.va_speak('Для начала, назови, знаменитого мужчину')    
            puple_1 = str(input(f'1. Имя знаменитого мужчины: {space}'))
            
            utils.tts.va_speak('какой?')    
            quality_1 = str(input(f'2. Какой?: {space}'))
            
            utils.tts.va_speak('Назови, еще, одного, знаменитого мужчину')    
            puple_2 = str(input(f'3. Имя ещё одного знаменитого мужчины: {space}'))
            
            utils.tts.va_speak('Какой? в несколько слов')    
            quality_2 = str(input(f'4. Какой? в несколько слов: {space}'))
            
            utils.tts.va_speak('Теперь ,назови, предмет, мужчкого рода')    
            item_1 = str(input(f'5. Предмет мужчкого рода: {space}'))
            
            utils.tts.va_speak('Какой?')    
            quality_item = str(input(f'6. Какой?: {space}'))
            
            utils.tts.va_speak('Назови, ещё, один предмет, мужчкого рода')    
            item_2= str(input(f'7. ещё один предмет мужчкого рода: {space}'))
            
            utils.tts.va_speak('И, последний вопрос. Какой?')    
            quality_3 = str(input(f'8. Какой?: {space}'))
            
            print('loading...')
            utils.tts.va_speak(f'Внимание!!, вот что получилось,: вчера, я ходила в цирк, сначала на арену, \
            выскочил {quality_1}, {puple_1}, за ним выполз {quality_2}, {puple_2}, и они бросались тухлой рыбой целый час,\
            за тем вышел, клоун у которого в руках был {item_2}, клоун бросил этот{item_2} в зрителей,\
            и попал прямо в меня. Я обидилась, Достала из своего кармана {quality_3}, {item_1}, \
            кинула в клоуна, и попала, прямо в лоб. Мне понравился этот цирк. По моему, получилась прикольная история.')     
                   
        if hs == 'hs3':
            print('---------------------history-3---------------------') 
            text = 'Хорошо, давайте придумаем, занимательную историю,'
            text+= 'Гороскоп, для близнецов.'
            utils.tts.va_speak(text)
            
            utils.tts.va_speak('Для начала, назови своего любимого актёра')
            hs3_1 = str(input(f'1. Твой любимый актёр: {space}'))
            
            utils.tts.va_speak('Какое любимое занятие, у этого человека?')
            hs3_2 = str(input(f'2. Его любимое занятие: {space}'))
            
            utils.tts.va_speak('Теперь, назови имя человека, который тебе не нравится')
            hs3_3 = str(input(f'3. Имя человека, который тебе не нравится: {space}'))
            
            utils.tts.va_speak('Как думаешь, ч+ем любит заниматься этот человек?')
            hs3_4 = str(input(f'4. Чем любит заниматься этот человек?: {space}'))
            
            utils.tts.va_speak('И, на последок, какие люди тебя окружают?')
            hs3_5 = str(input(f'5. Какие люди тебя окружают?: {space}'))
            
            print('loading...')
            utils.tts.va_speak(f'Весной вам вдруг покажется, что у вас раздвоение личности. Вы вроде {hs3_1}, ив тоже время\
            {hs3_3}. временами они будут ругаться, и очень утомлять, Вас, этим. Осенью у вас могут появиться вредные привычки\
            , такие как {hs3_2} ночью на крыше, {hs3_4}, на красной площади, ковырять в насу, с крикаим нашёл.  В декабре,\
            в Кремле, вам вручат золотоую медаль, {hs3_5}, близнецы страны. Почаще советуйтесь со своим внуртенним голосом. И всё будет отлично.\
            Я думаю получилось неплохо.')    
        
        if hs == 'hs4':
            print('---------------------history-4---------------------') 
            text = 'Хорошо, давайте, придумаем занимательную историю,'
            text+= 'Гороскоп для тельцов.'
            utils.tts.va_speak(text)
            
            utils.tts.va_speak('Сперва, назови существо, мужского рода.')
            hs4_1 = str(input(f'1. Существо мужского рода: {space}'))     
            
            utils.tts.va_speak('Теперь, какойнибудь напиток.')
            hs4_2 = str(input(f'2. Напиток:{space}'))  
            
            utils.tts.va_speak('Какой?')
            hs4_3 = str(input(f'3. Какой?:{space}')) 
            
            utils.tts.va_speak('Назови имя, кинозвезды...')
            hs4_4 = str(input(f'4. Имя кинозвезды:{space}'))

            utils.tts.va_speak('Теперь, большой предмет, женского рода.')
            hs4_5 = str(input(f'5. Большой предмет женского рода:{space}'))
            
            utils.tts.va_speak('И последнее, назови число, которе тебе не нравиться.')
            hs4_6 = str(input(f'6. Число:{space}'))
            
            print('loading...')
            utils.tts.va_speak(f'И так, гороскоп для тельцов. Ваша любимая рифма - телец, молодец, и это правда. Вам всё\
            удаётся, и друзья завидуя, называют вас {hs4_3}, {hs4_1}. Весной вы поставите рекорд, выпьете залпом\
            {hs4_6} своего любимого напитка, {hs4_2}, а ещё, вы получите приглашение на телевидение, где вас\
            будет ждать большая {hs4_5}, которую вручит {hs4_4}. Не надо нинакого бычиться, и всё будет превосходно.\
            По-моему, чудесный гороскоп.')
            
        else:
            print('Выход, введите любое значение.')
            i = str(input())
            if i == 'exit':
                pass
            else:
                pass
            
    elif text == "общение" or text == "друзья":
        webbrowser.open("https://discord.com/channels/@me")
        utils.tts.va_speak("Дискорд, открыт.")
        
    elif text == "погода":
        import requests
        import datetime
        from pprint import pprint
        from weather_token import open_weather_token


        def get_weather(city, open_weather_token):

            code_to_smile = {
                    "Clear": "Ясно \U00002600",
                    "Clouds": "Облачно \U00002601",
                    "Rain": "Дождь \U00002614",
                    "Drizzle": "Дождь \U00002614",
                    "Thunderstorm": "Гроза \U000026A1",
                    "Snow": "Снег \U0001F328",
                    "Mist": "Туман \U0001F32B"
                    }

            try:
                r = requests.get(
                        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
                    )
                data = r.json()
                pprint(data)

                city = data["name"]
                cur_weather = data["main"]["temp"]

                weather_description = data["weather"][0]["main"]
                if weather_description in code_to_smile:
                    wd = code_to_smile[weather_description]
                else:
                    wd = "Посмотри в окно, не пойму что там за погода!"

                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]
                wind = data["wind"]["speed"]
                sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
                sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
                length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
                data["sys"]["sunrise"])

                rez =(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
                            f"Влажность: {humidity}%\nВетер: {wind} м/с\n"
                            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                            f"Хорошего дня!"
                        )
                print(rez)
                    
            except Exception as ex:
                print(ex)
                print("Проверьте название города")


        def main():
            utils.tts.va_speak("Скажите город")
            print("City: ...")
            for text in lisen():
            
                text = text.title()  
                print(text)

                get_weather(text, open_weather_token)
                break

        if __name__ == '__main__':
            main()

    elif text  == "закрыть" or text == "выключение":
        utils.tts.va_speak("выключаюсь")
        quit()

    else:
        # Point to the local server
        print("log...")
        from openai import OpenAI
        client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
        while __name__ == '__main__':
            completion = client.chat.completions.create(
                        model="TheBloke/dolphin-2.2.1-mistral-7B-GGUF",
                        messages=[
                        {"role": "system", "content": "Always answer briefly."},
                        {"role": "user", "content": text} 
                        ],
                        temperature=0.4,
                        )

            l = str(completion.choices[0].message)
            seconds = time.time()
            seconds_last = time.ctime(seconds)
            print('AI: ' + l[32:-57] + f" \n {seconds_last}")
            utils.tts.va_speak(l[32:-57])
            break
