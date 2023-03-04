import subprocess

def handle_start(message):
    # запускаем первый скрипт
    subprocess.run(['python', '/Users/baichorovboris/PycharmProjects/image2/blizko.py'], wait=True)
    # запускаем второй скрипт после того, как первый закончится
    subprocess.run({'python', '/Users/baichorovboris/PycharmProjects/image2/image.py'})


