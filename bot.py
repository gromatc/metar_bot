import logging
import re
import html
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from settings import get_settings

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

settings = get_settings()


def validate_icao_code(code: str) -> bool:
    """Проверяет, что код соответствует формату ИКАО (4 буквы)"""
    pattern = r'^[A-Z]{4}$'
    return bool(re.match(pattern, code.upper()))


def get_airport_info(icao_code: str) -> tuple[str, str]:
    """
    Получает информацию об аэропорте (название и город)
    Возвращает кортеж (airport_name, city)
    """
    icao_code = icao_code.upper()
    
    try:
        # Попытка получить данные из aviationweather.gov API
        url = f"https://aviationweather.gov/api/airport/info/{icao_code}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            name = data.get('name', icao_code)
            city = data.get('city', '')
            return name, city
        
        # Fallback: расширенная база данных аэропортов
        airports_db = {
            # Россия
            'UUEE': ('Шереметьево', 'Москва'),
            'UUWW': ('Внуково', 'Москва'),
            'УУDD': ('Домодедово', 'Москва'),
            'UUDD': ('Домодедово', 'Москва'),
            'UUWW': ('Внуково', 'Москва'),
            'UUOB': ('Обь', 'Новосибирск'),
            'UNEE': ('Кольцово', 'Екатеринбург'),
            'UNII': ('Идрицево', 'Иркутск'),
            'UNVV': ('Соперское', 'Владивосток'),
            'UHLL': ('Лесное', 'Сочи'),
            'UUSU': ('Толмачёво', 'Новосибирск'),
            'UVVV': ('Сидоровичи', 'Вологда'),
            'UUWW': ('Внуково', 'Москва'),
            
            # Беларусь
            'UMKK': ('Минск Национальный', 'Минск'),
            'UMMS': ('Минск-2', 'Минск'),
            
            # Литва
            'EYVI': ('Вильнюс', 'Вильнюс'),
            'EYVL': ('Каунас', 'Каунас'),
            'EYKC': ('Паланга', 'Паланга'),
            
            # Польша
            'EPGD': ('Гданьск', 'Гданьск'),
            'EPWA': ('Шопен', 'Варшава'),
            'EPWU': ('Модлин', 'Варшава'),
            'EPKK': ('Балице', 'Краков'),
            'EPWR': ('Вроцлав', 'Вроцлав'),
            'EPPO': ('Пшеемысль', 'Пшеемысль'),
            'EPKT': ('Катовице', 'Катовице'),
            
            # Украина
            'UKBB': ('Борисполь', 'Киев'),
            'UKBK': ('Киев Жуляны', 'Киев'),
            'UKKK': ('Кировоград', 'Кировоград'),
            'UKOD': ('Одесса', 'Одесса'),
            'UKHH': ('Харьков', 'Харьков'),
            'UKDD': ('Днепр', 'Днепр'),
            
            # Казахстан
            'UUDD': ('Домодедово', 'Москва'),
            'UAKK': ('Алматы', 'Алматы'),
            'UACC': ('Нур-Султан', 'Нур-Султан'),
            'UATT': ('Атырау', 'Атырау'),
            
            # США
            'KORD': ('Chicago O\'Hare', 'Chicago'),
            'KJFK': ('JFK', 'New York'),
            'KLAX': ('LAX', 'Los Angeles'),
            'KATL': ('Hartsfield-Jackson', 'Atlanta'),
            'KDFW': ('Dallas/Fort Worth', 'Dallas'),
            'KDCA': ('Ronald Reagan', 'Washington DC'),
            
            # Европа
            'EGLL': ('London Heathrow', 'London'),
            'EGKK': ('Gatwick', 'London'),
            'LFPG': ('Paris Charles de Gaulle', 'Paris'),
            'EDDF': ('Frankfurt', 'Frankfurt'),
            'EDDM': ('Munich', 'Munich'),
            'LEMD': ('Madrid Barajas', 'Madrid'),
            'LIRF': ('Rome Fiumicino', 'Rome'),
            'LIRN': ('Rome Ciampino', 'Rome'),
            'LOWW': ('Vienna', 'Vienna'),
            'UUWW': ('Внуково', 'Moscow'),
            'LFPG': ('Charles de Gaulle', 'Paris'),
            'EGSS': ('Stansted', 'London'),
            'EHAM': ('Amsterdam', 'Amsterdam'),
            'KSFO': ('San Francisco', 'San Francisco'),
            
            # Другие
            'CYYZ': ('Toronto Pearson', 'Toronto'),
            'CYVR': ('Vancouver', 'Vancouver'),
            'KJFK': ('Kennedy', 'New York'),
            'ZBAA': ('Capital', 'Beijing'),
            'ZSPD': ('Pudong', 'Shanghai'),
        }
        
        if icao_code in airports_db:
            return airports_db[icao_code]
        
        return icao_code, ""
        
    except Exception as e:
        logger.error(f"Ошибка получения информации об аэропорте: {e}")
        return icao_code, ""


