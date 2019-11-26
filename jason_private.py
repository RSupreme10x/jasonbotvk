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
    2000000001, # Литература Light
    2000000017, # Литература Standart
    2000000018, # Литература PRO

    2000000016, # Информатика Light
    2000000014, # Информатика Standart
    2000000015, # Информатика PRO

    2000000013, # Химия Light
    2000000012, # Химия Standart
    2000000011, # Химия PRO
    2000000035, # Химия PRO 2

    2000000010, # Обществознание Light
    2000000043, # Обществознание Light 2
    2000000050, # Обществознание Light 3
    2000000009, # Обществознание Standart
    2000000042, # Обществознание Standart 2
    2000000008, # Обществознание PRO
    2000000041, # Обществознание PRO 2

    2000000003, # История Light
    2000000037, # История Light 2
    2000000004, # История Standart
    2000000036, # История Standart 2
    2000000002, # История PRO
    2000000038, # История PRO 2

    2000000007, # Биология Light
    2000000039, # Биология Light 2
    2000000006, # Биология Standart
    2000000005, # Биология PRO

    2000000030, # Физика Light
    2000000029, # Физика Standart
    2000000028, # Физика PRO
    2000000044, # Физика PRO 2

    2000000027, # Математика Light
    2000000025, # Математика Standart
    2000000026, # Математика PRO

    2000000024, # Русский язык Light
    2000000034, # Русский язык Light 2
    2000000023, # Русский язык Standart
    2000000045, # Русский язык Standart 2
    2000000021, # Русский язык PRO
    2000000040, # Русский язык PRO 2

    2000000022, # Английский язык Light
    2000000020, # Английский Standart
    2000000019, # Английский PRO
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
    2000000001, # Литература Light
    2000000017, # Литература Standart
    2000000018, # Литература PRO
]
ids_inf = [
    2000000016, # Информатика Light
    2000000014, # Информатика Standart
    2000000015, # Информатика PRO
]
ids_chem = [
    2000000013, # Химия Light
    2000000012, # Химия Standart
    2000000011, # Химия PRO
    2000000035, # Химия PRO 2
    2000000049, # Спецкурс по 30-32 заданиям. Лайт
    2000000048, # Спецкурс по 30-32 заданиям. Про
]
ids_ss = [
    2000000010, # Обществознание Light
    2000000043, # Обществознание Light 2
    2000000050, # Обществознание Light 3
    2000000009, # Обществознание Standart
    2000000042, # Обществознание Standart 2
    2000000008, # Обществознание PRO
    2000000041, # Обществознание PRO 2
]
ids_hist = [
    2000000003, # История Light
    2000000037, # История Light 2
    2000000004, # История Standart
    2000000036, # История Standart 2
    2000000002, # История PRO
    2000000038, # История PRO 2
]
ids_bio = [
    2000000007, # Биология Light
    2000000039, # Биология Light 2
    2000000006, # Биология Standart
    2000000005, # Биология PRO
]
ids_phys = [
    2000000030, # Физика Light
    2000000029, # Физика Standart
    2000000028, # Физика PRO
    2000000044, # Физика PRO 2
]
ids_math = [
    2000000027, # Математика Light
    2000000025, # Математика Standart
    2000000026, # Математика PRO
]
ids_rus = [
    2000000024, # Русский язык Light
    2000000034, # Русский язык Light 2
    2000000023, # Русский язык Standart
    2000000045, # Русский язык Standart 2
    2000000021, # Русский язык PRO
    2000000040, # Русский язык PRO 2
]
ids_eng = [
    2000000022, # Английский язык Light
    2000000020, # Английский Standart
    2000000019, # Английский PRO
]
ids_soch = [
    2000000047, # Итоговое сочинение Лайт
    2000000046, # Итоговое сочинение Стандарт
]
# ССЫЛКИ
link_lit = 'https://thenewschool.clickmeeting.com/tusa-literatorov'
link_inf = 'https://thenewschool.clickmeeting.com/demopotok-po-informatike'
link_chem = 'https://thenewschool.clickmeeting.com/ge-ni-u-se-s'
link_ss = 'https://thenewschool.clickmeeting.com/obschestvostaika-tusit-tut'
link_hist = 'https://thenewschool.clickmeeting.com/lalala'
link_bio = 'https://thenewschool.clickmeeting.com/biologiya-takaya-biologiya'
link_phys = 'https://thenewschool.clickmeeting.com/fizika'
link_math = 'https://thenewschool.clickmeeting.com/matematika-na-meste'
link_rus = 'https://thenewschool.clickmeeting.com/velikii-russkii-yazik'
link_eng = 'https://thenewschool.clickmeeting.com/london-is-the-capital-of-gb'
link_noon = 'https://vk.cc/9O13cN'
link_soch = 'https://thenewschool.clickmeeting.com/itogovoe-sochinenie'

