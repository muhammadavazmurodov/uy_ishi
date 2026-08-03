# def majority_element(nums: list) -> int:
#     if not nums:
#         return -1
#     dct = {}
#     for i in nums:
#         dct[i] = dct.get(i, 0) + 1
#     return max(dct, key=dct.get)

# nums = [2, 2, 1, 1, 1, 2, 2]
# print(majority_element(nums))

# ....

# def search_by_genre(cinema: list, genre: str) -> list:
#     return [i for i in cinema if i.get("genre") == genre]

# cinema = [
#     {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#     {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
#     {"title": "Oq yo‘l", "genre": "Drama", "price": 25000},
#     {"title": "Dune", "genre": "Fantastika", "price": 35000}
# ]
# print(search_by_genre(cinema, "Fantastika"))
    
# ....

# CREATE DATABASE transport_routes_db;
# USE transport_routes_db;

# CREATE TABLE routes (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     route_number VARCHAR(10) NOT NULL,
#     start_point VARCHAR(50) NOT NULL,
#     end_point VARCHAR(50) NOT NULL,
#     duration_min INT NOT NULL,
#     distance_km DECIMAL(5,1) NOT NULL,
#     ticket_price DECIMAL(7,2) NOT NULL, -- Jadvalda DECIMAL(5,2) yozilgan, lekin 1800.00 kabi narxlar sig'ishi uchun DECIMAL(7,2) tavsiya etiladi
#     bus_type VARCHAR(20) NOT NULL
# );

# INSERT INTO routes (route_number, start_point, end_point, duration_min, distance_km, ticket_price, bus_type) VALUES
# ('12', 'Chilonzor', 'Yunusobod', 45, 15.5, 1800.00, 'Shahar'),
# ('21A', 'Sergeli', 'Vokzal', 35, 12.0, 1800.00, 'Shahar'),
# ('75', 'Qo''yliq', 'Do''stlik', 25, 8.5, 1400.00, 'Elektr'),
# ('101', 'Tashkent', 'Samarkand', 240, 300.0, 95000.00, 'Tezyurar'),
# ('55', 'Oloy bozori', 'Chorsu', 20, 5.2, 1400.00, 'Elektr'),
# ('99', 'Beruniy', 'TTZ', 50, 18.3, 1800.00, 'Shahar'),
# ('44', 'Karvon', 'Uchtepa', 40, 14.1, 1800.00, 'Shahar'),
# ('110', 'Tashkent', 'Bukhara', 360, 550.0, 95000.00, 'Tezyurar'),
# ('88', 'Chilonzor', 'Bodomzor', 32, 11.4, 1800.00, 'Shahar'),
# ('14', 'Aeroport', 'Mingo''rik', 15, 6.0, 1400.00, 'Elektr');

# SELECT * FROM routes 
# ORDER BY ticket_price ASC;

# SELECT * FROM routes 
# ORDER BY distance_km DESC 
# LIMIT 3;

# SELECT * FROM routes 
# WHERE duration_min > 30 AND bus_type = 'Shahar';

# SELECT bus_type, AVG(ticket_price) AS average_price 
# FROM routes 
# GROUP BY bus_type;

