#def salom_ber():
#     """Salom beruvchi funksiya"""
# print("Assalomu aleykum")

# def uchburchak_yuzi(a,b,c):
#     p=(a+b+c)/2
#     s=(p*(p-a)+p*(p-b)+p*(p-c))**1/2
#     print("S=",s)
#
# uchburchak_yuzi(5,3,3)
# uchburchak_yuzi(6,7,2)
# uchburchak_yuzi(4,3,3)
#
#
# def salom_ber(ism):
#     """
#     Foydalanuvchini ismini qabul qlib
#     unga salom beruvhchi funksiya
#     print(f"Assalomu aleykum,hurmatli {ism.tittle()}!")
#
#     salom_ber('hasan')
#     print(salom_ber.__doc__)
#     """
#
# def  toliq_ism(ism,familiya):
#         """Foydalanuvchini ism va familyasini chiqaruvchu funksiya"""
#         print(f"Foydalanuvchi ismi:{ism.title()}\n"
#               f"Foydalanuvchi familyasi:{familiya.title()}")
#
# toliq_ism("ali", "valiyev")

# def yosh_hisobla(tugilgan_yil, joriy_yil=2040):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasz")
#
# yosh_hisobla(2007)

def toliq_ism(ism, familya):
    """Toliq ism qaytaruvchu funksiya"""
    toliq_ism=f"{ism} {familiya}"
    return toliq_ism

a=toliq_ism("ali","Valiyev")