# PASSWORDS
pw_lit = '2552160'
pw_inf = 'loveNS123'
pw_chem = 'Мимимицин'
pw_ss = 'все-сможем'
pw_hist = 'все-сможем'
pw_bio = 'инфузория-туфелька'
pw_phys = 'tnsphyskek'
pw_math = 'mathmath'
pw_rus = 'ясоздаюлучшуюверсиюсебя'
pw_eng = 'english100'
pw_soch = 'яумничкауменявсеполучится'

# MOBILE PASSWORDS
mob_lit = '755-579-928'
mob_inf = '837-386-749'
mob_chem = '594-727-252'
mob_ss = '149-674-923'
mob_hist = '421-913-171'
mob_bio = '722-129-484'
mob_phys = '619-825-826'
mob_math = '172-717-167'
mob_rus = '919-953-459'
mob_eng = '528-188-298'
mob_soch = '868-225-714'

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

        message = 'Привет, ребята! Сегодня будет вебинар. Всех жду. Ссылку на веб отправлю за 10 мин до начала.'
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

        message = 'Вебинар уже через час. Настраиваемся на работу и печатаем скрипт (он в группе).'
        for member_id in members_ids:
            if len(message) >= 4000:
                send_message(peer_id, message)
                message = 'Next: '
            message += f'[id{member_id}|.]'
        send_message(peer_id, message)


def Minute(links, ids, pw, mob):
    for peer_id in ids:
        members = vk.messages.getConversationMembers(
            peer_id = peer_id,
        )['items']

        members_ids = [member['member_id'] for member in members if member['member_id'] > 0]

        message = 'Начинаем занятие через 10 минут. Погнали! \nСсылка на веб: ' + links + '\nID для мобилы: ' + mob +'\nПароль: ' + pw + '\n'
        for member_id in members_ids:
            if len(message) >= 4000:
                send_message(peer_id, message)
                message = 'Next: '
            message += f'[id{member_id}|.]'
        send_message(peer_id, message)

def Minute_sunday(links, ids):
    for peer_id in ids:
        members = vk.messages.getConversationMembers(
            peer_id = peer_id,
        )['items']

        members_ids = [member['member_id'] for member in members if member['member_id'] > 0]

        message = 'Начинаем занятие через 10 минут. Погнали! \nСсылка на веб: ' + links + '\n'
        for member_id in members_ids:
            if len(message) >= 4000:
                send_message(peer_id, message)
                message = 'Next: '
            message += f'[id{member_id}|.]'
        send_message(peer_id, message)

# ЧАСОВОЙ ПОЯС -3
def scheduler() -> None:
# ПОНЕДЕЛЬНИК
    # УТРО
    schedule.every().monday.at('05:00').do(Morning, ids_eng) # Английский
    schedule.every().monday.at('05:00').do(Morning, ids_rus) # Русский язык
    schedule.every().monday.at('05:00').do(Morning, ids_lit) # Литература
    # ЗА ЧАС ДО ВЕБИНАРА
    schedule.every().monday.at('12:00').do(OneHour, ids_eng) # Английский
    schedule.every().monday.at('13:30').do(OneHour, ids_rus) # Русский язык
    schedule.every().monday.at('15:00').do(OneHour, ids_lit) # Литература
    # ЗА 10 МИНУТ ДО ВЕБИНАРА
    schedule.every().monday.at('12:50').do(Minute, link_eng, ids_eng, pw_eng, mob_eng) # Английский
    schedule.every().monday.at('14:20').do(Minute, link_rus, ids_rus, pw_rus, mob_rus) # Русский язык
    schedule.every().monday.at('15:50').do(Minute, link_lit, ids_lit, pw_lit, mob_lit) # Литература
