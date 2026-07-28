class MyDate:
    MONTHS = [
        "Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
        "Iyun", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"
    ]
    
    DAY_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day, month, year):
        if not self.isValidDate(day, month, year):
            raise ValueError("Noto'g'ri sana kiritildi")
        self.__day = day
        self.__month = month
        self.__year = year

    @staticmethod
    def isLeapYear(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def isValidDate(cls, day, month, year):
        if not (1 <= year <= 9999):
            return False
        if not (1 <= month <= 12):
            return False
            
        max_days = cls.DAY_IN_MONTHS[month - 1]
        if month == 2 and cls.isLeapYear(year):
            max_days = 29
            
        return 1 <= day <= max_days

    def setDate(self, day, month, year):
        if not self.isValidDate(day, month, year):
            raise ValueError("Noto'g'ri sana kiritildi")
        self.__day = day
        self.__month = month
        self.__year = year

    def nextDay(self):
        max_days = self.DAY_IN_MONTHS[self.__month - 1]
        if self.__month == 2 and self.isLeapYear(self.__year):
            max_days = 29

        if self.__day < max_days:
            self.__day += 1
        else:
            self.__day = 1
            if self.__month < 12:
                self.__month += 1
            else:
                self.__month = 1
                if self.__year < 9999:
                    self.__year += 1
                else:
                    raise ValueError("Yil chegaradan oshib ketdi")
        return self

    def previousDay(self):
        if self.__day > 1:
            self.__day -= 1
        else:
            if self.__month > 1:
                self.__month -= 1
            else:
                if self.__year > 1:
                    self.__year -= 1
                    self.__month = 12
                else:
                    raise ValueError("Yil chegaradan tushib ketdi")
            
            max_days = self.DAY_IN_MONTHS[self.__month - 1]
            if self.__month == 2 and self.isLeapYear(self.__year):
                max_days = 29
            self.__day = max_days
        return self

    def nextMonth(self):
        new_month = self.__month + 1 if self.__month < 12 else 1
        new_year = self.__year + 1 if self.__month == 12 else self.__year
        
        max_days = self.DAY_IN_MONTHS[new_month - 1]
        if new_month == 2 and self.isLeapYear(new_year):
            max_days = 29
            
        new_day = min(self.__day, max_days)
        
        if self.isValidDate(new_day, new_month, new_year):
            self.__day = new_day
            self.__month = new_month
            self.__year = new_year
        else:
            raise ValueError("Oy o'zgartirib bo'lmadi")
        return self

    def previousMonth(self):
        new_month = self.__month - 1 if self.__month > 1 else 12
        new_year = self.__year - 1 if self.__month == 1 else self.__year
        
        max_days = self.DAY_IN_MONTHS[new_month - 1]
        if new_month == 2 and self.isLeapYear(new_year):
            max_days = 29
            
        new_day = min(self.__day, max_days)
        
        if self.isValidDate(new_day, new_month, new_year):
            self.__day = new_day
            self.__month = new_month
            self.__year = new_year
        else:
            raise ValueError("Oy o'zgartirib bo'lmadi")
        return self

    def nextYear(self):
        new_year = self.__year + 1
        new_day = self.__day
        if self.__month == 2 and self.__day == 29 and not self.isLeapYear(new_year):
            new_day = 28
            
        if self.isValidDate(new_day, self.__month, new_year):
            self.__day = new_day
            self.__year = new_year
        else:
            raise ValueError("Yil o'zgartirib bo'lmadi")
        return self

    def previousYear(self):
        new_year = self.__year - 1
        new_day = self.__day
        if self.__month == 2 and self.__day == 29 and not self.isLeapYear(new_year):
            new_day = 28
            
        if self.isValidDate(new_day, self.__month, new_year):
            self.__day = new_day
            self.__year = new_year
        else:
            raise ValueError("Yil o'zgartirib bo'lmadi")
        return self

    def __str__(self):
        return f"{self.__day}-{self.MONTHS[self.__month - 1]} {self.__year} yil"

sana = MyDate(28, 2, 2012)
print("Boshlang'ich sana:", sana)
sana.nextDay()
print("Keyingi kun:", sana)
