# ///////////////////////////////////////////////////////// [IMPORT MODULES] /////////////////////////////////////////////////////////
from vk_api import VkApi
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkChatEventType
from vk_api.utils import get_random_id
from threading import Thread
from time import sleep
import schedule
import time

# ///////////////////////////////////////////////////////// [MASSIVE & DATA] /////////////////////////////////////////////////////////
ids_chat = [
    2000000026, # Русский язык 1
    2000000014, # Русский язык 2
    2000000034, # Русский язык 3
    2000000046, # Русский язык 4
    2000000021, # Информатика
    2000000048, # Математика
    2000000035, # Химия
    2000000019, # Английский
    2000000017, # Физика
    2000000018, # Обществознание
    2000000032, # Обществознание 2
    2000000047, # Обществознание 3
    2000000023, # Литература
    2000000015, # История
    2000000016, # Биология
    2000000028, # Биология 2
]

ids_teacher = [
    159523091, # Назиля (Русский язык)
    37066446, # Диляра (Обществознание)
    88864448, # Анвар (Физика)
    105722192, # Оля (История)
    241310331, # Антонина (Биология)
    44618787, # Регина(Английский язык)
    333017994, # Равиль (Зам Директора)
    23526696, # Альберт (Директор)
    504785497, # Санчай (Санчай)
    514032713, # Саша (Информатика)
    99087342, # Наргиза (Завуч)
    538148783, # Виля (Литература)
    102234475, # Евгения (Химия)
    99916294, # Камилла (Информатика)
]

# SCHOOL OBJECTS
ids_lit = [
    2000000023, # Литература
]
ids_inf = [
    2000000021, # Информатика
]
ids_chem = [
    2000000035, # Химия
]
ids_ss = [
    2000000018, # Обществознание
    2000000032, # Обществознание 2
    2000000047, # Обществознание 3
]
ids_hist = [
    2000000015, # История
]
ids_bio = [
    2000000016, # Биология
    2000000028, # Биология 2
]
ids_phys = [
   2000000017, # Физика
]
ids_math = [
    2000000048, # Математика
]
ids_rus = [
    2000000026, # Русский язык 1
    2000000014, # Русский язык 2
    2000000034, # Русский язык 3
    2000000046, # Русский язык 4
]
ids_eng = [
    2000000019, # Английский
]
# ССЫЛКИ
link= 'https://vk.cc/9O13cN'
link_lit = 'https://vk.cc/a3K5QY'

# ///////////////////////////////////////////////////////// [MASSIVE & DATA] /////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////// [BASIC FUNCTIONS] /////////////////////////////////////////////////////////

def send_message(peer_id, message):
    vk.messages.send(
        peer_id=peer_id,
        message=message,
        random_id=get_random_id(),
    )

def prizyv():
    members = vk.messages.getConversationMembers(
        peer_id = peer_id,
    )['items']
    members_ids = [member['member_id'] for member in members if member['member_id'] > 0]
    message = 'Призыв!'
    for member_id in members_ids:
        if len(message) >= 4075:
            send_message(peer_id, message)
            message = ''
        message += f'[id{member_id}|.]'
    send_message(peer_id, message)

def prizyv_all():
    for peer_id in ids_chat:
        members = vk.messages.getConversationMembers(
            peer_id = peer_id,
        )['items']

        members_ids = [member['member_id'] for member in members if member['member_id'] > 0]

        message = 'Призыв '
        for member_id in members_ids:
            if len(message) >= 4000:
                send_message(peer_id, message)
                message = 'Остальные: '
            message += f'[id{member_id}|.]'
        send_message(peer_id, message)

def messforall():
    for event in longPoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            from_id in ids_teacher  # id пользователя, который отправил сообщение
            peer_id in ids_chat # peer_id беседы или ЛС, откуда пришло сообщение

            # lower - это метод приведения к нижнему регистру. Для регистронезависимости.
            message = event.obj['text'].lower()

            # message теперь в нижнем регистре, поэтому все проверки делаем тоже в нижнем регистре
            if ('#' in message) and (from_id in ids_teacher):
                for i in range(len(ids_chat)):
                    send_message(ids_chat[i], message)
        return ''

# ///////////////////////////////////////////////////////// [SECONDARY FUNCTIONS] /////////////////////////////////////////////////////////
def Morning(ids):
    for peer_id in ids:
        members = vk.messages.getConversationMembers(
            peer_id = peer_id,
        )['items']

        members_ids = [member['member_id'] for member in members if member['member_id'] > 0]

        message = 'Привет, ребята! \nСегодня будет вебинар. Всех жду. \nСсылку на веб отправлю за 10 мин до начала.'
        for member_id in members_ids:
            if len(message) >= 4000:
                send_message(peer_id, message)
                message = 'Next: '
            message += f'[id{member_id}|.]'
        send_message(peer_id, message)

def OneHour(ids):
    for peer_id in ids:
        members = vk.messages.getConversationMembers(
            peer_id = peer_id,
        )['items']

        members_ids = [member['member_id'] for member in members if member['member_id'] > 0]

        message = 'Вебинар уже через час. \nНастраиваемся на работу и печатаем скрипт (он в группе).\n'
        for member_id in members_ids:
            if len(message) >= 4000:
                send_message(peer_id, message)
                message = 'Next: '
            message += f'[id{member_id}|.]'
        send_message(peer_id, message)


