import os
import smtplib
from dotenv import load_dotenv

load_dotenv('login_ya.env')



my_secret = os.environ['LOGIN']
my_secret_2 = os.environ['PASSWORD']

from_user = 'olesya.arhishina@yandex.ru'
to = 'oleska2601@yandex.ru'
subject = 'Приглашение!'
content_type = 'text/plain; charset="UTF-8";'

letter = '''From: {from_user}
To: {to}
Subject: {subject}
Content-Type: {content_type}

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''.format(from_user = from_user, to = to, subject = subject, content_type = content_type).replace('%website%', 'https://dvmn.org/referrals/3FEMQCyqLeT1ERyjjXroORu3UZ03sqbzHMhytFTW/').replace('%friend_name%', 'Иван').replace('%my_name%', 'Олеся')

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(my_secret, my_secret_2)
server.sendmail(my_secret, to, letter)
server.quit()