def get_metar_taf(icao_code: str) -> tuple[str, str]:
    """
    Получает METAR и TAF данные для указанного аэропорта
    Возвращает кортеж (metar, taf)
    """
    icao_code = icao_code.upper()
    
    try:
        metar_text = "Не удалось получить METAR"
        taf_text = "Не удалось получить TAF"

        # METAR (NOAA/NWS plain text)
        metar_url = settings.metar_url_template.format(icao=icao_code)
        metar_response = requests.get(metar_url, timeout=10)
        if metar_response.status_code == 200:
            lines = [line.strip() for line in metar_response.text.splitlines() if line.strip()]
            # Обычно: 1-я строка время, 2-я строка METAR
            if len(lines) >= 2:
                metar_text = lines[1]
            elif len(lines) == 1:
                metar_text = lines[0]
            else:
                metar_text = f"METAR для {icao_code} не найден"
        elif metar_response.status_code == 404:
            # fallback: VATSIM
            vatsim_metar_url = settings.vatsim_metar_url_template.format(icao=icao_code)
            vatsim_metar_resp = requests.get(vatsim_metar_url, timeout=10)
            if vatsim_metar_resp.status_code == 200 and vatsim_metar_resp.text.strip():
                # VATSIM обычно отдаёт одну строку
                metar_text = vatsim_metar_resp.text.strip().splitlines()[0].strip()
            else:
                metar_text = f"METAR для {icao_code} не найден"
        else:
            metar_text = f"Ошибка получения METAR (HTTP {metar_response.status_code})"
            logger.error(f"METAR HTTP {metar_response.status_code}: {metar_url}")

        # TAF (NOAA/NWS plain text)
        taf_url = settings.taf_url_template.format(icao=icao_code)
        taf_response = requests.get(taf_url, timeout=10)
        if taf_response.status_code == 200:
            lines = [line.strip() for line in taf_response.text.splitlines() if line.strip()]
            # Обычно: 1-я строка время, дальше TAF может быть в несколько строк
            if len(lines) >= 2:
                taf_text = " ".join(lines[1:])
            elif len(lines) == 1:
                taf_text = lines[0]
            else:
                taf_text = f"TAF для {icao_code} не найден"
        elif taf_response.status_code == 404:
            # fallback: VATSIM
            vatsim_taf_url = settings.vatsim_taf_url_template.format(icao=icao_code)
            vatsim_taf_resp = requests.get(vatsim_taf_url, timeout=10)
            if vatsim_taf_resp.status_code == 200 and vatsim_taf_resp.text.strip():
                # На всякий случай схлопнем переносы в одну строку (у нас inline `...`)
                taf_text = " ".join(vatsim_taf_resp.text.split())
            else:
                taf_text = f"TAF для {icao_code} не найден"
        else:
            taf_text = f"Ошибка получения TAF (HTTP {taf_response.status_code})"
            logger.error(f"TAF HTTP {taf_response.status_code}: {taf_url}")
        
        return metar_text, taf_text
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка запроса к API: {e}")
        return "Ошибка подключения к серверу погоды", "Ошибка подключения к серверу погоды"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    welcome_message = (
        "👋 Привет! Я бот для получения метеорологической информации об аэропортах.\n\n"
        "📝 Отправьте мне код аэропорта в формате ИКАО (4 буквы, например: UUEE, KORD, EGLL)\n"
        "и я пришлю вам актуальные данные METAR и TAF.\n\n"
        "Используйте /help для получения дополнительной информации."
    )
    await update.message.reply_text(welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /help"""
    help_text = (
        "ℹ️ Справка по использованию бота:\n\n"
        "📌 Формат кода аэропорта: ИКАО (4 заглавные буквы)\n"
        "Примеры: UUEE, KORD, EGLL, LFPG\n\n"
        "📋 Команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать эту справку\n\n"
        "💡 Просто отправьте код аэропорта, и бот вернет METAR и TAF данные."
    )
    await update.message.reply_text(help_text)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик текстовых сообщений"""
    user_message = update.message.text.strip().upper()
    
    # Проверяем, что сообщение соответствует формату ИКАО
    if not validate_icao_code(user_message):
        await update.message.reply_text(
            "❌ Неверный формат кода аэропорта.\n\n"
            "Пожалуйста, введите код в формате ИКАО (4 заглавные буквы).\n"
            "Примеры: UUEE, KORD, EGLL"
        )
        return
    
    # Отправляем сообщение о загрузке
    loading_message = await update.message.reply_text("⏳ Запрашиваю данные...")
    
    # Получаем информацию об аэропорте и METAR/TAF
    airport_name, city = get_airport_info(user_message)
    metar, taf = get_metar_taf(user_message)
    
    # Формируем ответ
    location_info = f"{airport_name}, {city}" if city else airport_name
    response = (
        f"✈️ <b>ICAO:</b> {html.escape(user_message)}\n"
        f"<b>Аэропорт:</b> {html.escape(location_info)}\n\n"
        f"🌤️ <b>METAR:</b>\n<code>{html.escape(metar)}</code>\n\n"
        f"📊 <b>TAF:</b>\n<code>{html.escape(taf)}</code>"
    )
    
    # Удаляем сообщение о загрузке и отправляем результат
    await loading_message.delete()
    await update.message.reply_text(response, parse_mode="HTML")


def main() -> None:
    """Запуск бота"""
    if not settings.bot_token:
        logger.error("BOT_TOKEN не задан. Задайте переменную окружения BOT_TOKEN (или .env для локального запуска).")
        return
    
    # Создаем приложение
    application = Application.builder().token(settings.bot_token).build()
    
    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    logger.info("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()

