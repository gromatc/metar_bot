"""
Пример конфигурационного файла
Скопируйте этот файл как config.py и замените YOUR_BOT_TOKEN_HERE на ваш токен
"""

# Токен бота от BotFather
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Источники данных (простые текстовые файлы NOAA/NWS)
METAR_URL_TEMPLATE = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/{icao}.TXT"
TAF_URL_TEMPLATE = "https://tgftp.nws.noaa.gov/data/forecasts/taf/stations/{icao}.TXT"

# Запасной источник (часто удобен, отдаёт plain text)
VATSIM_METAR_URL_TEMPLATE = "https://metar.vatsim.net/metar/{icao}"
VATSIM_TAF_URL_TEMPLATE = "https://metar.vatsim.net/taf/{icao}"

# (старый вариант через aviationweather.gov оставлен на будущее)
AVIATION_WEATHER_API = "https://aviationweather.gov/adds/dataserver_current/httpparam"

