"""
База аэропортов России и Европы
Формат: {ICAO: (название_ru, название_en)}
"""

AIRPORTS = {
    # ===================== РОССИЯ =====================
    # Москва и Московская область
    "UUEE": ("Шереметьево, Москва", "Sheremetyevo, Moscow"),
    "UUDD": ("Домодедово, Москва", "Domodedovo, Moscow"),
    "UUWW": ("Внуково, Москва", "Vnukovo, Moscow"),
    "UUBW": ("Жуковский, Москва", "Zhukovsky, Moscow"),
    
    # Санкт-Петербург
    "ULLI": ("Пулково, Санкт-Петербург", "Pulkovo, St. Petersburg"),
    
    # Юг России
    "URSS": ("Сочи (Адлер)", "Sochi (Adler)"),
    "URKK": ("Пашковский, Краснодар", "Pashkovsky, Krasnodar"),
    "URRR": ("Платов, Ростов-на-Дону", "Platov, Rostov-on-Don"),
    "URWW": ("Гумрак, Волгоград", "Gumrak, Volgograd"),
    "URWA": ("Астрахань", "Astrakhan"),
    "URMM": ("Минеральные Воды", "Mineralnye Vody"),
    "URML": ("Махачкала", "Makhachkala"),
    "URMO": ("Владикавказ", "Vladikavkaz"),
    "URKR": ("Симферополь", "Simferopol"),
    "URFF": ("Симферополь", "Simferopol"),
    
    # Поволжье
    "UWWW": ("Курумоч, Самара", "Kurumoch, Samara"),
    "UWKD": ("Казань", "Kazan"),
    "UWOO": ("Стригино, Нижний Новгород", "Strigino, Nizhny Novgorod"),
    "UWSS": ("Саратов (Гагарин)", "Saratov (Gagarin)"),
    "UWPS": ("Пенза", "Penza"),
    "UWUU": ("Уфа", "Ufa"),
    
    # Урал
    "USSS": ("Кольцово, Екатеринбург", "Koltsovo, Yekaterinburg"),
    "USCC": ("Челябинск", "Chelyabinsk"),
    "USPP": ("Большое Савино, Пермь", "Bolshoye Savino, Perm"),
    "USTТ": ("Рощино, Тюмень", "Roshchino, Tyumen"),
    "USRR": ("Сургут", "Surgut"),
    "USHH": ("Ханты-Мансийск", "Khanty-Mansiysk"),
    "USNN": ("Нижневартовск", "Nizhnevartovsk"),
    "USMM": ("Магнитогорск", "Magnitogorsk"),
    "USMU": ("Новый Уренгой", "Novy Urengoy"),
    
    # Сибирь
    "UNNT": ("Толмачёво, Новосибирск", "Tolmachevo, Novosibirsk"),
    "UNOO": ("Омск", "Omsk"),
    "UNKL": ("Емельяново, Красноярск", "Yemelyanovo, Krasnoyarsk"),
    "UIAA": ("Чита", "Chita"),
    "UIII": ("Иркутск", "Irkutsk"),
    "UIBB": ("Братск", "Bratsk"),
    "UNBB": ("Барнаул", "Barnaul"),
    "UNWW": ("Кемерово", "Kemerovo"),
    "UNEE": ("Абакан", "Abakan"),
    
    # Дальний Восток
    "UHWW": ("Кневичи, Владивосток", "Knevichi, Vladivostok"),
    "UHHH": ("Хабаровск (Новый)", "Khabarovsk (Novy)"),
    "UHSS": ("Хомутово, Южно-Сахалинск", "Khomutovo, Yuzhno-Sakhalinsk"),
    "UHPP": ("Елизово, Петропавловск-Камчатский", "Yelizovo, Petropavlovsk-Kamchatsky"),
    "UHMM": ("Магадан", "Magadan"),
    "UEEE": ("Якутск", "Yakutsk"),
    "UHMA": ("Анадырь", "Anadyr"),
    
    # Северо-Запад России
    "ULAA": ("Архангельск", "Arkhangelsk"),
    "ULMM": ("Мурманск", "Murmansk"),
    "ULOO": ("Псков", "Pskov"),
    "ULWW": ("Северный, Великий Новгород", "Severny, Veliky Novgorod"),
    "UUOK": ("Калининград (Храброво)", "Kaliningrad (Khrabrovo)"),
    "ULPB": ("Петрозаводск", "Petrozavodsk"),
    "USDD": ("Воркута", "Vorkuta"),
    
    # Центральная Россия
    "UUOO": ("Воронеж", "Voronezh"),
    "UUBC": ("Белгород", "Belgorod"),
    "UUBP": ("Брянск", "Bryansk"),
    "UUBL": ("Липецк", "Lipetsk"),
    "UUOR": ("Рязань", "Ryazan"),
    "UWSG": ("Ярославль", "Yaroslavl"),
    
    # ===================== ЕВРОПА =====================
    # Великобритания
    "EGLL": ("Хитроу, Лондон", "Heathrow, London"),
    "EGKK": ("Гатвик, Лондон", "Gatwick, London"),
    "EGSS": ("Станстед, Лондон", "Stansted, London"),
    "EGLC": ("Лондон-Сити", "London City"),
    "EGCC": ("Манчестер", "Manchester"),
    "EGBB": ("Бирмингем", "Birmingham"),
    "EGPH": ("Эдинбург", "Edinburgh"),
    "EGPF": ("Глазго", "Glasgow"),
    "EGGW": ("Лутон, Лондон", "Luton, London"),
    "EGGD": ("Бристоль", "Bristol"),
    "EGNX": ("Ист-Мидлендс", "East Midlands"),
    
    # Германия
    "EDDF": ("Франкфурт-на-Майне", "Frankfurt am Main"),
    "EDDM": ("Мюнхен", "Munich"),
    "EDDB": ("Берлин-Бранденбург", "Berlin Brandenburg"),
    "EDDL": ("Дюссельдорф", "Düsseldorf"),
    "EDDH": ("Гамбург", "Hamburg"),
    "EDDK": ("Кёльн/Бонн", "Cologne/Bonn"),
    "EDDS": ("Штутгарт", "Stuttgart"),
    "EDDP": ("Лейпциг/Галле", "Leipzig/Halle"),
    "EDDN": ("Нюрнберг", "Nuremberg"),
    "EDDW": ("Бремен", "Bremen"),
    "EDDC": ("Дрезден", "Dresden"),
    
    # Франция
    "LFPG": ("Шарль де Голль, Париж", "Charles de Gaulle, Paris"),
    "LFPO": ("Орли, Париж", "Orly, Paris"),
    "LFML": ("Марсель", "Marseille"),
    "LFLL": ("Лион", "Lyon"),
    "LFMN": ("Ницца", "Nice"),
    "LFBD": ("Бордо", "Bordeaux"),
    "LFBO": ("Тулуза", "Toulouse"),
    "LFRS": ("Нант", "Nantes"),
    "LFSB": ("Базель-Мюлуз", "Basel-Mulhouse"),
    "LFST": ("Страсбург", "Strasbourg"),
    
    # Испания
    "LEMD": ("Барахас, Мадрид", "Barajas, Madrid"),
    "LEBL": ("Эль-Прат, Барселона", "El Prat, Barcelona"),
    "LEPA": ("Пальма-де-Майорка", "Palma de Mallorca"),
    "LEMG": ("Малага", "Malaga"),
    "LEAL": ("Аликанте", "Alicante"),
    "LEVC": ("Валенсия", "Valencia"),
    "LEZL": ("Севилья", "Seville"),
    "LEBB": ("Бильбао", "Bilbao"),
    "LEST": ("Сантьяго-де-Компостела", "Santiago de Compostela"),
    "GCTS": ("Тенерифе Юг", "Tenerife South"),
    "GCLP": ("Гран-Канария", "Gran Canaria"),
    
    # Италия
    "LIRF": ("Фьюмичино, Рим", "Fiumicino, Rome"),
    "LIMC": ("Мальпенса, Милан", "Malpensa, Milan"),
    "LIME": ("Орио-аль-Серио, Бергамо", "Orio al Serio, Bergamo"),
    "LIPZ": ("Марко Поло, Венеция", "Marco Polo, Venice"),
    "LIRN": ("Неаполь", "Naples"),
    "LIML": ("Линате, Милан", "Linate, Milan"),
    "LIPE": ("Болонья", "Bologna"),
    "LICJ": ("Палермо", "Palermo"),
    "LICC": ("Катания", "Catania"),
    "LIRP": ("Пиза", "Pisa"),
    "LIPX": ("Верона", "Verona"),
    
    # Нидерланды
    "EHAM": ("Схипхол, Амстердам", "Schiphol, Amsterdam"),
    "EHRD": ("Роттердам", "Rotterdam"),
    "EHEH": ("Эйндховен", "Eindhoven"),
    
    # Бельгия
    "EBBR": ("Брюссель", "Brussels"),
    "EBCI": ("Шарлеруа", "Charleroi"),
    "EBAW": ("Антверпен", "Antwerp"),
    
    # Швейцария
    "LSZH": ("Цюрих", "Zurich"),
    "LSGG": ("Женева", "Geneva"),
    "LSZB": ("Берн", "Bern"),
    "LSZA": ("Лугано", "Lugano"),
    
    # Австрия
    "LOWW": ("Вена", "Vienna"),
    "LOWS": ("Зальцбург", "Salzburg"),
    "LOWG": ("Грац", "Graz"),
    "LOWI": ("Инсбрук", "Innsbruck"),
    
    # Польша
    "EPWA": ("Шопен, Варшава", "Chopin, Warsaw"),
    "EPKK": ("Краков", "Krakow"),
    "EPGD": ("Гданьск", "Gdansk"),
    "EPWR": ("Вроцлав", "Wroclaw"),
    "EPPO": ("Познань", "Poznan"),
    "EPKT": ("Катовице", "Katowice"),
    "EPMO": ("Модлин, Варшава", "Modlin, Warsaw"),
    
    # Чехия
    "LKPR": ("Вацлав Гавел, Прага", "Václav Havel, Prague"),
    "LKTB": ("Брно", "Brno"),
    "LKMT": ("Острава", "Ostrava"),
    
    # Венгрия
    "LHBP": ("Ференц Лист, Будапешт", "Ferenc Liszt, Budapest"),
    "LHDC": ("Дебрецен", "Debrecen"),
    
    # Скандинавия
    "EKCH": ("Каструп, Копенгаген", "Kastrup, Copenhagen"),
    "ESSA": ("Арланда, Стокгольм", "Arlanda, Stockholm"),
    "ENGM": ("Гардермуэн, Осло", "Gardermoen, Oslo"),
    "EFHK": ("Хельсинки-Вантаа", "Helsinki-Vantaa"),
    "ESGG": ("Гётеборг", "Gothenburg"),
    "ENBR": ("Берген", "Bergen"),
    "ENTC": ("Тромсё", "Tromsø"),
    "ENZV": ("Ставангер", "Stavanger"),
    "EFTU": ("Турку", "Turku"),
    "EFOU": ("Оулу", "Oulu"),
    "EKBI": ("Биллунн", "Billund"),
    "ESMS": ("Мальмё", "Malmö"),
    
    # Прибалтика
    "EVRA": ("Рига", "Riga"),
    "EETN": ("Таллин", "Tallinn"),
    "EYVI": ("Вильнюс", "Vilnius"),
    "EYKA": ("Каунас", "Kaunas"),
    
    # Греция
    "LGAV": ("Афины", "Athens"),
    "LGTS": ("Салоники", "Thessaloniki"),
    "LGIR": ("Ираклион, Крит", "Heraklion, Crete"),
    "LGKR": ("Корфу", "Corfu"),
    "LGSR": ("Санторини", "Santorini"),
    "LGMK": ("Миконос", "Mykonos"),
    "LGKO": ("Кос", "Kos"),
    "LGRP": ("Родос", "Rhodes"),
    
    # Турция (европейская часть)
    "LTFM": ("Стамбул", "Istanbul"),
    "LTFJ": ("Сабиха Гёкчен, Стамбул", "Sabiha Gökçen, Istanbul"),
    "LTAI": ("Анталья", "Antalya"),
    "LTFE": ("Даламан", "Dalaman"),
    "LTBJ": ("Измир", "Izmir"),
    "LTAC": ("Эсенбога, Анкара", "Esenboğa, Ankara"),
    "LTBS": ("Бодрум", "Bodrum"),
    
    # Португалия
    "LPPT": ("Лиссабон", "Lisbon"),
    "LPPR": ("Порту", "Porto"),
    "LPFR": ("Фару", "Faro"),
    "LPMA": ("Мадейра", "Madeira"),
    
    # Ирландия
    "EIDW": ("Дублин", "Dublin"),
    "EICK": ("Корк", "Cork"),
    "EINN": ("Шаннон", "Shannon"),
    
    # Румыния
    "LROP": ("Анри Коанда, Бухарест", "Henri Coandă, Bucharest"),
    "LRBS": ("Бэняса, Бухарест", "Băneasa, Bucharest"),
    "LRCL": ("Клуж-Напока", "Cluj-Napoca"),
    "LRTM": ("Тимишоара", "Timișoara"),
    
    # Болгария
    "LBSF": ("София", "Sofia"),
    "LBWN": ("Варна", "Varna"),
    "LBBG": ("Бургас", "Burgas"),
    
    # Сербия
    "LYBE": ("Белград", "Belgrade"),
    
    # Хорватия
    "LDZA": ("Загреб", "Zagreb"),
    "LDSP": ("Сплит", "Split"),
    "LDDU": ("Дубровник", "Dubrovnik"),
    
    # Словения
    "LJLJ": ("Любляна", "Ljubljana"),
    
    # Словакия
    "LZIB": ("Братислава", "Bratislava"),
    "LZKZ": ("Кошице", "Košice"),
    
    # Украина
    "UKBB": ("Борисполь, Киев", "Boryspil, Kyiv"),
    "UKKK": ("Жуляны, Киев", "Zhuliany, Kyiv"),
    "UKLL": ("Львов", "Lviv"),
    "UKOO": ("Одесса", "Odessa"),
    "UKDD": ("Днепр", "Dnipro"),
    "UKHH": ("Харьков", "Kharkiv"),
    
    # Беларусь
    "UMMS": ("Минск-2", "Minsk National"),
    "UMMM": ("Минск-1", "Minsk-1"),
    "UMGG": ("Гомель", "Gomel"),
    
    # Молдова
    "LUKK": ("Кишинёв", "Chișinău"),
    
    # Кипр
    "LCLK": ("Ларнака", "Larnaca"),
    "LCPH": ("Пафос", "Paphos"),
    
    # Мальта
    "LMML": ("Мальта", "Malta"),
    
    # Исландия
    "BIKF": ("Кефлавик, Рейкьявик", "Keflavík, Reykjavík"),
    
    # Люксембург
    "ELLX": ("Люксембург", "Luxembourg"),
    
    # Монако (используют Ниццу LFMN)
    
    # Грузия
    "UGTB": ("Тбилиси", "Tbilisi"),
    "UGSS": ("Сочи", "Sochi"),
    "UGKO": ("Кутаиси", "Kutaisi"),
    "URKA": ("Батуми", "Batumi"),
    
    # Армения
    "UDYZ": ("Звартноц, Ереван", "Zvartnots, Yerevan"),
    
    # Азербайджан
    "UBBB": ("Гейдар Алиев, Баку", "Heydar Aliyev, Baku"),
    
    # Казахстан (западная часть, ближе к Европе)
    "UAAA": ("Алматы", "Almaty"),
    "UACC": ("Астана", "Astana"),
    "UATE": ("Актау", "Aktau"),
    "UATG": ("Атырау", "Atyrau"),
}


def get_airport_name(icao: str) -> tuple[str, str]:
    """
    Возвращает название аэропорта по коду ИКАО.
    Возвращает (название_ru, название_en).
    Если аэропорт не найден, возвращает ("Неизвестный аэропорт", "Unknown airport").
    """
    icao = icao.upper().strip()
    return AIRPORTS.get(icao, ("Неизвестный аэропорт", "Unknown airport"))

