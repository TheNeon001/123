from telethon import TelegramClient, events
from telegram import Bot

api_id = 00000000
api_hash = "e185dbd4bd50b6a1f5640a0a50000000"
phone = "+0000000000"
bot_token = "7128578861:AAGq_MSwAo-YCcptQgOmuQD##########"  # Вставьте сюда токен вашего бота

# Создаем клиент Telegram
client = TelegramClient('session_name', api_id, api_hash)
bot = Bot(token=bot_token)

async def monitor_messages():
    # Определяем ключевые слова, по которым будем фильтровать сообщения
    ключевые_слова = ['ищу', "работа"]

    # Задаем список названий каналов для мониторинга
    целевые_каналы = ['КЛИЕНТЫ || РАБОТА ОНЛАЙН']

    @client.on(events.NewMessage)
    async def handler(event):
        try:
            if event.is_channel and event.chat:
                if event.chat.title in целевые_каналы:
                    for ключ in ключевые_слова:
                        if ключ.lower() in event.raw_text.lower():
                            имя_отправителя = event.sender.username if event.sender else "Нет имени пользователя"
                            сообщение = f'Новое сообщение в канале {event.chat.title}:\n'
                            сообщение += f'{имя_отправителя} написал(а): {event.raw_text}'
                            # Отправляем сообщение в чат-бот
                            await bot.send_message(chat_id=2072351966, text=сообщение)  # Замените YOUR_CHAT_ID на ID вашего чата
        except Exception as e:
            if "AuthKeyUnregisteredError" not in str(e):
                print(e)

    print("Старт мониторинга сообщений...")
    await client.run_until_disconnected()

async def main():
    # Запускаем мониторинг сообщений в фоновом режиме
    await monitor_messages()

# Запускаем клиент Telegram и основную программу
with client:
    client.loop.run_until_complete(main())
