SPENDINGS = [200, 250, 350, 400, 450, 500, 600, 750, 800, 900, 1000, 1250, 1300, 1500, 1600, 1750, 1800,
                   2000, 2200, 2400, 2500, 2600, 2800, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 
                   7500, 8000, 8500, 9000, 9500, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 17500, 
                   18000, 18500, 19000, 19500, 20000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 
                   3200, 3300, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000, 
                   6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 9200, 
                   9400, 9600, 9800, 10000]
DATES = ["01.01.2024", "02.01.2024", "03.01.2024", "04.01.2024", "05.01.2024", "06.01.2024", "07.01.2024", 
         "08.01.2024", "09.01.2024", "10.01.2024", "11.01.2024", "12.01.2024", "13.01.2024", "14.01.2024", 
         "15.01.2024", "16.01.2024", "17.01.2024", "18.01.2024", "19.01.2024", "20.01.2024", "21.01.2024", 
         "22.01.2024", "23.01.2024", "24.01.2024", "25.01.2024", "26.01.2024", "27.01.2024", "28.01.2024", 
         "29.01.2024", "30.01.2024", "31.01.2024", "01.02.2024", "02.02.2024", "03.02.2024", "04.02.2024", 
         "05.02.2024", "06.02.2024", "07.02.2024", "08.02.2024", "09.02.2024", "10.02.2024", "11.02.2024", 
         "12.02.2024", "13.02.2024", "14.02.2024", "15.02.2024", "16.02.2024", "17.02.2024", "18.02.2024", 
         "19.02.2024", "20.02.2024", "21.02.2024", "22.02.2024", "23.02.2024", "24.02.2024", "25.02.2024", 
         "26.02.2024", "27.02.2024", "28.02.2024", "29.02.2024", "01.03.2024", "02.03.2024", "03.03.2024", 
         "04.03.2024", "05.03.2024", "06.03.2024", "07.03.2024", "08.03.2024", "09.03.2024", "10.03.2024", 
         "11.03.2024", "12.03.2024", "13.03.2024", "14.03.2024", "15.03.2024", "16.03.2024", "17.03.2024", 
         "18.03.2024", "19.03.2024", "20.03.2024", "21.03.2024", "22.03.2024", "23.03.2024", "24.03.2024", 
         "25.03.2024", "26.03.2024", "27.03.2024", "28.03.2024", "29.03.2024", "30.03.2024", "31.03.2024", 
         "01.04.2025"]

EVENT_REASONS = ["Проживание в отеле", "Аренда автомобиля", "Такси до отеля", "Экскурсии и туры", 
                 
                "Посещение музеев", "Входные билеты на аттракционы", "Питание в ресторанах", "Уличная еда", 
                "Напитки", "Сувениры", "Одежда и аксессуары", "Местные деликатесы", 
                "Спасение на случай экстренной ситуации", "Чаевые", "Туристические страховки", 
                "Сим-карта для телефона", "Wi-Fi в гостинице", "Мобильный интернет", 
                "Памятные фотографии", "Экологические сборы", "Участие в мастер-классах", 
                "Живописные поездки", "Развлекательные мероприятия (концерты, спектакли)", 
                "Водные виды спорта", "Оренда спортивного снаряжения", "Билеты на транспорт внутри города",
                "Визовые сборы", "Авиаперевозки", "Платные туалеты", "Билеты на поезд", 
                "Водительские услуги", "Общественный транспорт", "Услуги гида", "Платные экскурсии", 
                "Артефакты и антиквариат", "Массаж и спа-процедуры", "Туристические группы", 
                "Культурные события", "Научные выставки", "Посещение аквапарков", "Картинг и ралли", 
                "Занятия йогой", "Полеты на воздушном шаре", "Восхождения и треккинг", "Услуги переводчика", 
                "Ограниченные выпуски товаров", "Местные праздники и фестивали", "Платные парковки", 
                "Билеты в планетарий", "Услуги уборки в отеле", "Чистка обуви", "Местные экскурсионные автобусы", 
                "Прокат велосипедов", "Заказ такси через приложения", "Кулинарные мастер-классы", 
                "Посещение виноделен", "Туры на рыбалку", "Аренда пляжного оборудования", 
                "Платные площадки для пикников", "Ночные клубы и бары", "Аксессуары для кемпинга", 
                "Плёнка для фотоаппарата", "Эмоциональные впечатления (плавание с дельфинами)", 
                "Спортивные билеты (футбол, хоккей)", "Зимние виды спорта", "Крафтовые товары местных ремесленников", 
                "Программы лояльности", "Платные местные телевидения и радиопередачи", 
                "Пенный вечеринка на пляже", "Дегустация местных напитков", "Пожа в групповых занятиях", 
                "Посещение художественной галереи", "Специальные сады и парки", 
                "Сертификаты на будущие покупки", "Специальные ужины", "Фитнес-залы и тренажерные залы", 
                "Безлимитный проездной на транспорт", "Местные курсы по языку", 
                "Услуги по обслуживанию домашних животных", "Оформление нотариальных документов", 
                "Эксклюзивные мероприятия для VIP", "Продукты местного фермерского рынка", 
                "Издержки на помощь местных жителей", "Посещение местных школ и университетов", 
                "Туры по историческим местам", "Путеводители и карты", "Озеленение частных участков", 
                "Поддержка местных НКО", "Пакетированные экскурсии с перелетом", 
                "Помощь в организации мероприятий", "Дополнительные ночи в отеле", "Медицинские услуги", 
                "Услуги консьержа", "Платный доступ в залы ожидания в аэропорту", "Помощь с оформлением налогов",
                "Премиум-класса услуги", "Услуги по организации свадеб", "Живописные туры по рекам", 
                "Билеты на театральные постановки"]
    
