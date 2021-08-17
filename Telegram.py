import requests

#Get your bot token from BotFater bot in telegram
bot_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
base_url = "https://api.telegram.org/bot" + bot_token


def get_chat_id_from_user_name(username, last_updated_id):
    # Return chat id and last_updated_id
    # If username not subscribe return -1
    # subscribe by send any message to bot and then give user username to this method will return chat id
    # Store chat_id,update_id at any place to get next time data after that
    try:
        update = requests.get(base_url + "/getUpdates??offset=" + last_updated_id)
        data = update.json()["result"]
        for dt in data:
            if username == dt["message"]["chat"]["username"]:
                return dt["message"]["chat"]["id"], dt["update_id"]
        return -1, -1
    except KeyError as e:
        return -1, -1


def delete_webhook():
    res = requests.get(base_url + "/deleteWebhook")
    return res.json()["ok"]


def telegram_bot_sendmsg(chat_id, bot_message):
    send_text = base_url + '/sendMessage?chat_id=' + str(chat_id) + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


# karan-525616246
# First you need to send one message to your bot than pass your username and call get_chat_id_from_user_name
# You will get chat id along with update_id, save user chat_id in db,file for later use.  

chat_id, update_id = get_chat_id_from_user_name("shahkaran01", "-1")
# Save update_id any place and pass it in next call so will start get data after that

# Pass chat id and your message to be send to telegram_bot_sendmsg. will send message to your bot
res = telegram_bot_sendmsg("525616246", "Text Message")
print(res)
