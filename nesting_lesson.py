car0 = {
    'model' : 'lacetti',
    'rang' : 'oq',
    'yil' : 2018,
    'narh' : 13000,
    'km' : 50000,
    'karobka' : 'avtomat'
}

car1 = {
    'model' : 'nexia 3',
    'rang' : 'qora',
    'yil' : 2014,
    'narh' : 9000,
    'km' : 89000,
    'karobka' : 'mexanika'
}

car2 = {
    'model' : 'gentre',
    'rang' : 'qizil',
    'yil' : 2019,
    'narh' : 15000,
    'km' : 20000,
    'karobka' : 'avtomat'
}
cars = [car0,car1, car2]
for car in cars:
    print(f"{car['model'].title()}",
          f"{car['rang']} rang ",
          f"{car['yil']}-yil, {car['narh']}$")

print(cars[0])
print(cars[0]['model'])
print(f"{cars[2]['rang'].title()}",
          f"{cars[2]['model']}")


malibus=[]
for n in range (10):
    new_car = {
    'model' : 'malibu',
    'rang' : 'None',
    'yil' : 2018,
    'narh' : None,
    'km' : 0,
    'karobka' : 'avtomat'
    }
    malibus.append(new_car)
print(malibus)

for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'

    for malibu in malibus[3:6]:
        malibu['rang'] = 'qora'

for malibu in malibus[:6]:
    malibu['rang'] = 'qora'
    malibu['karobka'] = 'mexanika'

for malibu in malibus:
    if malibu ['karobka']=='avto' :
        malibu['narh']=40000
    else:
        malibu['narh']=35000
print(malibus)


dasturchilar = {
    'ali': ['python','c++'],
    'vali': ['htmli', 'css', 'js'],
    'hasan' : ['php','sql'],
    'husan' : ['python', 'php'],
    'maryam': ['c++', 'c#']
}
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())


hamkasblar = {
    'ali' : {"familiya": "valiyev",
        'tyil':1995,
        'malumot': 'oliy',
        'tillar' :['python', 'c++']
    },

    'vali' : {"familiya": "aliyev",
        'tyil':2001,
        'malumot': 'orta maxsusu',
        'tillar' :['html', 'css', 'jss']},

    'hasan': {"familiya": "aliyev",
        'tyil': 1999,
        'malumot': 'maxsusus',
        'tillar': ['html', 'css', 'jss']}
}

for ism , info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title},"
          f"{info['tyil']}-yilda tugilgan."
          f"Ma`lumoti: {info['malumot']}.\n"
          "quyidagi dasturlash tillarini bialdi:")
    for til in  info['tilar']:
         print(til.upper())