# ВТОРНИК
    # УТРО
    schedule.every().tuesday.at('05:00').do(Morning, ids_inf) # Информатика
    schedule.every().tuesday.at('05:00').do(Morning, ids_phys) # Физика
    schedule.every().tuesday.at('05:00').do(Morning, ids_math) # Математика
    # ЗА ЧАС ДО ВЕБИНАРА
    schedule.every().tuesday.at('12:00').do(OneHour, ids_inf) # Информатика
    schedule.every().tuesday.at('13:30').do(OneHour, ids_math) # Математика
    schedule.every().tuesday.at('15:00').do(OneHour, ids_phys) # Физика
    # ЗА 10 МИНУТ ДО ВЕБИНАРА
    schedule.every().tuesday.at('12:50').do(Minute, link_inf, ids_inf, pw_inf, mob_inf) # Информатика
    schedule.every().tuesday.at('14:20').do(Minute, link_math, ids_math, pw_math, mob_math) # Математика
    schedule.every().tuesday.at('15:50').do(Minute, link_phys, ids_phys, pw_phys, mob_phys) # Физика
# СРЕДА
    # УТРО
    schedule.every().wednesday.at('05:00').do(Morning, ids_hist) # История
    schedule.every().wednesday.at('05:00').do(Morning, ids_chem) # Химия
    schedule.every().wednesday.at('05:00').do(Morning, ids_ss) # Обществознание
    schedule.every().wednesday.at('05:00').do(Morning, ids_bio) # Биология
    # ЗА ЧАС ДО ВЕБИНАРА
    schedule.every().wednesday.at('12:00').do(OneHour, ids_hist) # История
    schedule.every().wednesday.at('12:00').do(OneHour, ids_chem) # Химия
    schedule.every().wednesday.at('13:30').do(OneHour, ids_ss) # Обществознание
    schedule.every().wednesday.at('15:00').do(OneHour, ids_bio) # Биология
    # ЗА 10 МИНУТ ДО ВЕБИНАРА
    schedule.every().wednesday.at('12:50').do(Minute, link_hist, ids_hist, pw_hist, mob_hist) # История
    schedule.every().wednesday.at('12:50').do(Minute, link_chem, ids_chem, pw_chem, mob_chem) # Химия
    schedule.every().wednesday.at('14:20').do(Minute, link_ss, ids_ss, pw_ss, mob_ss) # Обществознание
    schedule.every().wednesday.at('15:50').do(Minute, link_bio, ids_bio, pw_bio, mob_bio) # Биология
# ЧЕТВЕРГ
    # УТРО
    schedule.every().thursday.at('05:00').do(Morning, ids_eng) # Английский
    schedule.every().thursday.at('05:00').do(Morning, ids_lit) # Литература
    schedule.every().thursday.at('05:00').do(Morning, ids_phys) # Физика
    # ЗА ЧАС ДО ВЕБИНАРА
    schedule.every().thursday.at('12:00').do(OneHour, ids_eng) # Английский
    schedule.every().thursday.at('13:30').do(OneHour, ids_lit) # Литература
    schedule.every().thursday.at('15:00').do(OneHour, ids_phys) # Физика
    # ЗА 10 МИНУТ ДО ВЕБИНАРА
    schedule.every().thursday.at('12:50').do(Minute, link_eng, ids_eng, pw_eng, mob_eng) # Английский
    schedule.every().thursday.at('14:20').do(Minute, link_lit, ids_lit, pw_lit, mob_lit) # Литература
    schedule.every().thursday.at('15:50').do(Minute, link_phys, ids_phys, pw_phys, mob_phys) # Физика
# ПЯТНИЦА
    # УТРО
    schedule.every().friday.at('05:00').do(Morning, ids_hist) # История
    schedule.every().friday.at('05:00').do(Morning, ids_chem) # Химия
    schedule.every().friday.at('05:00').do(Morning, ids_rus) # Русский язык
    schedule.every().friday.at('05:00').do(Morning, ids_inf) # Информатика
    # ЗА ЧАС ДО ВЕБИНАРА
    schedule.every().friday.at('12:00').do(OneHour, ids_hist) # История
    schedule.every().friday.at('12:00').do(OneHour, ids_chem) # Химия
    schedule.every().friday.at('13:30').do(OneHour, ids_rus) # Русский язык
    schedule.every().friday.at('15:00').do(OneHour, ids_inf) # Информатика
    # ЗА 10 МИНУТ ДО ВЕБИНАРА
    schedule.every().friday.at('12:50').do(Minute, link_hist, ids_hist, pw_hist, mob_hist) # История
    schedule.every().friday.at('12:50').do(Minute, link_chem, ids_chem, pw_chem, mob_chem) # Химия
    schedule.every().friday.at('14:20').do(Minute, link_rus, ids_rus, pw_rus, mob_rus) # Русский язык
    schedule.every().friday.at('15:50').do(Minute, link_inf, ids_inf, pw_inf, mob_inf) # Информатика
