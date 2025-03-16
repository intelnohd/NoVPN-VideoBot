import telebot
import os
import requests
import yt_dlp
from tikdan import Tikdan

# Указываем токен бота
TOKEN = "YOUR_TOKEN"
bot = telebot.TeleBot(TOKEN)

# Создаём экземпляр API Tikdan для работы с TikTok
tiktok_api = Tikdan.Api()

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "📥 Отправьте ссылку на видео (YouTube, TikTok, Instagram): ")

# Обработчик сообщений (принимает ссылки на YouTube, TikTok и Instagram)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text.strip()
    
    if "youtube.com" in url or "youtu.be" in url:
        download_youtube_video(message, url)
    elif "tiktok.com" in url:
        download_tiktok_video(message, url)
    elif "instagram.com" in url:
        download_instagram_video(message, url)
    else:
        bot.send_message(message.chat.id, "❌ Неверная ссылка!")

# Функция загрузки видео с YouTube
def download_youtube_video(message, url):
    try:
        bot.send_message(message.chat.id, "⏳ Загружаю видео с YouTube...")
        
        video_path = "youtube_video.mp4"
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': video_path,
            'merge_output_format': 'mp4',
            'quiet': True
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        bot.send_video(message.chat.id, open(video_path, 'rb'))
        os.remove(video_path)  # Удаляем видео после отправки
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка при обработке YouTube: {e}")

# Функция загрузки видео с TikTok
def download_tiktok_video(message, url):
    try:
        video_info = tiktok_api.export_video_info(url)
        download_url = video_info['download_url']
        
        bot.send_message(message.chat.id, "⏳ Загружаю видео с TikTok...")

        video_path = "tiktok_video.mp4"
        download_video(download_url, video_path)

        bot.send_video(message.chat.id, open(video_path, 'rb'))
        os.remove(video_path)  # Удаляем видео после отправки
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка при обработке TikTok: {e}")

# Функция загрузки видео с Instagram
def download_instagram_video(message, url):
    try:
        bot.send_message(message.chat.id, "⏳ Загружаю видео с Instagram...")

        video_path = "instagram_video.mp4"
        ydl_opts = {'outtmpl': video_path, 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        bot.send_video(message.chat.id, open(video_path, 'rb'))
        os.remove(video_path)  # Удаляем видео после отправки
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка при обработке Instagram: {e}")

# Функция скачивания видео по ссылке
def download_video(url, save_path):
    try:
        with requests.get(url, stream=True) as response:
            with open(save_path, "wb") as video_file:
                for chunk in response.iter_content(chunk_size=1024):
                    video_file.write(chunk)
    except Exception as e:
        print(f"Ошибка при загрузке видео: {e}")

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
