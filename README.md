# Telegram Shop Bot

Телеграм-бот-магазин с 17 товарами в формате: **название | вес | цена**.

## 🚀 Как развернуть на Render

1. Создай новый репозиторий на GitHub и закинь туда файлы (`bot.py`, `requirements.txt`, `README.md`).
2. Зайди на [Render](https://render.com).
3. Создай **New Web Service** → выбери свой репозиторий.
4. В настройках:
   - **Runtime**: Python 3
   - **Start Command**: python bot.py
5. В **Environment Variables** добавь:
   - TOKEN = твой токен от @BotFather
   - ADMIN_CHAT_ID = твой Telegram ID
6. Нажми Deploy ✅

Бот будет работать 24/7.
