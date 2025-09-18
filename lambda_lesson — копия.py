from math import sqrt

def daraja(n):
     return lambda x : x**n
kvadarat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadarati {kvadarat(3)} ga, kubi {kub(3)} ga teng")



sonlar = list (range(11)) # 0 dan 10 gacha sonlar royxati
ildizlar  = list(map(sqrt,sonlar))
print(ildizlar)


import math
uzunlik = lambda pi,r : 2*pi*r
print(uzunlik(math.pi,10))


product = lambda x,y : x ** y
print(product(3,2))



sonlar = list(range(11)) #0 dan 10 gacha sonlar royxati

def daraja2(x):
    """Berilgan sonning kvadaratini qayataruvchi funksiya"""
    return x*x

print(list(map(daraja2,sonlar)))

kvadratlar = list(map(lambda x :x*x,sonlar))
print(kvadratlar)


a = [4,5,6]
b = [7,8,9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)

ismlar = ['hasan', 'husan', 'olim', 'umid']
print(list(map(lambda matn:matn.upper(),ismlar)))


# filter funksiya
import random as r

sonlar = r.sample(range(100),10) # 0-99 oraligidaki tasadifiy sonlar
#
# def juftmi(x):
#     """x juft bolsa True, aks holda FAlse qayataruvchi funksiya"""
#     return x%2==0
 #lambda orqali ishlanishi


juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

print(sonlar)
print(juft_sonlar)


mevalar = ['olma', 'anor','anjir', 'shaftoli', "o`rik",'tarvuz', 'qovun','baliq']

mevalar_b = list(filter(lambda meva:meva.startswith('a'),mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda meva:len(meva)<=5,mevalar))
print(mevalar2)