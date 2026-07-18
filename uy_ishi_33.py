# a =  [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(sorted(b))

# # ....

# A = [ 
#     [1, 2], 
#     [3, 4] 
# ] 
 
# B = [ 
#     [5, 6], 
#     [7, 8] 
# ]

# C = [[A[x][i] + B[x][i] for i in range(len(A[x]))] for x in range(len(A))]
# print(f"C = [ \n    {C[0]},\n    {C[1]}\n]")

# ....

# def count_passing_students(grades: list[int], passingGrade: int) -> int:
#     count = 0
#     for i in grades:
#         if i >= passingGrade:
#             count += 1
#     return count
# grades = [45, 60, 75, 30, 90] 
# passingGrade = 60 
# print(count_passing_students(grades, passingGrade))

# ....

# def ends_with_gram(words: list[str]) -> list[str]:
#     a = []
#     for i in words:
#         if i.lower().endswith('gram'):
#             a.append(i)
#     return a        
        
# words = ["telegram", "Instagram", "hello", "program", "diagram", 
# "world"] 
# print(ends_with_gram(words))

# ....

def get_phone_number(contacts: dict[str, str], search_name: str) -> str:
    for i, x in contacts.items():
        if i.lower() == search_name.lower():
            return x
    return 'Topilmadi'

contacts = { 
    "Ali": "+998901112233", 
    "Vali": "+998909998877", 
    "Hasan": "+998938889900" }
search_name = input('>>> ')
print(get_phone_number(contacts, search_name))               
