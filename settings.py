DEBUG = False


token_prod = '5173119245:AAH0U_iIkubcTHgW2K-K8iQayEkKVrB5MlA'
token_test = '5222693840:AAE5XhxZ250vaAdwVPexqP8RWWjvCGSjMnY'
ivan = 445248738
anton = 365813198
channel_prod = -1001606988992
channel_test = -1001614329550
group_prod = 'https://vk.com/gisinalolstream'
group_test = 'https://vk.com/club211430881'
path_test = '/Users/ivan/Library/Application Support/JetBrains/PyCharm2021.3/scratches/test.jpg'
path_prod = '/opt/anton_bot/post_pic.jpg'

if DEBUG:
    settings = {
        'token': token_test,
        'channel': channel_test,
        'group': group_test,
        'img_path': path_test
    }
else:
    settings = {
        'token': token_prod,
        'channel': channel_prod,
        'group': group_prod,
        'img_path': path_prod
    }
