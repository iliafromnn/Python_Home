import re

RE_USER = re.compile(r'(^[a-zA-z0-9\w]+)@([a-zA-z0-9]+\.+[a-z]+)')

# email = 'ilyafromnn@gmail.com'
# print(RE_USER.match(email))

def user_email(email):
    user_info = RE_USER.findall(email)[0]
    if user_info:
        name, adress = user_info
        print(name, adress)
    else:
        raise ValueError(f'enter wrong email {email}')

mail = 'gusev_ilia@mail.ru'

user_email(mail)