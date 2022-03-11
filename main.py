from bs4 import BeautifulSoup
import requests
import telebot


bot = telebot.TeleBot('5173119245:AAH0U_iIkubcTHgW2K-K8iQayEkKVrB5MlA')
ivan = 445248738
anton = 365813198
anton_channel = -1001606988992
test_channel = -1001614329550


def get_latest_post():
    r = requests.get('https://vk.com/gisinalolstream')
    soup = BeautifulSoup(r.text, 'html.parser')
    with open('post.txt', 'r+') as f:
        latest_post_id = soup.find_all(class_='pi_author')[0]['data-post-id']
        if latest_post_id == f.readline():
            return 0
        f.seek(0)
        f.write(latest_post_id)

    post_strings = [repr(x).strip("'") for x in soup.find_all(class_='pi_text')[0].strings]
    s = ''
    flag = 0
    for row in post_strings:
        if row.startswith('https://') and flag == 0:
            s += '\n'
            flag = 1
        s += row + '\n'
    return s


if __name__ == '__main__':
    text = get_latest_post()
    if text != 0:
        bot.send_message(test_channel, text)
    else:
        bot.send_message(ivan, 'net novih')
