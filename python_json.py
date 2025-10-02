# import json
# bemor = {
#     "ism": "Ali Valiyev",
#     "yosh": 30,
#     "oila": True,
#     "farzandlar": ("shoxruza", "Sevinch"),
#     "allergiya": None,
#     "dorilar": [
#         {"nomi": "Analgin", "miqdori":0.5},
#         {"nomi": "Pandol" ,"miqdori": 1.2}
#     ]
# }
# bemor_json = json.dumps(bemor, indent=4)
# print(bemor_json)
# print(type(bemor_json))
#
# with open ('bemor.json', 'w') as f:
#     json.dump(bemor,f)

#
#
# yosh = input('yoshingizni kiriting:')
# try:
#     yosh = int(yosh)
#     print(f"siz{2025-yosh} yilda tugilgansiz")
# except:
#     print("Butun son kiritmadingiz")
#
# print("Dastur Tugadi!")

x,y=5,10
try:
    y/(x-5)
except :
    print("Butun son kirit")



n = input("Butun son kiriting:")
try:
    n = int(n)
    x=20/n
except ValueError:
    print("Butun son kiritmadingiz")
except ZeroDivisionError:
    print("0 ga bo`lib bolmaydi")
else:
    print(f"x={x}")
