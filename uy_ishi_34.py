# class Kitob:
#     def __init__(self, nomi, muallifi, narxi, nashriyoti):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.narxi = narxi
#         self.nashriyoti = nashriyoti
#     def malumot(self):
#         print(f"Nomi: {self.nomi}, Muallifi: {self.muallifi}, Narxi: {self.narxi}, Nashriyoti: {self.nashriyoti}")
#     def sarala(royxat):
#         for i in royxat:
#             a  = i.nashriyoti[0].upper()
#             if 'A' <= a <= 'H':
#                 i.malumot()

# k1 = Kitob('k1n', 'k1m', 100, 'Ak1na')                
# k2 = Kitob('k2n', 'k2m', 200, 'bk2na')
# kitoblar = [k1, k2]
# Kitob.sarala(kitoblar)




# class Kompyuter:
#     def __init__(self, nom, ram, narx, protsessor):
#         self.nom = nom
#         self.ram = ram
#         self.narx = narx
#         self.protsessor = protsessor
#     def sarala(royxat):
#         for i in royxat:
#             if 4 < i.ram < 16:
#                 print(f"{i.nom} {i.ram} {i.narx} {i.protsessor}")

# k1 = Kompyuter('kn', 8, 200, 'kp')
# k2 = Kompyuter('knn', 1, 200, 'kpp')
# komp = [k1, k2]
# Kompyuter.sarala(komp)




class User:
    def __init__(self, ism, foydalanuvchi_nomi, email):
        self.ism = ism
        self.foydalanuvchi_nomi = foydalanuvchi_nomi
        self.email = email
    def get_info(self):
        print(f"Ismi: {self.ism}, Foydalanuvchi nomi: {self.foydalanuvchi_nomi}, Email: {self.email}")

u1 = User("user1", "user1fn", "user1@gamil.com")
u1.get_info()
