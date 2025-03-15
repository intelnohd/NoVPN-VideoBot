# Telegram Video Downloader Bot

## 📌 Описание

Этот бот позволяет скачивать видео из TikTok и Instagram напрямую в Telegram. Основная особенность — использование **Tikdan API** для скачивания видео из TikTok **без VPN**, что особенно полезно для стран, где TikTok заблокирован.

## ⚙️ Функциональность

- 📥 Скачивание видео из **TikTok** без водяного знака без использования VPN (благодаря **Tikdan API**)
- 📥 Скачивание видео из **Instagram**
- ⚡ Быстрая обработка и отправка видео напрямую в Telegram

## 🚀 Как использовать

1. Отправьте боту ссылку на видео из TikTok или Instagram.
2. Бот автоматически скачает видео и отправит вам в Telegram.

## 🛠 Технологии

- **Python** — основной язык
- **Telebot** — работа с Telegram API
- **yt-dlp** — загрузка видео из Instagram
- **Tikdan API** — обход блокировки TikTok и скачивание без VPN
- **Requests** — загрузка видео

## 🔧 Установка и запуск

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/yourusername/telegram-video-bot.git
   cd telegram-video-bot
   ```
2. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```
3. Запустите бота:
   ```sh
   python bot.py
   ```

## 🔑 Переменные окружения

Создайте файл `.env` и добавьте свой Telegram Bot Token:

```env
TOKEN=your-telegram-bot-token
```

##
