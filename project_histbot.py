import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import json
import pymorphy2
import wikipedia


with open('project_date.json', 'r', encoding='utf8') as read_file:
    data = json.load(read_file)
    read_file.close()
date = list(data)


j = False
first_message = True


def main():
    vk_session = vk_api.VkApi(token='vk1.a.VwouBQ6DHOP9cnbNU0A6XuUq0I6cSgso23phzeWTq0ygM8T7ujKX9IDE7MqEdM0MycRGd6TDff8usXa88YQcpaghD5mNtQ05aT3dfLZVVt1zyve6iSaJk20oh2ZYNKibG4ZiuwP68VNq5FMgElTyTGKxjf6WYdbA4C1xlkrtS7Ypu_mgvjDjQR8mwp9bSk4ypWorNGf4FhspyykgLodwEg')
    longpoll = VkBotLongPoll(vk_session, 220100919)
    vk = vk_session.get_api()
    global first_message

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            if first_message:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Вас приветствует History_Bot!\nЧтобы ввести ответ на дату начинайте Ваше сообщение со слова 'событие'\nДля того чтобы завершить тренировку введите '/stop'",
                                 random_id=random.randint(0, 2 ** 64))
                first_message = False


            morph = pymorphy2.MorphAnalyzer()
            global j
            global date
            if event.obj.message['text'] != '/stop':
                if not(j):
                    a = random.choice(date)
                print(a)
                if not ('событие' in event.obj.message['text']):

                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f"Какое событие было в {a}?",
                                     random_id=random.randint(0, 2 ** 64))
                    j = True
                    if len(date) > 0:
                       ind = date.index(a)
                       del date[ind]
                    else:
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=f"Спасибо за тренировку!",
                                         random_id=random.randint(0, 2 ** 64))

                else:
                    czet = 0
                    k = event.obj.message['text'].split()
                    for i in k:
                        i = i.lower()
                        i = morph.parse(i)[0].normal_form
                        print(i)
                        if i in data[a]['poick']:
                            czet += 1
                        if czet > 1:
                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message=f"Верно!",
                                             random_id=random.randint(0, 2 ** 64))
                            if len(date) > 0:
                                a = random.choice(date)
                                vk.messages.send(user_id=event.obj.message['from_id'],
                                                 message=f"Какое событие было в {a}?",
                                                 random_id=random.randint(0, 2 ** 64))
                                ind = date.index(a)
                                del date[ind]
                                print(a)
                                j = True
                                break
                            else:
                                vk.messages.send(user_id=event.obj.message['from_id'],
                                                 message=f"Спасибо за тренировку!",
                                                 random_id=random.randint(0, 2 ** 64))
                    print(czet)
                    if czet < 2:
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=f"Событие {data[a]['name']}",
                                         random_id=random.randint(0, 2 ** 64))
                        wikipedia.set_lang("ru")
                        if len(wikipedia.search(data[a]['name'])) != 0:
                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message=f"{wikipedia.summary(data[a]['name'], 4)}",
                                             random_id=random.randint(0, 2 ** 64))
                        if len(date) > 0:
                            a = random.choice(date)
                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message=f"Какое событие было в {a}?",
                                             random_id=random.randint(0, 2 ** 64))
                            ind = date.index(a)
                            del date[ind]
                            print(a)
                            j = True
                        else:
                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message=f"Спасибо за тренировку!",
                                             random_id=random.randint(0, 2 ** 64))




            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f"Спасибо за тренировку!",
                                 random_id=random.randint(0, 2 ** 64))



            vk = vk_session.get_api()




if __name__ == '__main__':
    main()