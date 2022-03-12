from bs4 import BeautifulSoup
import requests
import telebot
from PIL import Image
from io import BytesIO
from settings import settings


bot = telebot.TeleBot(settings['token'])


def get_latest_post():
    r = requests.get(settings['group'])
    soup = BeautifulSoup(r.text, 'html.parser')
    with open('/Users/ivan/PycharmProjects/anton_bot/post.txt', 'r+') as f:
        latest_post = soup.find(class_='wall_item')
        latest_post_id = latest_post.find('a', class_='pi_author')['data-post-id']
        f.seek(0)
        if latest_post_id == f.readline():
            return None, None
        f.seek(0)
        f.truncate()
        f.write(latest_post_id)

    post_strings = [repr(x).strip("'") for x in latest_post.find(class_='pi_text').strings]
    s = ''
    flag = 0
    for row in post_strings:
        if row.startswith('https://') and flag == 0:
            s += '\n'
            flag = 1
        s += row + '\n'

    try:
        img_source = latest_post.find('div', class_='thumb_map_img_as_div')['data-src_big']
        r2 = requests.get(img_source)
        i = Image.open(BytesIO(r2.content))
        img_path = settings['img_path']
        i.save(img_path)
    except TypeError:
        img_path = None
    finally:
        return s, img_path


if __name__ == '__main__':
    text, image = get_latest_post()
    if text:
        bot.send_message(settings['channel'], text)
    if image:
        with open(image, 'rb') as f:
            bot.send_photo(settings['channel'], f)