def Minute(ids):
    for peer_id in ids:
        members = vk.messages.getConversationMembers(
            peer_id = peer_id,
        )['items']

        members_ids = [member['member_id'] for member in members if member['member_id'] > 0]

        message = 'Начинаем занятие через 10 минут. Погнали! \nСсылка на веб: ' + link + '\n'
        for member_id in members_ids:
            if len(message) >= 4000:
                send_message(peer_id, message)
                message = 'Next: '
            message += f'[id{member_id}|.]'
        send_message(peer_id, message)

def razov(ids):
    for peer_id in ids:
        members = vk.messages.getConversationMembers(
            peer_id = peer_id,
        )['items']

        members_ids = [member['member_id'] for member in members if member['member_id'] > 0]

        message = 'Начинаем занятие через 10 минут. Погнали! \nСсылка на веб: ' + link_lit + '\nID для мобилы: 115-684-743'
        for member_id in members_ids:
            if len(message) >= 4000:
                send_message(peer_id, message)
                message = 'Next: '
            message += f'[id{member_id}|.]'
        send_message(peer_id, message)

# ЧАСОВОЙ ПОЯС -3
def scheduler() -> None:
# ВОСКРЕСЕНЬЕ
    # УТРО
    schedule.every().sunday.at('05:00').do(Morning, ids_chat)
    # ЗА ЧАС ДО ВЕБИНАРА
    schedule.every().sunday.at('06:00').do(OneHour, ids_inf) # Информатика
    schedule.every().sunday.at('07:00').do(OneHour, ids_hist) # История
    schedule.every().sunday.at('08:00').do(OneHour, ids_lit) # Литература
    schedule.every().sunday.at('09:00').do(OneHour, ids_bio) # Биология
    schedule.every().sunday.at('10:00').do(OneHour, ids_math) # Математика
    schedule.every().sunday.at('11:00').do(OneHour, ids_chem) # Химия
    schedule.every().sunday.at('12:00').do(OneHour, ids_ss) # Обществознание
    schedule.every().sunday.at('13:00').do(OneHour, ids_phys) # Физика
    schedule.every().sunday.at('14:00').do(OneHour, ids_eng) # Английский
    schedule.every().sunday.at('15:00').do(OneHour, ids_rus) # Русский
    # ЗА 10 МИНУТ ДО ВЕБИНАРА
    schedule.every().sunday.at('06:50').do(Minute, ids_inf) # Информатика
    schedule.every().sunday.at('07:50').do(Minute, ids_hist) # История
    schedule.every().sunday.at('08:50').do(razov, ids_lit) # Литература
    schedule.every().sunday.at('09:50').do(Minute, ids_bio) # Биология
    schedule.every().sunday.at('10:50').do(Minute, ids_math) # Математика
    schedule.every().sunday.at('11:50').do(Minute, ids_chem) # Химия
    schedule.every().sunday.at('12:50').do(Minute, ids_ss) # Обществознание
    schedule.every().sunday.at('13:50').do(Minute, ids_phys) # Физика
    schedule.every().sunday.at('14:50').do(Minute, ids_eng) # Английский
    schedule.every().sunday.at('15:50').do(Minute, ids_rus) # Русский

    while True:
        schedule.run_pending()
        sleep(1)

t = Thread(target=scheduler)
t.start()


# ///////////////////////////////////////////////////////// Конец планировщика /////////////////////////////////////////////////////////


#JASON
accessToken = '2e8f08dbcc12368c29c609f894976aaa5ff4a25d0a43e8e9b084a3fbc6b13765b0f55a667330963279231'
groupId = 183464879

vkBotSession = VkApi(token=accessToken)
longPoll = VkBotLongPoll(vkBotSession, groupId)
vk = vkBotSession.get_api()

while True:
    try:
        for event in longPoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                from_id = event.obj['from_id']
                peer_id = event.obj['peer_id']
                message = event.obj['text'].lower()
                sender_name = list(filter(lambda name: name['id'] == event.obj.from_id, [name for name in vk.messages.getConversationMembers(peer_id=event.obj.peer_id, fields='profiles')['profiles']]))[0]
                last_and_first_name = str(sender_name['first_name']) + ' ' + str(sender_name['last_name'])
                first_name = str(sender_name['first_name'])
                last_name = str(sender_name['last_name'])

                if "призыв" == message and (from_id in ids_teacher):
                    prizyv()
                if ('призови всех' in message) and (from_id in ids_teacher):
                    prizyv_all()
                if ('общее' in message) and ('сообщение' in message) and (from_id in ids_teacher):
                    messforall()
                if ('круто' == message) or ('cool' == message):
                    send_message(peer_id, 'О да, это точно круто! B-)')
                if ('джейсон' in message) and ('согласен' in message) and (from_id in ids_teacher):
                    send_message(peer_id, 'Да!')
            if 'action' in event.raw['object']:
                if ('chat_invite_user' or 'chat_invite_user_by_invitelink') in event.raw['object']['action']['type']:
                    mess = 'Привет ' + f'[id{event.obj.from_id}|{first_name}]' + '!' + ' Рады видеть тебя в наших рядах. Знакомься и вливайся в наш коллектив!'
                    send_message(peer_id, mess)
    except Exception as E:
        time.sleep(1)