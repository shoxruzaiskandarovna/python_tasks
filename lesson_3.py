# ism = "Shahruza"
# yosh = 18
# print(ism)
# print(yosh)
#
# i_sm = "Shoxruza"
# print(i_sm)
# ism = "Shaxruza"
# print(ism)
#
# ism_familya = "Otanazarova Shohruza"
#
# # camel case
# ismFamilya = "Otanzarova Shohruza"
#
# # paskal case
# IsmFamilya = "Otanazarova Shohruza"
#
# # class = "urganch"
# Shahar = "Urganch"
# viloyat = 'Xorazm'
#
# matn = "men yangi 📱 oldim 😂"
# print(matn)
#
# ism = 'Shahruza'
# print("Mening ismim " + ism)
# print("Mening ismim",ism)
#
# ism = "Shahruza"
# familya = 'Otanazarova'
# ism_sharif = f"{ism} {familya}  {5+3}!"
#
# print('Hello World')
# print("Hello\n World ")
# print("Hello\t World ")
#
# ism = "1shoxruza"
# familya = 'Otanazarova'
# ism_sharif = f"{ism} {familya}"
#
# print(ism_sharif.upper())
# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())
#
# meva = "   uzum   "
# print("Men " + meva.lstrip() + "yaxshi ko`raman")
# print("Men " + meva.rstrip() + "yaxshi ko`raman")
# print("Men " + meva.strip() + "yaxshi ko`raman")
# print("Men " + meva + "yaxshi ko`raman")
#
# ism= input("Ismingiz nima?")
# print("Assalomu aleykum, "+ ism)

#type casting
a = 20  #sonlar musbat yoki
b = -30 #manfiy bo'lishi mumkin
c = a+b
print(c)

#kvadratning yuzini xisoblaymiz
kvdrt_tmni = 20 #kvadrating tomoni 20 ga teng
kvdrt_yuzi =  kvdrt_tmni**2 # kvadrat yuzini hisoblaymuz
print(kvdrt_yuzi)

#float
a = -20
b = 40
c = b/a
print(c) # natija o`nlik son bo`ladi

aholi_soni = 7_594_000_000 # o`zimizga qulY Bo`lishi uchun shunday
print("Yer kurrasida", aholi_soni, "ga yaqin odam yashaydi")

a = 10.3
a = str(a)
print(a)
print(type(a))

b= "15"
b = int(b)
b= float(b)
print(b)
print(type(b))

#foydaalanuvchining tug`ilgan yilini soraymiz
t_yil = input("Tug`ilgan yilingizni kiriting:")
#foydalanuvchining yoshini hisoblaymiz
yosh = 2025 - int(t_yil) #
#foydalanuvchini yoshini konsolga chiqaramiz
print(f"Siz {yosh} yoshda ekansiz")


colors = ["red", "green", "blue"]
colors.clear()  # This removes all elements from the list
print(colors)

numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)

toys = ["teddy bear", "car", "puzzle"]
toys.clear()
print(toys)

#copy()-lisdaki elementlardan nusxa oladi
cars = ["bmw", "audi", "tesla"]
cars = cars.copy()
print(cars)

letters = ["A", "B", "C", "D"]
letters = letters.copy()
print(letters)  # ['A', 'B', 'C', 'D']

positions = ["first", "second", "third"]
positions = positions.copy()
print(positions[1])  # 'second'

#count(), u roʻyxatda berilgan qiymat necha martauchraganini sanaydi
numbers = [1, 2, 3, 2, 4, 2, 5]
count_twos = numbers.count(2)
print(count_twos)  # Natija: 3

words = ["hello", "world", "hello", "python"]
count_hello = words.count("hello")
print(count_hello)

empty_list = []
count_any = empty_list.count("anything")
print(count_any)

#ectend-bir ro'yxatga boshqa ro'yxatning elementlarini qoshadi
list1 = []
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

numbers = [10, 20]
numbers = [30, 40, 50]
numbers.extend(numbers)
print(numbers)

words = ["hello", "world"]
words = ["python", "is", "fun"]
words.extend(words)
print(words)

#index() metodi ro'yxatda berilgan qiymatning eng birinchi uchragan joyidagi indeksini (o'rnini) qaytaradi.
books = ["Alchemist", "War and Peace", "1984", "The Hobbit"]
books = books.index("1984")
print(books)

library = ["Don Quixote", "Moby Dick", "Hamlet", "The Odyssey"]
library = library.index("Hamlet")
print(library)

#insert() metodi ro'yxatga ma'lum indeksga yangi element qo'shadi
cities = ["Paris", "London", "Tokyo"]
cities.insert(1, "New York")
print(cities)

colors = ["red", "green", "blue"]
colors.insert(0, "yellow")
print(colors)

cars = ["Toyota", "Honda", "Ford"]
cars.insert(2, "Chevrolet")
print(cars)

#pop() metodi ishlatilgan — u ro’yxatdan ko‘rsatilgan indeksdagi elementni o`chrb tashlaydi
colors = ["red", "green", "blue", "yellow"]
colors.pop(2)
print(colors)

cities = ["Paris", "London", "Tokyo", "New York"]
cities.pop(3)
print(cities)

books = ["Hamlet", "Macbeth", "Othello"]
books.pop(0)
print(books)

#remove() metodi ishlatilgan — u ro‘yxatdan berilgan qiymatni o‘chiradi (faqat birinchi uchraganini).
animals = ["dog", "cat", "elephant", "rabbit"]
animals.remove("cat")
print(animals)

languages = ["Python", "Java", "C++", "JavaScript"]
languages.remove("Java")
print(languages)

topics = ["math", "history", "physics", "chemistry"]
topics.remove("history")
print(topics)


#reverse ro‘yxatdagi elementlar tartibini teskari qladi
languages = ["Python", "Java", "C++", "JavaScript"]
languages.reverse()
print(languages)

genres = ["rock", "jazz", "pop", "classical"]
genres.reverse()
print(genres)

foods = ["bread", "cheese", "butter", "egg"]
foods.reverse()
print(foods)

#sort ro'yxatdagi elementlarni tartiblab (saralab) chiqadi (odatda alifbo yoki son tartibida).
languages = ["Python", "Java", "C++", "Ruby"]
languages.sort()
print(languages)

clothes = ["jacket", "hat", "shirt", "pants"]
clothes.sort()
print(clothes)

genres = ["jazz", "rock", "blues", "pop"]
genres.sort()
print(genres)







































































