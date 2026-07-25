# class User:
#     def __init__(self, name, email, address):
#         self.name = name
#         self.email = email
#         self.adress = address
#     def get_name(self):
#         return self.name
#     def get_email(self):
#         return self.email
#     def get_address(self):
#         return self.address
#     def set_address(self, new_address):
#         self.address = new_address
#     def __str__(self):
#         return f"User: {self.name} <{self.email}>"

# # u1 = User("user1","user1@gamil.com","Toshkent")
# # print(u1) 
# # u1.set_address("Neww")
# # print(u1.get_address())




# class Customer(User):
#     def __init__(self, name, email, address, balance):
#         super().__init__(name, email, address)
#         self.balance = balance
#         self.cart = []
#     def add_to_cart(self, product, qty, price):
#         if qty > 0 and price >= 0:
#             mahsulot_malumoti = (product, qty, price)
#             self.cart.append(mahsulot_malumoti)
#     def clear_cart(self):
#         self.cart = []
#     def get_cart_total(self):
#         jami_pul = 0
#         for i in self.cart:
#             nomi = i[0]
#             soni = i[1]
#             narxi = i[2]
#             jami_pul = jami_pul + (soni * narxi)
#         return jami_pul
#     def checkout(self):
#         umumiy_narx = self.get_cart_total()
#         if self.balance >= umumiy_narx:
#             self.balance = self.balance - umumiy_narx 
#             self.clear_cart()
#             return True
#         else:
#             return False
#     def __str__(self):
#         return f"Customer: {self.name} (balance: {self.balance} so'm)"        

# # mijoz = Customer("mijoz1", "mijoz1@mail.com", "Toshkent", balance=100000)
# # print(mijoz)
# # mijoz.__str__()




# class Seller(User):
#     def __init__(self, name, email, address, rating = 0.0):
#         super().__init__(name, email, address)
#         self.products = {}
#         self.rating = float(rating)
#     def add_product(self, name, qty):
#         if qty > 0:
#             if name in self.products:
#                 self.products[name] += qty
#             else:
#                 self.products[name] = qty
#     def remove_product(self, name):
#         if name in self.products:
#             del self.products[name]
#             return True
#         return False
#     def update_stock(self, name, delta_qty):
#         if name not in self.products:
#             return False
#         new_qty = self.products[name] + delta_qty
#         if new_qty < 0:
#             return False
#         self.products[name] = new_qty
#         return True
#     def get_stock(self):
#         return self.products.copy()
#     def __str__(self):
#         total_items = sum(self.products.values())
#         return f"Seller: {self.name} (rating: {self.rating}, items: {total_items})"

# ...........................................................................................

# class Person:
#     def __init__(self, name, id_number):
#         self.name = name
#         self.id_number = id_number
#     def get_name(self):
#         return self.name
#     def get_id(self):
#         return self.id_number
#     def __str__(self):
#         return f"Person: {self.name} (#{self.id_number})"




    
# class Patient(Person):
#     def __init__(self, name, id_number):
#         super().__init__(name, id_number)
#         self.diagnoses = []
#         self.bill = 0
#     def add_diagnosis(self, text):
#         self.diagnoses.append(text)
#     def add_charge(self, amount):
#         if amount > 0:
#             self.bill += amount
#     def pay(self, amount):
#         if amount <= 0:
#             return False
#         if amount >= self.bill:
#             self.bill = 0
#             return True
#         else:
#             self.bill -= amount
#             return True
#     def get_balance(self):
#         return self.bill
#     def print_history(self):
#         print(f"Patient: {self.name}")
#         print("Diagnoses:")
#         for i in self.diagnoses:
#             print(f"- {i}")
#         print(f"Current Bill: {self.bill} so'm")




# class Doctor(Person):
#     def __init__(self, name, id_number, specialty):
#         super().__init__(name, id_number)
#         self.specialty = specialty
#         self.schedule = {}
#     def add_slot(self, day, time):
#         if day not in self.schedule:
#             self.schedule[day] = []
#         if time not in self.schedule[day]:
#             self.schedule[day].append(time)
#     def book_slot(self, day, time):
#         if day in self.schedule and time in self.schedule[day]:
#             self.schedule[day].remove(time)
#             return True
#         return False
#     def available_slots(self, day):
#         if day in self.schedule:
#             return self.schedule[day].copy()
#         return []
#     def __str__(self):
#         return f"Dr. {self.name} ({self.specialty})"   

# .............................................................................................

class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []
    def get_title(self):
        return self.title
    def get_teacher(self):
        return self.teacher
    def enroll(self, student_name):
        if student_name in self.students:
            return False
        self.students.append(student_name)
        return True
    def drop(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            return True
        return False
    def __str__(self):
        return f"{self.title} ({self.teacher})"




class OnlineCourse(Course):
    def __init__(self, title, teacher, url, max_students):
        super().__init__(title, teacher)
        self.url = url
        self.max_students = int(max_students)
    def enroll(self, student_name):
        if len(self.students) < self.max_students:
            return super().enroll(student_name)
        return False
    def get_room(self):
        return f"Virtual: {self.url}" 




class OfflineCourse(Course):
    def __init__(self, title, teacher, room, capacity):
        super().__init__(title, teacher)
        self.room = room
        self.capacity = int(capacity)
    def enroll(self, student_name):
        if len(self.students) < self.capacity:
            return super().enroll(student_name)
        return False
    def get_room(self):
        return f"Room: {self.room}"    

