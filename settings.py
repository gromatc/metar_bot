import os
from dataclasses import dataclass


def _load_dotenv_if_present() -> None:
    """
    Мягко подгружаем .env, если установлен python-dotenv.
    На сервере обычно используют переменные окружения, там .env не обязателен.
    """
    try:
        from dotenv import load_dotenv  # type: ignore
    except Exception:
        return

    load_dotenv()


@dataclass(frozen=True)
class Settings:
    bot_token: str
    metar_url_template: str
    taf_url_template: str
    vatsim_metar_url_template: str
    vatsim_taf_url_template: str


def get_settings() -> Settings:
    _load_dotenv_if_present()

    return Settings(
        bot_token=os.getenv("BOT_TOKEN", "").strip(),
        metar_url_template=os.getenv(
            "METAR_URL_TEMPLATE",
            "https://tgftp.nws.noaa.gov/data/observations/metar/stations/{icao}.TXT",
        ),
        taf_url_template=os.getenv(
            "TAF_URL_TEMPLATE",
            "https://tgftp.nws.noaa.gov/data/forecasts/taf/stations/{icao}.TXT",
        ),
        vatsim_metar_url_template=os.getenv(
            "VATSIM_METAR_URL_TEMPLATE",
            "https://metar.vatsim.net/metar/{icao}",
        ),
        vatsim_taf_url_template=os.getenv(
            "VATSIM_TAF_URL_TEMPLATE",
            "https://metar.vatsim.net/taf/{icao}",
        ),
    )