TICKET_RACES_ID = ["7L8nQm4a2D", "X3o5Wz9qR1", "J8eR4f6aB2", "Q2t1Kx5P0Z", "Y9cV8n3kW5", "H7mJ3v2Y6X", 
                   "A1dZ0q5rD8", "F5jN9b4K3P", "L2pW6e1N7C", "T8kA4v0X2Z", "K7uQ9t6F1H", "B5zC3g2W8D", 
                   "N1yE8p4X5K", "M5fT9l1R2Z", "U8sD4b3E9Q", "P6mA1c0Z5H", "O2gN7x8L4R", "S9fX3p2Y6W", 
                   "Q0jB8k4A1V", "E7tL2m3H8X", "W3cU5j9K1A", "H1nB7s8Y4D", "Z8lJ0k5Q2R", "X1qT4e3P9Y", 
                   "Y5dM2f6B0K", "S4tJ1n9L7C", "R7aN3q8X5E", "C1mW4h6D2V", "F8pK0g5T3Z", "K6tF8w1J5Q", 
                   "A2nH4j7K9R", "D5eW6p1X3T", "R9kX5b2V8M", "B3jD2f9T4Q", "Q1yZ8m3W6C", "N4sA3j0F8H", 
                   "T7qW1b2L5Z", "G6tX9k3D1A", "P0jD7c4H2K", "E8fK4y2N5W", "L2wY1h7Q4N", "X1jP8k3V6D", 
                   "Y4eF9t5C2R", "N6gK7p1B3H", "Q3yV5m4J8T", "H9aD2n0L1X", "C7nB8t5K3M", "W8pT1j9Y6R", 
                   "A5fG4k6C2Z", "M0jS3t7P9N", "O2dW6e4Y5Q", "F5tY9j1N3V", "R1mP2k8H4D", "B3yW6q9T1X", 
                   "T1jC5n8K2R", "L9kF2g3H7Q", "D5eR8w1T4N", "J7gY4n6K8M", "K0mT3j5P1Z", "E1bJ5k8D2Q", 
                   "I3yR8n2Q5F", "N9kT1w7W2L", "H7dJ6c3V8X", "R1bA4q5M9K", "P5gN2e8H3W", "Z4kS9f7Y2D", 
                   "C8tW3j1B5X", "F1yK2n4M9R", "L9rJ6q3H7D", "A7jE8g5N1T", "Y2kP5n3C8R", "H4dB0q9L3X", 
                   "M8nF1t7K2J", "V1gT4h5P3Y", "R9kJ2n8H6D", "P7bW3e1F0K", "K2cY5t9M7Q", "B3jR8w4D2T", 
                   "T5mG1n6L9P", "A8fD2k3X0R"]

TICKETS = ["100 Main St", "101 Oak Ave", "102 Maple Rd", "103 Pine Ct", "104 Cedar Blvd", "105 Elm St", 
                "106 Birch Ln", "107 Walnut Dr", "108 Spruce Way", "109 Ash Pl", "110 Willow St", 
                "111 Sycamore Ave", "112 Chestnut Rd", "113 Redwood Ct", "114 Fir Blvd", "115 Palm St", 
                "116 Dogwood Ln", "117 Magnolia Dr", "118 Cherry Way", "119 Fig Pl", "120 Lark St", 
                "121 Robin Ave", "122 Sparrow Rd", "123 Finch Ct", "124 Eagle Blvd", "125 Hawk St", 
                "126 Owl Ln", "127 Bluejay Dr", "128 Parrot Way", "129 Puffin Pl", "130 Lion Rd", 
                "131 Tiger Blvd", "132 Bear St", "133 Wolf Ct", "134 Fox Ave", "135 Lynx Ln", 
                "136 Cheetah Dr", "137 Puma Way", "138 Jaguar Pl", "139 Leopard Rd", "140 Dolphin St", 
                "141 Whale Ave", "142 Shark Rd", "143 Seal Ct", "144 Starfish Blvd", "145 Coral St", 
                "146 Shell Ln", "147 Seaweed Dr", "148 Tide Way", "149 Ocean Pl", "150 River St", 
                "151 Stream Dr", "152 Creek Ln", "153 Brook Ct", "154 Lagoon Blvd", "155 Bay St", 
                "156 Harbor Ave", "157 Coast Rd", "158 Island Ct", "159 Shore Blvd", "160 Mountain St", 
                "161 Hill Ave", "162 Valley Rd", "163 Plain Ct", "164 Plateau Blvd", "165 Cliff St", 
                "166 Peak Ln", "167 Summit Dr", "168 Ridge Way", "169 Canyon Pl", "170 Desert St", 
                "171 Oasis Ave", "172 Dune Rd", "173 Sand Ct", "174 Rock Blvd", "175 Earth St", 
                "176 Sky Ln", "177 Star Dr", "178 Cloud Way", "179 Moon Pl", "180 Sun St", "181 Light Ave", 
                "182 Bright Rd", "183 Shine Ct", "184 Glow Blvd", "185 Spark St", "186 Flame Ln", 
                "187 Ember Dr", "188 Ash Way", "189 Coal Pl","190 Fire Rd", "191 Heat Ct", "192 Warm Blvd", 
                "193 Cool St", "194 Breeze Ave", "195 Wind Rd", "196 Storm Ct", "197 Rain Blvd", 
                "198 Snow St", "199 Frost Ln"]

SERVER_MAIL_ADDRES = "syxapiki.team@mail.ru"
SERVER_MAIL_PASSWORD = "cverXMP9vSrmHsD7QfKc"