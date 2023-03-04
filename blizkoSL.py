import os
from PIL import Image
import cv2
import streamlit as st

# Количество фотографий для съемки
NUM_IMAGES = 30

# Создаем директорию, если ее нет
if not os.path.exists('images'):
    os.makedirs('images')

# Инициализируем камеру
cap = cv2.VideoCapture(0)

# Создаем пустой список для хранения изображений
images = []

# Функция для отображения изображения в Streamlit
def show_image(image):
    img = Image.fromarray(image)
    st.image(img, channels="BGR")

# Функция для запуска съемки
def start_capture():
    # Запускаем цикл для съемки фотографий
    for i in range(NUM_IMAGES):
        # Захватываем изображение с камеры
        ret, frame = cap.read()

        # Отображаем изображение
        show_image(frame)

        # Сохраняем изображение в папке "images"
        filename = os.path.join('images', f'image_{i}.jpg')
        cv2.imwrite(filename, frame)

        # Добавляем изображение в список
        images.append(frame)

        # Ожидаем 500 мс между съемками фотографий
        cv2.waitKey(500)

    # Останавливаем камеру
    cap.release()

# Запускаем функцию для съемки
if st.button("Start"):
    start_capture()

# Обрабатываем список изображений, как в вашем текущем коде
