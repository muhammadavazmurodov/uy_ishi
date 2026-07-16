import json
# with open("on.json") as f:
#     branch = json.load(f)
#     for i in branch["branches"]:
#         print(i['name'])

# ....

# with open("on.json") as f:
#     branch = json.load(f)
#     for i in branch["branches"]:
#         for l in i['teachers']:
#             if l ['subject'] == 'Python':
#                 print(f'{l['name']} -> {i['name']} -> {l['experience']}')
       
# ....

# with open("on.json") as f:
#     dct = {}
#     branch = json.load(f)
#     for i in branch["branches"]:
#         for l in i['students']:
#             if i['name'] not in dct:
#                 dct[i['name']] = 1
#             else:
#                 dct[i['name']] += 1                
#     print(dct)

# ....

# with open("on.json") as f:
#     data = json.load(f)
#     st = []
#     for i in data["branches"]:
#         for l in i['students']:
#             student = {
#                 'name' : l['name'],
#                 'branch' : i['name'],
#                 'payment': l['payment']
#             }
#             st.append(student)
# top = max(st, key=lambda x: x['payment'])
# print(f'{top['name']} -> {top['branch']} -> {top['payment']}')

# ....

# with open('on.json') as f:
#     data = json.load(f)
#     for i in data['branches']:
#         s = sum(s['payment'] for s in i['students'])
#         print(f'{i['name']} -> {s}')

# ....

# with open('on.json') as f:
#     data = json.load(f)
#     for i in data['branches']:
#         for l in i['teachers']:
#             if l ['experience'] > 5:
#                 print(l['name'])

# ....

with open('on.json') as f:
    data = json.load(f)
    for i in data['branches']:
        if all(l['subject'] == 'Python' for l in i['teachers']):
            print(i['name'])