import pymysql

class RestoranlarDB:
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateRestaurantTB()
        self.InsertInitialData()

    def ConnectDB(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        self.c = self.db.cursor()

    def CreateDB(self):
        self.c.execute('''USE Talaba''')

    def CreateRestaurantTB(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS restoranlar(
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100),
                        address VARCHAR(200),
                        maxFoodPrice INT,
                        minFoodPrice INT,
                        employeesCount INT,
                        experience INT
                    )''')
        self.db.commit()

    def InsertInitialData(self):
        self.c.execute("TRUNCATE TABLE restoranlar")
        
        data = [
            ("Merw", "Chilonzor 3-kvartal", 150000, 35000, 25, 5),
            ("Minor", "Yunusobod 4-daha", 90000, 20000, 12, 3),
            ("Milliy Taomlar", "G'ofur G'ulom", 80000, 15000, 30, 8),
            ("Marvarid", "Mirobod tumani", 350000, 70000, 45, 12),
            ("Rayhon", "Shayxontohur", 120000, 25000, 60, 10),
            ("Maxler", "Sergeli 2-daha", 200000, 45000, 18, 4),
            ("Manzara", "Yashnobod", 500000, 100000, 50, 6),
            ("Monor", "Chorsu maydoni", 110000, 22000, 15, 2),
            ("Muzaffar", "Uchtepa", 75000, 18000, 10, 1),
            ("Mister", "Yakkasaroy", 180000, 40000, 22, 7)
        ]
        
        query = """INSERT INTO restoranlar (name, address, maxFoodPrice, minFoodPrice, employeesCount, experience) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        
        self.c.executemany(query, data)
        self.db.commit()
        print("10 ta restoran ma'lumotlari muvaffaqiyatli qo'shildi!")


    def bir(self):
        self.c.execute("SELECT name FROM restoranlar WHERE name LIKE 'M%%r' ORDER BY maxFoodPrice")
        print("\n1. M...r va o'sish tartibida:", self.c.fetchall())

    def ikki(self):
        self.c.execute("SELECT name FROM restoranlar ORDER BY minFoodPrice LIMIT 3")
        print("2. Eng arzon 3 ta:", self.c.fetchall())

    def uch(self):
        self.c.execute("SELECT name, maxFoodPrice FROM restoranlar ORDER BY experience DESC, maxFoodPrice DESC LIMIT 4")
        print("3. Tajribali va eng qimmat 4 ta:", self.c.fetchall())

r1 = RestoranlarDB()
r1.bir()
r1.ikki()
r1.uch()