# СУББОТА
    # УТРО
    schedule.every().saturday.at('05:00').do(Morning, ids_bio) # Биология
    schedule.every().saturday.at('05:00').do(Morning, ids_math) # Математика
    schedule.every().saturday.at('05:00').do(Morning, ids_ss) # Обществознание
    schedule.every().saturday.at('05:00').do(Morning, ids_soch) # Итоговое сочинение
    # ЗА ЧАС ДО ВЕБИНАРА
    schedule.every().saturday.at('12:00').do(OneHour, ids_bio) # Биология
    schedule.every().saturday.at('13:30').do(OneHour, ids_math) # Математика
    schedule.every().saturday.at('15:00').do(OneHour, ids_ss) # Обществознание
    schedule.every().saturday.at('13:45').do(OneHour, ids_soch) # Итоговое сочинение
    # ЗА 10 МИНУТ ДО ВЕБИНАРА
    schedule.every().saturday.at('12:50').do(Minute, link_bio, ids_bio, pw_bio, mob_bio) # Биология
    schedule.every().saturday.at('14:20').do(Minute, link_math, ids_math, pw_math, mob_math) # Математика
    schedule.every().saturday.at('15:50').do(Minute, link_ss, ids_ss, pw_ss, mob_ss) # Обществознание
    schedule.every().saturday.at('14:35').do(Minute, link_soch, ids_soch, pw_soch, mob_soch) # Итоговое сочинение


# ВОСКРЕСЕНЬЕ
    # УТРО
    schedule.every().sunday.at('05:00').do(Morning, ids_inf) # Информатика
    schedule.every().sunday.at('05:00').do(Morning, ids_hist) # История
    schedule.every().sunday.at('05:00').do(Morning, ids_lit) # Литература
    schedule.every().sunday.at('05:00').do(Morning, ids_bio) # Биология
    schedule.every().sunday.at('05:00').do(Morning, ids_math) # Математика
    schedule.every().sunday.at('05:00').do(Morning, ids_chem) # Химия
    schedule.every().sunday.at('05:00').do(Morning, ids_ss) # Обществознание
    schedule.every().sunday.at('05:00').do(Morning, ids_phys) # Физика
    schedule.every().sunday.at('05:00').do(Morning, ids_eng) # Английский
    schedule.every().sunday.at('05:00').do(Morning, ids_rus) # Русский
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
    schedule.every().sunday.at('06:50').do(Minute_sunday, link_noon, ids_inf) # Информатика
    schedule.every().sunday.at('07:50').do(Minute_sunday, link_noon, ids_hist) # История
    schedule.every().sunday.at('08:50').do(Minute_sunday, link_noon, ids_lit) # Литература
    schedule.every().sunday.at('09:50').do(Minute_sunday, link_noon, ids_bio) # Биология
    schedule.every().sunday.at('10:50').do(Minute_sunday, link_noon, ids_math) # Математика
    schedule.every().sunday.at('11:50').do(Minute_sunday, link_noon, ids_chem) # Химия
    schedule.every().sunday.at('12:50').do(Minute_sunday, link_noon, ids_ss) # Обществознание
    schedule.every().thursday.at('13:50').do(Minute, link_phys, ids_phys, pw_phys, mob_phys) # Физика
    schedule.every().sunday.at('14:50').do(Minute_sunday, link_noon, ids_eng) # Английский
    schedule.every().sunday.at('15:50').do(Minute_sunday, link_noon, ids_rus) # Русский

    while True:
        schedule.run_pending()
        sleep(1)

t = Thread(target=scheduler)
t.start()


# ///////////////////////////////////////////////////////// Конец планировщика /////////////////////////////////////////////////////////


#JASON PRIVATE
accessToken = '460384f147d2d4e2900af5ef70b10f9c33e3997e840b76c6bfcf5b80714721583b0560a12bcc15b98fc27'
groupId = 186083531

# CHRISTOPHER
# accessToken = '056f6934f2d0f51392d435b4565c67fb67969f2c56891037bfa1dcbfc551a2bacc827b69a16e202143c4c'
# groupId = 186719960

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
                    mess = 'Привет ' + f'[id{event.obj.from_id}|{first_name}]' + '!' + ' Рады видеть тебя в наших рядах. Читай закрепленное сообщение и вливайся!'
                    send_message(peer_id, mess)
    except Exception as E:
        time.sleep(1)