import os
from bot import bot_start

def main():
    if not os.path.isdir('no_bg_photos'):
        os.mkdir('no_bg_photos')
    if not os.path.isdir('original_photos'):
        os.mkdir('original_photos')
    bot_token = os.environ.get('bot_token')
    bot_start(bot_token)
if __name__ == '__main__':
    main()
