# # ==========================================
# # Python Basics - جزوه جامع مقدماتی پایتون
# # ==========================================


# # ==========================================
# # 1. PRINT - نمایش خروجی
# # ==========================================

# print("Hello World")
# print(25)
# print(10 + 5)

# # نمایش چند مقدار
# print("Name:", "Ali")


# # ==========================================
# # 2. VARIABLES - متغیرها
# # ==========================================

# name = "Parsa"
# age = 18
# height = 1.75
# is_student = True

# print(name)
# print(age)
# print(height)
# print(is_student)


# # ==========================================
# # 3. DATA TYPES - انواع داده
# # ==========================================

# text = "Python"          # str: رشته
# number = 10              # int: عدد صحیح
# decimal = 3.14           # float: عدد اعشاری
# active = True            # bool: مقدار منطقی
# fruits = ["apple", "banana"]  # list: لیست
# coordinates = (10, 20)    # tuple: تاپل
# unique_numbers = {1, 2, 3}  # set: مجموعه
# person = {"name": "Ali", "age": 20}  # dict: دیکشنری
# empty_value = None       # NoneType: مقدار تهی

# print(type(text))
# print(type(number))
# print(type(decimal))
# print(type(active))


# # ==========================================
# # 4. TYPE CONVERSION - تبدیل نوع داده
# # ==========================================

# age_text = "18"

# age_number = int(age_text)
# price = float("19.5")
# message = str(100)
# is_valid = bool(1)

# print(age_number + 2)
# print(price)
# print(message)
# print(is_valid)


# # ==========================================
# # 5. ARITHMETIC OPERATORS - عملگرهای ریاضی
# # ==========================================

# print(5 + 2)    # جمع
# print(5 - 2)    # تفریق
# print(5 * 2)    # ضرب
# print(5 / 2)    # تقسیم
# print(5 // 2)   # تقسیم صحیح
# print(5 % 2)    # باقی‌مانده تقسیم
# print(2 ** 3)   # توان

# score = 10
# score += 5
# print(score)

# score -= 3
# print(score)


# # ==========================================
# # 6. COMPARISON OPERATORS - عملگرهای مقایسه
# # ==========================================

# print(5 == 5)   # برابر
# print(5 != 3)   # نابرابر
# print(5 > 3)    # بزرگ‌تر
# print(2 < 5)    # کوچک‌تر
# print(5 >= 5)   # بزرگ‌تر یا برابر
# print(3 <= 5)   # کوچک‌تر یا برابر


# # ==========================================
# # 7. LOGICAL OPERATORS - عملگرهای منطقی
# # ==========================================

# print(True and True)   # هر دو شرط درست باشند
# print(True or False)   # حداقل یک شرط درست باشد
# print(not True)        # برعکس کردن مقدار منطقی


# # ==========================================
# # 8. STRINGS - رشته‌ها
# # ==========================================

# word = "Python"

# print(word[0])       # اولین کاراکتر
# print(word[-1])      # آخرین کاراکتر
# print(word[0:3])     # برش رشته
# print(word[::-1])    # معکوس کردن رشته

# print("Hello" + " World")  # اتصال رشته‌ها
# print("Hi " * 3)            # تکرار رشته


# # ==========================================
# # 9. STRING METHODS - متدهای رشته
# # ==========================================

# text = "  hello python  "

# print(text.upper())               # حروف بزرگ
# print(text.lower())               # حروف کوچک
# print(text.capitalize())          # بزرگ کردن حرف اول
# print(text.title())               # بزرگ کردن ابتدای کلمات
# print(text.strip())               # حذف فاصله‌های ابتدا و انتها
# print(text.lstrip())              # حذف فاصله از چپ
# print(text.rstrip())              # حذف فاصله از راست
# print(text.replace("python", "world"))  # جایگزینی
# print(text.find("python"))        # پیدا کردن موقعیت
# print(text.count("o"))            # شمارش تکرار

# print("Python".startswith("Py"))  # بررسی شروع
# print("file.png".endswith(".png"))  # بررسی پایان

# words = "apple,banana,orange"
# print(words.split(","))           # تقسیم رشته به لیست

# word_list = ["Hello", "Python"]
# print(" ".join(word_list))        # اتصال اعضای رشته‌ای

# print("Python".isalpha())         # فقط حروف
# print("123".isdigit())            # فقط ارقام
# print("Python123".isalnum())      # حروف یا ارقام

# print("Hi".center(10, "-"))       # وسط‌چین کردن

# # جدول تبدیل کاراکترها
# table = str.maketrans("abc", "xyz")
# print("abc cab".translate(table))


# # ==========================================
# # 10. CONDITIONALS - ساختارهای شرطی
# # ==========================================

# age = 17

# if age >= 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")


# # ==========================================
# # 11. LOOPS - حلقه‌ها
# # ==========================================

# # حلقه for
# for number in range(5):
#     print(number)

# # تعیین شروع، پایان و فاصله
# for number in range(2, 10, 2):
#     print(number)

# # حلقه while
# count = 1

# while count <= 3:
#     print(count)
#     count += 1

# # break: خروج از حلقه
# for number in range(10):
#     if number == 3:
#         break
#     print(number)

# # continue: رد کردن تکرار فعلی
# for number in range(5):
#     if number == 2:
#         continue
#     print(number)


# # ==========================================
# # 12. LISTS - لیست‌ها
# # ==========================================

# numbers = [3, 1, 2, 2]

# numbers.append(4)       # افزودن عضو
# numbers.extend([5, 6])  # افزودن چند عضو
# numbers.insert(0, 10)   # افزودن در موقعیت مشخص
# numbers.remove(2)       # حذف اولین مقدار 2

# last_number = numbers.pop()  # حذف و برگرداندن آخرین عضو

# print(numbers)
# print(last_number)
# print(numbers.count(2))  # شمارش تکرار
# print(numbers.index(3))  # پیدا کردن موقعیت

# numbers.sort()           # مرتب‌سازی صعودی
# numbers.reverse()        # معکوس کردن ترتیب

# print(numbers)

# # ساخت لیست جدید از روی لیست قبلی
# squares = [number ** 2 for number in range(5)]
# print(squares)


# # ==========================================
# # 13. TUPLES - تاپل‌ها
# # ==========================================

# coordinates = (10, 20, 30)

# print(coordinates[0])
# print(len(coordinates))


# # ==========================================
# # 14. SETS - مجموعه‌ها
# # ==========================================

# set_a = {1, 2, 3}
# set_b = {3, 4, 5}

# set_a.add(4)           # افزودن عضو
# set_a.discard(10)      # حذف بدون خطا در صورت نبودن عضو

# print(set_a | set_b)   # اجتماع
# print(set_a & set_b)   # اشتراک
# print(set_a - set_b)   # تفاضل


# # ==========================================
# # 15. DICTIONARIES - دیکشنری‌ها
# # ==========================================

# person = {
#     "name": "Ali",
#     "age": 20
# }

# print(person["name"])
# print(person.get("city", "Unknown"))

# person["city"] = "Mashhad"  # افزودن کلید جدید
# person.update({"age": 21})  # به‌روزرسانی

# print(person.keys())        # کلیدها
# print(person.values())      # مقادیر
# print(person.items())       # کلید و مقدار

# removed_age = person.pop("age")
# print(removed_age)


# # ==========================================
# # 16. FUNCTIONS - توابع
# # ==========================================

# def greet(name):
#     return f"Hello {name}"


# print(greet("Ali"))


# # تابع با چند پارامتر
# def add(a, b):
#     return a + b


# print(add(3, 4))


# # پارامتر پیش‌فرض
# def welcome(name="Friend"):
#     return f"Welcome {name}"


# print(welcome())
# print(welcome("Parsa"))


# # چند مقدار برگشتی
# def calculate(a, b):
#     return a + b, a * b


# total, product = calculate(3, 4)

# print(total)
# print(product)


# # ==========================================
# # 17. BUILT-IN FUNCTIONS - توابع آماده
# # ==========================================

# print(len("Python"))
# print(sum([1, 2, 3]))
# print(min([4, 1, 8]))
# print(max([4, 1, 8]))
# print(abs(-5))
# print(round(3.14159, 2))
# print(sorted([3, 1, 2]))
# print(isinstance(5, int))

# print(all([True, True]))
# print(any([False, True]))


# # ==========================================
# # 18. ALL, ANY AND ENUMERATE
# # ==========================================

# numbers = [2, 4, 6]

# print(all(number > 0 for number in numbers))
# print(any(number > 5 for number in numbers))

# # enumerate: شماره و مقدار هر عضو
# for index, fruit in enumerate(["apple", "banana"]):
#     print(index, fruit)


# # ==========================================
# # 19. F-STRINGS - قالب‌بندی رشته
# # ==========================================

# name = "Ali"
# age = 20

# print(f"My name is {name} and I am {age} years old.")

# number = 3.14159
# print(f"Number: {number:.2f}")  # دو رقم اعشار


# # ==========================================
# # 20. TRY AND EXCEPT - مدیریت خطا
# # ==========================================

# try:
#     number = int("123")
#     print(number)
# except ValueError:
#     print("Invalid number")


# # ==========================================
# # 21. MEMBERSHIP OPERATORS - عملگرهای عضویت
# # ==========================================

# print("Py" in "Python")
# print(5 in [1, 2, 3])
# print(5 not in [1, 2, 3])


# # ==========================================
# # 22. IMPORT - استفاده از ماژول‌ها
# # ==========================================

# import math

# print(math.sqrt(25))
# print(math.ceil(3.2))
# print(math.floor(3.8))


# # ==========================================
# # 23. RPG CHARACTER - تمرین ترکیبی
# # ==========================================

# def create_character(name, strength, intelligence, charisma):

#     # اعتبارسنجی نام
#     if not isinstance(name, str):
#         return "The character name should be a string"

#     if name == "":
#         return "The character should have a name"

#     if len(name) > 10:
#         return "The character name is too long"

#     if " " in name:
#         return "The character name should not contain spaces"

#     # ذخیره ویژگی‌ها در لیست
#     stats = [strength, intelligence, charisma]

#     # بررسی عدد صحیح بودن ویژگی‌ها
#     if not all(
#         isinstance(stat, int) and not isinstance(stat, bool)
#         for stat in stats
#     ):
#         return "All stats should be integers"

#     # بررسی محدوده ویژگی‌ها
#     if any(stat < 1 for stat in stats):
#         return "All stats should be no less than 1"

#     if any(stat > 4 for stat in stats):
#         return "All stats should be no more than 4"

#     # مجموع امتیازها باید 7 باشد
#     if sum(stats) != 7:
#         return "The character should start with 7 points"

#     # ساخت نمایش ویژگی‌ها
#     full_dot = "●"
#     empty_dot = "○"

#     return (
#         f"{name}\n"
#         f"STR {full_dot * strength}{empty_dot * (10 - strength)}\n"
#         f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}\n"
#         f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
#     )


# print(create_character("ren", 4, 2, 1))

# #==========================================
# #24. LIST INDEXING - دسترسی به اعضای لیست
# #==========================================

# cities = ['Los Angeles', 'London', 'Tokyo']

# print(cities[0])   # اولین عضو
# print(cities[-1])  # آخرین عضو

# # تبدیل رشته به لیست کاراکترها
# developer = 'Jessica'
# print(list(developer))

# # تعداد اعضای لیست
# numbers = [1, 2, 3, 4, 5]
# print(len(numbers))


# # ==========================================
# # 25. MODIFYING LISTS - تغییر اعضای لیست
# # ==========================================

# programming_languages = ['Python', 'Java', 'C++', 'Rust']

# programming_languages[0] = 'JavaScript'
# print(programming_languages)  # تغییر عضو اول

# # شماره اندیس باید در محدوده لیست باشد
# # programming_languages[10] = 'JavaScript'
# # IndexError: اندیس خارج از محدوده است


# # ==========================================
# # 26. REMOVING ELEMENTS - حذف اعضای لیست
# # ==========================================

# developer = ['Jane Doe', 23, 'Python Developer']

# del developer[1]  # حذف عضو با اندیس مشخص
# print(developer)

# numbers = [10, 20, 30, 40, 50]
# numbers.remove(50)  # حذف اولین مقدار مشخص
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# removed_number = numbers.pop(1)  # حذف و برگرداندن عضو
# print(removed_number)

# numbers.pop()  # حذف آخرین عضو
# numbers.clear()  # حذف تمام اعضا


# # ==========================================
# # 27. MEMBERSHIP - بررسی وجود عضو در لیست
# # ==========================================

# programming_languages = ['Python', 'Java', 'C++', 'Rust']

# print('Rust' in programming_languages)        # True
# print('JavaScript' in programming_languages)  # False


# # ==========================================
# # 28. NESTED LISTS - لیست‌های تو در تو
# # ==========================================

# developer = ['Alice', 25, ['Python', 'Rust', 'C++']]

# print(developer[2])     # دسترسی به لیست داخلی
# print(developer[2][1])  # دسترسی به عضو دوم لیست داخلی


# # ==========================================
# # 29. UNPACKING LISTS - باز کردن اعضای لیست
# # ==========================================

# developer = ['Alice', 34, 'Rust Developer']

# name, age, job = developer

# print(name)
# print(age)
# print(job)

# # استفاده از * برای دریافت اعضای باقی‌مانده
# name, *rest = developer

# print(name)
# print(rest)

# # تعداد متغیرها باید با اعضای لیست سازگار باشد
# # name, age, job, city = developer
# # ValueError: تعداد اعضا کافی نیست


# # ==========================================
# # 30. LIST SLICING - برش لیست
# # ==========================================

# desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']

# print(desserts[1:4])  # اعضای اندیس 1 تا قبل از 4

# numbers = [1, 2, 3, 4, 5, 6]

# print(numbers[1::2])  # اعضا با فاصله 2 از اندیس 1
# print(numbers[0::2])  # اعضا با فاصله 2 از اندیس 0


# # ==========================================
# # 31. APPEND AND EXTEND - افزودن به لیست
# # ==========================================

# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)  # افزودن یک عضو
# print(numbers)

# # append لیست را به‌عنوان یک عضو اضافه می‌کند
# even_numbers = [6, 8, 10]
# numbers.append(even_numbers)
# print(numbers)

# # extend اعضای لیست دیگر را جداگانه اضافه می‌کند
# numbers = [1, 2, 3, 4, 5]
# even_numbers = [6, 8, 10]

# numbers.extend(even_numbers)
# print(numbers)


# # ==========================================
# # 32. INSERT - افزودن در موقعیت مشخص
# # ==========================================

# numbers = [1, 2, 3, 4, 5]

# numbers.insert(2, 2.5)  # افزودن در اندیس 2
# print(numbers)


# # ==========================================
# # 33. POP AND CLEAR - حذف اعضا
# # ==========================================

# numbers = [1, 2, 3, 4, 5]

# removed_number = numbers.pop(1)  # حذف عضو اندیس 1
# print(removed_number)

# numbers.pop()  # حذف آخرین عضو
# print(numbers)

# numbers.clear()  # خالی کردن لیست
# print(numbers)


# # ==========================================
# # 34. SORT AND SORTED - مرتب‌سازی لیست
# # ==========================================

# numbers = [19, 2, 35, 1, 67, 41]

# numbers.sort()  # مرتب‌سازی خود لیست
# print(numbers)

# numbers = [19, 2, 35, 1, 67, 41]

# sorted_numbers = sorted(numbers)  # ساخت لیست مرتب جدید

# print(numbers)         # لیست اصلی بدون تغییر
# print(sorted_numbers)  # لیست مرتب‌شده

# # مرتب‌سازی نزولی
# numbers.sort(reverse=True)
# print(numbers)


# # ==========================================
# # 35. REVERSE - معکوس کردن ترتیب لیست
# # ==========================================

# numbers = [6, 5, 4, 3, 2, 1]

# numbers.reverse()
# print(numbers)


# # ==========================================
# # 36. INDEX - پیدا کردن اندیس یک عضو
# # ==========================================

# programming_languages = ['Rust', 'Java', 'Python', 'C++']

# print(programming_languages.index('Java'))

# # اگر مقدار وجود نداشته باشد، خطای ValueError رخ می‌دهد
# # print(programming_languages.index('JavaScript'))


# # ==========================================
# # 37. TUPLES - تاپل‌ها
# # ==========================================

# # تاپل مجموعه‌ای مرتب و غیرقابل تغییر است
# developer = ('Alice', 34, 'Rust Developer')

# print(developer[0])   # دسترسی به عضو اول
# print(developer[-1])  # دسترسی به عضو آخر

# # تغییر اعضای تاپل مجاز نیست
# # programming_languages = ('Python', 'Java', 'C++', 'Rust')
# # programming_languages[0] = 'JavaScript'
# # TypeError: تاپل از تغییر عضو پشتیبانی نمی‌کند

# # دسترسی به اندیس خارج از محدوده
# # numbers = (1, 2, 3, 4, 5)
# # numbers[7]
# # IndexError: اندیس خارج از محدوده است


# # ==========================================
# # 38. TUPLE CONVERSION - تبدیل به تاپل
# # ==========================================

# developer = 'Jessica'

# print(tuple(developer))  # تبدیل رشته به تاپل کاراکترها


# # ==========================================
# # 39. MEMBERSHIP - بررسی وجود عضو در تاپل
# # ==========================================

# programming_languages = ('Python', 'Java', 'C++', 'Rust')

# print('Rust' in programming_languages)        # True
# print('JavaScript' in programming_languages)  # False


# # ==========================================
# # 40. UNPACKING TUPLES - باز کردن اعضای تاپل
# # ==========================================

# developer = ('Alice', 34, 'Rust Developer')

# name, age, job = developer

# print(name)
# print(age)
# print(job)

# # دریافت اعضای باقی‌مانده با *
# name, *rest = developer

# print(name)
# print(rest)  # لیست اعضای باقی‌مانده


# # ==========================================
# # 41. TUPLE SLICING - برش تاپل
# # ==========================================

# desserts = ('cake', 'pie', 'cookies', 'ice cream')

# print(desserts[1:3])  # ('pie', 'cookies')

# # ==========================================
# # 42. TUPLE METHODS - متدهای تاپل
# # ==========================================

# # programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')

# print(programming_languages.count('Rust'))        # تعداد تکرار مقدار
# print(programming_languages.count('JavaScript'))  # اگر نباشد، 0

# # متد count به یک آرگومان نیاز دارد
# # programming_languages.count()
# # TypeError: آرگومان لازم ارسال نشده است


# # پیدا کردن اندیس اولین وقوع مقدار
# print(programming_languages.index('Java'))  # 1

# # اگر مقدار وجود نداشته باشد، خطای ValueError رخ می‌دهد
# # programming_languages.index('JavaScript')


# # جست‌وجو از اندیس مشخص
# programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

# print(programming_languages.index('Python', 3))  # 5

# # جست‌وجو در محدوده مشخص؛ اندیس پایان شامل نمی‌شود
# programming_languages = (
#     'Rust', 'Java', 'Python', 'C++',
#     'Rust', 'Python', 'JavaScript', 'Python'
# )

# print(programming_languages.index('Python', 2, 5))  # 2


# # ==========================================
# # 43. SORTED - مرتب‌سازی تاپل
# # ==========================================

# numbers = (13, 2, 78, 3, 45, 67, 18, 7)

# # مرتب‌سازی صعودی و ساخت لیست جدید
# print(sorted(numbers))

# programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

# # مرتب‌سازی بر اساس طول رشته‌ها
# print(sorted(programming_languages, key=len))

# # مرتب‌سازی نزولی بر اساس ترتیب حروف
# print(sorted(programming_languages, reverse=True))


# # ==========================================
# # 44. FOR LOOP - حلقه for
# # ==========================================

# programming_languages = ['Rust', 'Java', 'Python', 'C++']

# for language in programming_languages:
#     print(language)  # پیمایش اعضای لیست

# # پیمایش کاراکترهای رشته
# for char in 'code':
#     print(char)


# # ==========================================
# # 45. NESTED LOOPS - حلقه‌های تو در تو
# # ==========================================

# categories = ['Fruit', 'Vegetable']
# foods = ['Apple', 'Carrot', 'Banana']

# # اجرای حلقه داخلی برای هر عضو حلقه خارجی
# for category in categories:
#     for food in foods:
#         print(category, food)


# # ==========================================
# # 46. WHILE LOOP - حلقه while
# # ==========================================

# secret_number = 3
# guess = 0

# # تکرار تا زمانی که عدد درست حدس زده شود
# while guess != secret_number:
#     guess = int(input('Guess the number (1-5): '))

#     if guess != secret_number:
#         print('Wrong! Try again.')

# print('You got it!')


# # ==========================================
# # 47. BREAK - خروج از حلقه
# # ==========================================

# developer_names = ['Jess', 'Naomi', 'Tom']

# for developer in developer_names:
#     if developer == 'Naomi':
#         break  # توقف کامل حلقه
#     print(developer)


# # ==========================================
# # 48. CONTINUE - رد کردن تکرار فعلی
# # ==========================================

# developer_names = ['Jess', 'Naomi', 'Tom']

# for developer in developer_names:
#     if developer == 'Naomi':
#         continue  # رد کردن این تکرار
#     print(developer)


# # ==========================================
# # 49. FOR-ELSE - استفاده از else در حلقه
# # ==========================================

# words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

# for word in words:
#     for letter in word:
#         if letter.lower() in 'aeiou':
#             print(f"'{word}' contains the vowel '{letter}'")
#             break
#     else:
#         # فقط وقتی اجرا می‌شود که حلقه داخلی break نشود
#         print(f"'{word}' has no vowels")

# # ==========================================
# # 50. RANGE - تولید دنباله‌ای از اعداد
# # ==========================================

# # تولید اعداد از 0 تا قبل از 3
# for num in range(3):
#     print(num)

# # تعیین نقطه شروع و پایان
# for num in range(1, 5):
#     print(num)

# # تعیین شروع، پایان و گام
# for num in range(2, 11, 2):
#     print(num)

# # range حداقل به یک آرگومان صحیح نیاز دارد
# # range()
# # TypeError: حداقل یک آرگومان لازم است

# # آرگومان range باید عدد صحیح باشد
# # range(3.1)
# # TypeError: عدد اعشاری قابل استفاده نیست

# # گام منفی برای شمارش معکوس
# for num in range(40, 0, -10):
#     print(num)

# # تبدیل range به لیست
# numbers = list(range(2, 11, 2))
# print(numbers)


# # ==========================================
# # 51. ENUMERATE - شماره‌گذاری اعضا
# # ==========================================

# languages = ['Spanish', 'English', 'Russian', 'Chinese']

# # پیمایش اعضای لیست
# for language in languages:
#     print(language)

# # شماره‌گذاری دستی اعضا
# index = 0

# for language in languages:
#     print(f'Index {index} and language {language}')
#     index += 1

# # ساخت زوج‌های (اندیس، مقدار)
# print(list(enumerate(languages)))

# # دریافت اندیس و مقدار به‌صورت هم‌زمان
# for index, language in enumerate(languages):
#     print(f'Index {index} and language {language}')

# # شروع شماره‌گذاری از 1
# for index, language in enumerate(languages, 1):
#     print(f'Index {index} and language {language}')


# # ==========================================
# # 52. ZIP - ترکیب اعضای چند مجموعه
# # ==========================================

# developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
# ids = [1, 2, 3, 4]

# # ترکیب اعضای هم‌موقعیت
# print(list(zip(developers, ids)))

# # پیمایش هم‌زمان دو لیست
# for name, dev_id in zip(developers, ids):
#     print(f'Name: {name}')
#     print(f'ID: {dev_id}')

# # zip تا طول کوتاه‌ترین مجموعه پیش می‌رود


# # ==========================================
# # 53. LIST COMPREHENSION - ساخت لیست خلاصه
# # ==========================================

# # ساخت لیست اعداد زوج با حلقه معمولی
# even_numbers = []

# for num in range(21):
#     if num % 2 == 0:
#         even_numbers.append(num)

# print(even_numbers)

# # ساخت همان لیست با List Comprehension
# even_numbers = [num for num in range(21) if num % 2 == 0]
# print(even_numbers)

# # تعیین زوج یا فرد بودن هر عدد
# numbers = [1, 2, 3, 4, 5]

# result = [
#     (num, 'Even') if num % 2 == 0 else (num, 'Odd')
#     for num in numbers
# ]

# print(result)


# # ==========================================
# # 54. FILTER - فیلتر کردن اعضا
# # ==========================================

# words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

# def is_long_word(word):
#     return len(word) > 4

# # انتخاب کلماتی که طول آن‌ها بیشتر از 4 است
# long_words = list(filter(is_long_word, words))
# print(long_words)


# # ==========================================
# # 55. MAP - اعمال تابع روی اعضا
# # ==========================================

# celsius = [0, 10, 20, 30, 40]

# def to_fahrenheit(temp):
#     return (temp * 9 / 5) + 32

# # تبدیل تمام دماها به فارنهایت
# fahrenheit = list(map(to_fahrenheit, celsius))
# print(fahrenheit)


# # ==========================================
# # 56. SUM - محاسبه مجموع اعداد
# # ==========================================

# numbers = [5, 10, 15, 20]

# # محاسبه مجموع اعضا
# total = sum(numbers)
# print(total)

# # تعیین مقدار اولیه مجموع
# total = sum(numbers, 10)
# print(total)

# # استفاده از آرگومان نام‌گذاری‌شده
# total = sum(numbers, start=10)
# print(total)

# # ==========================================
# # 57. LAMBDA - توابع بی‌نام
# # ==========================================

# # تعریف تابع معمولی
# def square(num):
#     return num ** 2

# print(square(4))  # 16

# # تعریف تابع بی‌نام با lambda
# square = lambda num: num ** 2
# print(square(4))  # 16

# # ساختار کلی:
# # lambda parameters: expression


# # ==========================================
# # 58. LAMBDA WITH FILTER - فیلتر با لامبدا
# # ==========================================

# numbers = [1, 2, 3, 4, 5]

# # انتخاب اعداد زوج
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # [2, 4]


# # ==========================================
# # 59. LAMBDA WITH MAP - تبدیل اعضا با لامبدا
# # ==========================================

# numbers = [1, 2, 3, 4, 5]

# # محاسبه توان دوم هر عدد
# square = lambda x: x ** 2

# squared_numbers = list(map(square, numbers))
# print(squared_numbers)  # [1, 4, 9, 16, 25]


# # ==========================================
# # 60. CONDITIONAL LAMBDA - شرط در لامبدا
# # ==========================================

# # اجرای عبارت اول اگر x مثبت باشد؛ در غیر این صورت عبارت دوم
# result = (
#     lambda x: (x ** 2 + 2 * x - 1) if x > 0
#     else (x ** 3 - x + 4)
# )(3)

# print(result)  # 14


# # ==========================================
# # 61. LAMBDA VS FUNCTION - مقایسه با تابع معمولی
# # ==========================================

# # پیاده‌سازی همان شرط با تابع معمولی
# def calculate_expression(x):
#     if x > 0:
#         return x ** 2 + 2 * x - 1
#     else:
#         return x ** 3 - x + 4

# print(calculate_expression(3))  # 14

# # ==========================================
# # 62. PIN EXTRACTOR - استخراج کد از شعر
# # ==========================================

# def pin_extractor(poems):
#     secret_codes = []  # ذخیره کدهای استخراج‌شده

#     # پیمایش شعرها
#     for poem in poems:
#         secret_code = ''

#         # تقسیم شعر به خطوط جداگانه
#         lines = poem.split('\n')

#         # دریافت اندیس و متن هر خط
#         for line_index, line in enumerate(lines):
#             words = line.split()  # تقسیم خط به کلمات

#             # بررسی وجود کلمه در اندیس موردنظر
#             if len(words) > line_index:
#                 # افزودن تعداد حروف کلمه به کد
#                 secret_code += str(len(words[line_index]))
#             else:
#                 # اگر کلمه‌ای وجود نداشت، صفر اضافه می‌شود
#                 secret_code += '0'

#         # ذخیره کد استخراج‌شده از شعر
#         secret_codes.append(secret_code)

#     return secret_codes  # برگرداندن تمام کدها


# # ==========================================
# # 63. TESTING - آزمایش تابع
# # ==========================================

# poem1 = """Stars and the moon
# shine in the sky
# white and
# until the end of the night"""

# poem2 = """The grass is green
# here and there
# hoping for rain
# before it turns yellow"""

# poem3 = """There
# once
# was
# a
# dragon"""

# # ارسال شعرها به‌صورت یک لیست
# print(pin_extractor([poem1, poem2, poem3]))


# # ==========================================
# # 63. NUMBER PATTERN - ساخت الگوی اعداد
# # ==========================================

# def number_pattern(n):

#     # بررسی صحیح بودن نوع ورودی
#     if not isinstance(n, int) or isinstance(n, bool):
#         return "Argument must be an integer value."

#     # بررسی مثبت بودن عدد
#     if n < 1:
#         return "Argument must be an integer greater than 0."

#     result = ""  # رشته‌ای برای ذخیره نتیجه

#     # پیمایش اعداد از 1 تا n
#     for i in range(1, n + 1):

#         # افزودن فاصله بین اعداد
#         if i > 1:
#             result += " "

#         # تبدیل عدد به رشته و افزودن به نتیجه
#         result += str(i)

#     return result  # برگرداندن رشته نهایی


# # ==========================================
# # 64. TESTING - آزمایش تابع
# # ==========================================

# print(number_pattern(5))      # 1 2 3 4 5
# print(number_pattern(1))      # 1
# print(number_pattern(0))      # پیام خطا
# print(number_pattern(-3))     # پیام خطا
# print(number_pattern(2.5))    # پیام خطا
# print(number_pattern(True))   # پیام خطا
# print(number_pattern("5"))    # پیام خطا


# # ==========================================
# # 65. DICTIONARIES - دیکشنری‌ها
# # ==========================================

# # ساخت دیکشنری با کلید و مقدار
# dictionary = {
#     'key1': 'value1',
#     'key2': 'value2'
# }

# pizza = {
#     'name': 'Margherita Pizza',
#     'price': 8.9,
#     'calories_per_slice': 250,
#     'toppings': ['mozzarella', 'basil']
# }


# # ==========================================
# # 66. DICT CONSTRUCTOR - ساخت دیکشنری با dict
# # ==========================================

# # ساخت دیکشنری از زوج‌های کلید و مقدار
# pizza = dict([
#     ('name', 'Margherita Pizza'),
#     ('price', 8.9),
#     ('calories_per_slice', 250),
#     ('toppings', ['mozzarella', 'basil'])
# ])


# # ==========================================
# # 67. ACCESS AND MODIFY - دسترسی و تغییر مقادیر
# # ==========================================

# # تغییر مقدار یک کلید
# pizza['name'] = 'Margherita'

# print(pizza['name'])

# # دسترسی با get؛ بدون خطا در صورت نبودن کلید
# print(pizza.get('name', 'Unknown'))
# print(pizza.get('unknown_key', 'Default Value'))
# print(pizza.get('toppings', []))


# # ==========================================
# # 68. KEYS AND VALUES - کلیدها و مقادیر
# # ==========================================

# pizza = {
#     'name': 'Margherita Pizza',
#     'price': 8.9,
#     'calories_per_slice': 250
# }

# print(pizza.keys())    # نمایش کلیدها
# print(pizza.values())  # نمایش مقادیر
# print(pizza.items())   # نمایش زوج‌های کلید و مقدار


# # ==========================================
# # 69. POP - حذف کلید و دریافت مقدار
# # ==========================================

# pizza = {
#     'name': 'Margherita Pizza',
#     'price': 8.9,
#     'calories_per_slice': 250
# }

# # حذف کلید موجود و برگرداندن مقدار آن
# print(pizza.pop('price'))

# # اگر کلید وجود نداشته باشد، مقدار پیش‌فرض برگردانده می‌شود
# print(pizza.pop('total_price', 'Not Found'))

# # بدون مقدار پیش‌فرض، نبودن کلید باعث KeyError می‌شود
# # pizza.pop('total_price')


# # ==========================================
# # 70. UPDATE - افزودن و به‌روزرسانی
# # ==========================================

# pizza = {
#     'name': 'Margherita Pizza',
#     'price': 8.9,
#     'calories_per_slice': 250,
#     'toppings': ['mozzarella', 'basil']
# }

# # تغییر قیمت و افزودن کلید جدید
# pizza.update({
#     'price': 15,
#     'total_time': 25
# })

# print(pizza)


# # ==========================================
# # 71. POPITEM - حذف آخرین زوج
# # ==========================================

# # حذف و برگرداندن آخرین زوج کلید و مقدار
# removed_item = pizza.popitem()

# print(removed_item)
# print(pizza)


# # ==========================================
# # 72. CLEAR - خالی کردن دیکشنری
# # ==========================================

# pizza.clear()
# print(pizza)  # {}

# # ==========================================
# # 73. DICTIONARY LOOPS - پیمایش دیکشنری
# # ==========================================

# products = {
#     'Laptop': 990,
#     'Smartphone': 600,
#     'Tablet': 250,
#     'Headphones': 70,
# }

# # پیمایش مقادیر دیکشنری
# for price in products.values():
#     print(price)

# # پیمایش کلیدهای دیکشنری
# for product in products.keys():
#     print(product)

# # پیمایش مستقیم دیکشنری؛ به‌صورت پیش‌فرض کلیدها
# for product in products:
#     print(product)

# # پیمایش زوج‌های کلید و مقدار
# for product in products.items():
#     print(product)

# # دریافت کلید و مقدار در دو متغیر جداگانه
# for product, price in products.items():
#     print(product, price)


# # ==========================================
# # 74. MODIFY VALUES - تغییر مقادیر دیکشنری
# # ==========================================

# products = {
#     'Laptop': 990,
#     'Smartphone': 600,
#     'Tablet': 250,
#     'Headphones': 70,
# }

# # اعمال 20 درصد تخفیف روی قیمت‌ها
# for product, price in products.items():
#     products[product] = round(price * 0.8)

# print(products)


# # ==========================================
# # 75. ENUMERATE DICTIONARY - شماره‌گذاری کلیدها
# # ==========================================

# products = {
#     'Laptop': 990,
#     'Smartphone': 600,
#     'Tablet': 250,
#     'Headphones': 70,
# }

# # دریافت اندیس و کلید به‌صورت یک زوج
# for product in enumerate(products):
#     print(product)

# # دریافت اندیس و کلید در متغیرهای جداگانه
# for index, product in enumerate(products):
#     print(index, product)


# # ==========================================
# # 76. ENUMERATE VALUES - شماره‌گذاری مقادیر
# # ==========================================

# # دریافت اندیس و قیمت به‌صورت یک زوج
# for price in enumerate(products.values()):
#     print(price)

# # دریافت اندیس و قیمت در متغیرهای جداگانه
# for index, price in enumerate(products.values()):
#     print(index, price)


# # ==========================================
# # 77. ENUMERATE ITEMS - شماره‌گذاری زوج‌ها
# # ==========================================

# # دریافت اندیس و زوج کلید و مقدار
# for index, product in enumerate(products.items()):
#     print(index, product)

# # شروع شماره‌گذاری از 1
# for index, product in enumerate(products.items(), 1):
#     print(index, product)

# # ==========================================
# # 78. SET - مجموعه
# # ==========================================
# my_set = {1, 2, 3, 4, 5}

# set()  # ساخت مجموعه خالی
# {}     # ساخت دیکشنری خالی

# # ==========================================
# # 79. ADD - اضافه کردن عضو
# # ==========================================
# my_set.add(6)  # اضافه کردن عضو جدید
# my_set.add(5)  # اعضای تکراری ذخیره نمی‌شوند

# # ==========================================
# # 80. REMOVE - حذف عضو
# # ==========================================
# my_set.remove(4)   # حذف عضو؛ اگر وجود نداشته باشد خطا می‌دهد
# my_set.discard(4)  # حذف عضو؛ اگر وجود نداشته باشد خطا نمی‌دهد
# my_set.clear()     # حذف تمام اعضای مجموعه

# # ==========================================
# # 81. SUBSET & SUPERSET - زیرمجموعه و ابرمجموعه
# # ==========================================
# my_set = {1, 2, 3, 4, 5}
# your_set = {2, 3, 4, 6}

# print(your_set.issubset(my_set))    # False
# print(my_set.issuperset(your_set))  # False

# # ==========================================
# # 82. SET OPERATIONS - عملیات روی مجموعه‌ها
# # ==========================================
# my_set | your_set  # اجتماع: {1, 2, 3, 4, 5, 6}
# my_set & your_set  # اشتراک: {2, 3, 4}
# my_set - your_set  # تفاضل: {1, 5}
# my_set ^ your_set  # اعضای غیرمشترک: {1, 5, 6}

# # ==========================================
# # 83. SET ASSIGNMENT OPERATORS - عملگرهای ترکیبی
# # ==========================================
# # |= اجتماع
# # &= اشتراک
# # -= تفاضل
# # ^= اعضای غیرمشترک

# my_set -= your_set
# print(my_set)  # {1, 5}

# # ==========================================
# # 84. MEMBERSHIP - بررسی وجود عضو
# # ==========================================
# print(5 in my_set)  # True


# # ==========================================
# # 85. IMPORT - وارد کردن ماژول
# # ==========================================
# import math

# math.sqrt(36)  # محاسبه جذر عدد 36

# # ==========================================
# # 86. IMPORT AS - نام مستعار برای ماژول
# # ==========================================
# import math as m

# m.sqrt(36)  # استفاده از نام مستعار m

# # ==========================================
# # 87. FROM IMPORT - وارد کردن توابع مشخص
# # ==========================================
# from math import radians, sin, cos

# angle_degrees = 40
# angle_radians = radians(angle_degrees)  # تبدیل درجه به رادیان

# sine_value = sin(angle_radians)  # محاسبه سینوس
# cos_value = cos(angle_radians)   # محاسبه کسینوس

# print(sine_value)  # 0.6427876096865393
# print(cos_value)   # 0.766044443118978

# # ==========================================
# # 88. IMPORT AS - نام مستعار برای توابع
# # ==========================================
# # from module_name import name1 as alias1
# # from module_name import name2 as alias2

# # ==========================================
# # 89. FROM IMPORT * - وارد کردن تمام نام‌ها
# # ==========================================
# from math import *

# print(sqrt(36))  # 6.0؛ محاسبه جذر
# print(pow(5, 2)) # 25.0؛ توان
# print(exp(1))    # 2.718281828459045؛ توان عدد e

# # ==========================================
# # 90. MATH MODULE - ثابت‌های ریاضی
# # ==========================================
# import math

# print(math.pi)  # عدد پی

# # ==========================================
# # 91. DATETIME - کار با تاریخ
# # ==========================================
# import datetime

# birthday = datetime.date(1959, 7, 15)

# print(birthday.day)    # 15؛ روز
# print(birthday.month)  # 7؛ ماه
# print(birthday.year)   # 1959؛ سال

# # ==========================================
# # 92. __NAME__ - نقطه شروع اجرای برنامه
# # ==========================================
# if __name__ == '__main__':
#     # کدهای اصلی برنامه در این بخش قرار می‌گیرند
#     pass

# # ==========================================
# # 93. REGEX - عبارت‌های منظم
# # ==========================================
# import re

# # re.fullmatch() بررسی می‌کند که کل رشته با الگو مطابقت داشته باشد.
# # re.IGNORECASE باعث می‌شود بزرگی و کوچکی حروف مهم نباشد.

# # ==========================================
# # 94. MEDICAL RECORDS - لیست دیکشنری‌ها
# # ==========================================
# medical_records = [
#     {
#         'patient_id': 'P1001',
#         'age': 34,
#         'gender': 'Female',
#         'diagnosis': 'Hypertension',
#         'medications': ['Lisinopril'],
#         'last_visit_id': 'V2301',
#     },
#     {
#         'patient_id': 'p1002',
#         'age': 47,
#         'gender': 'male',
#         'diagnosis': 'Type 2 Diabetes',
#         'medications': ['Metformin', 'Insulin'],
#         'last_visit_id': 'v2302',
#     },
#     {
#         'patient_id': 'P1003',
#         'age': 29,
#         'gender': 'female',
#         'diagnosis': 'Asthma',
#         'medications': ['Albuterol'],
#         'last_visit_id': 'v2303',
#     },
#     {
#         'patient_id': 'p1004',
#         'age': 56,
#         'gender': 'Male',
#         'diagnosis': 'Chronic Back Pain',
#         'medications': ['Ibuprofen', 'Physical Therapy'],
#         'last_visit_id': 'V2304',
#     }
# ]

# # ==========================================
# # 95. VALIDATION - بررسی اعتبار اطلاعات
# # ==========================================
# def find_invalid_records(
#     patient_id, age, gender, diagnosis, medications, last_visit_id
# ):
#     constraints = {
#         # شناسه باید رشته‌ای مانند P1001 باشد.
#         'patient_id': isinstance(patient_id, str)
#         and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE),

#         # سن باید عدد صحیح و حداقل 18 باشد.
#         'age': isinstance(age, int) and age >= 18,

#         # جنسیت باید male یا female باشد.
#         'gender': isinstance(gender, str)
#         and gender.lower() in ('male', 'female'),

#         # تشخیص باید رشته یا None باشد.
#         'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

#         # داروها باید لیستی از رشته‌ها باشند.
#         'medications': isinstance(medications, list)
#         and all([isinstance(i, str) for i in medications]),

#         # شناسه ویزیت باید رشته‌ای مانند V2301 باشد.
#         'last_visit_id': isinstance(last_visit_id, str)
#         and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
#     }

#     # برگرداندن نام فیلدهایی که اعتبار ندارند.
#     return [key for key, value in constraints.items() if not value]

# # ==========================================
# # 96. ISINSTANCE - بررسی نوع داده
# # ==========================================
# # isinstance(value, type) بررسی می‌کند مقدار از نوع موردنظر هست یا نه.

# # isinstance(data, (list, tuple))
# # بررسی می‌کند داده لیست یا تاپل باشد.

# # isinstance(dictionary, dict)
# # بررسی می‌کند داده دیکشنری باشد.

# # ==========================================
# # 97. SET - بررسی کلیدهای دیکشنری
# # ==========================================
# key_set = set([
#     'patient_id', 'age', 'gender',
#     'diagnosis', 'medications', 'last_visit_id'
# ])

# # set(dictionary.keys()) مجموعه کلیدهای دیکشنری را می‌سازد.
# # برای اعتبار، کلیدها باید دقیقاً با key_set برابر باشند.

# # ==========================================
# # 98. VALIDATE - بررسی ساختار داده‌ها
# # ==========================================
# def validate(data):
#     # داده باید لیست یا تاپل باشد.
#     is_sequence = isinstance(data, (list, tuple))

#     if not is_sequence:
#         print('Invalid format: expected a list or tuple.')
#         return False

#     is_invalid = False

#     key_set = set([
#         'patient_id', 'age', 'gender',
#         'diagnosis', 'medications', 'last_visit_id'
#     ])

#     # enumerate شماره هر رکورد و خود رکورد را می‌دهد.
#     for index, dictionary in enumerate(data):

#         # هر رکورد باید دیکشنری باشد.
#         if not isinstance(dictionary, dict):
#             print(f'Invalid format: expected a dictionary at position {index}.')
#             is_invalid = True
#             continue

#         # بررسی وجود تمام کلیدهای موردنیاز و نبود کلید اضافی.
#         if set(dictionary.keys()) != key_set:
#             print(
#                 f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
#             )
#             is_invalid = True
#             continue

#         # **dictionary دیکشنری را به آرگومان‌های نام‌دار تبدیل می‌کند.
#         invalid_records = find_invalid_records(**dictionary)

#         # نمایش فیلدهای نامعتبر هر رکورد.
#         for key in invalid_records:
#             print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
#             is_invalid = True

#     # اگر خطایی وجود داشته باشد False برمی‌گرداند.
#     if is_invalid:
#         return False

#     print('Valid format.')
#     return True

# # ==========================================
# # 99. FUNCTION CALL - اجرای تابع اعتبارسنجی
# # ==========================================
# validate(medical_records)  # بررسی اعتبار تمام رکوردها

# # ==========================================
# # 100. ADD SETTING - اضافه کردن تنظیمات
# # ==========================================
# def add_setting(settings, key_value):
#     key, value = key_value  # باز کردن تاپل و دریافت کلید و مقدار
#     key = key.lower()      # تبدیل کلید به حروف کوچک
#     value = value.lower()  # تبدیل مقدار به حروف کوچک

#     if key in settings:  # بررسی وجود کلید
#         return f"Setting '{key}' already exists! Cannot add a new setting with this name."

#     settings[key] = value  # اضافه کردن تنظیم جدید
#     return f"Setting '{key}' added with value '{value}' successfully!"

# # ==========================================
# # 101. UPDATE SETTING - به‌روزرسانی تنظیمات
# # ==========================================
# def update_setting(settings, key_value):
#     key, value = key_value
#     key = key.lower()
#     value = value.lower()

#     if key in settings:  # اگر کلید وجود داشته باشد
#         settings[key] = value  # تغییر مقدار قبلی
#         return f"Setting '{key}' updated to '{value}' successfully!"

#     return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

# # ==========================================
# # 102. DELETE SETTING - حذف تنظیمات
# # ==========================================
# def delete_setting(settings, key):
#     key = key.lower()

#     if key in settings:  # بررسی وجود کلید
#         del settings[key]  # حذف کلید و مقدار آن
#         return f"Setting '{key}' deleted successfully!"

#     return "Setting not found!"  # کلید پیدا نشد

# # ==========================================
# # 103. VIEW SETTINGS - نمایش تنظیمات
# # ==========================================
# def view_settings(settings):
#     if not settings:  # بررسی خالی بودن دیکشنری
#         return "No settings available."

#     result = "Current User Settings:\n"

#     # پیمایش کلیدها و مقدارهای دیکشنری
#     for key, value in settings.items():
#         result += f"{key.capitalize()}: {value}\n"

#     return result  # برگرداندن متن نهایی

# # ==========================================
# # 104. TEST DICTIONARY - دیکشنری آزمایشی
# # ==========================================
# test_settings = {
#     "theme": "dark",
#     "language": "english",
#     "notifications": "enabled"
# }

# # ==========================================
# # 105. FUNCTION - تعریف تابع و برگرداندن نتیجه
# # ==========================================
# def add(a, b):
#     result = a + b  # جمع دو عدد
#     print(f'Adding {a} and {b} gives {result}')  # نمایش نتیجه
#     return result  # برگرداندن نتیجه به محل فراخوانی تابع


# # ==========================================
# # 106. PDB - ابزار دیباگ پایتون
# # ==========================================
# import pdb  # وارد کردن ماژول دیباگ

# def divide(a, b):
#     pdb.set_trace()  # توقف برنامه و ورود به محیط دیباگر
#     return a / b  # تقسیم دو عدد

# print(divide(10, 2))

# # ==========================================
# # 107. PDB COMMANDS - دستورات دیباگر
# # ==========================================
# # help       نمایش راهنمای دستورات
# # whatis a   نمایش نوع متغیر a
# # p a        نمایش مقدار متغیر a
# # n          اجرای خط بعدی بدون ورود به تابع
# # s          اجرای خط بعدی با ورود به تابع
# # c          ادامه اجرای برنامه تا نقطه توقف بعدی
# # l          نمایش خطوط اطراف محل فعلی
# # q          خروج از دیباگر

# # مثال خروجی دستور whatis:
# # (Pdb) whatis a
# # <class 'int'>

# # مثال خروجی دستور whatis برای تابع:
# # (Pdb) whatis divide
# # Function divide

# # ==========================================
# # 108. DEBUGGING - حذف نقطه توقف
# # ==========================================
# def divide(a, b):
#     result = a / b  # ذخیره نتیجه تقسیم
#     return result  # برگرداندن نتیجه

# print(divide(10, 2))  # 5.0
# print(divide(15, 3))  # 5.0

# # ==========================================
# # 109. TRY & EXCEPT - مدیریت خطا
# # ==========================================
# try:
#     x = 10 / 0  # ایجاد خطای تقسیم بر صفر
# except ZeroDivisionError:
#     print("You can't divide by zero!")  # اجرا در صورت وقوع این خطا

# # ==========================================
# # 110. ELSE & FINALLY - بخش‌های تکمیلی
# # ==========================================
# try:
#     x = 10 / 2
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# else:
#     print('Division successful:', x)  # فقط در صورت نبود خطا اجرا می‌شود
# finally:
#     print('This block always runs.')  # در حالت عادی همیشه اجرا می‌شود

# # ==========================================
# # 111. MULTIPLE EXCEPT - مدیریت چند نوع خطا
# # ==========================================
# try:
#     number = int('abc')  # تبدیل رشته نامعتبر به عدد
#     result = 10 / number
# except ValueError:
#     print('That was not a valid number.')  # خطای تبدیل نوع
# except ZeroDivisionError:
#     print("Can't divide by zero.")  # خطای تقسیم بر صفر

# # ==========================================
# # 112. EXCEPT AS - دریافت اطلاعات خطا
# # ==========================================
# try:
#     x = 1 / 0
# except ZeroDivisionError as e:
#     print(f'Error occurred: {e}')  # نمایش پیام خطا

# # ==========================================
# # 113. MULTIPLE EXCEPTIONS - مدیریت چند خطا با هم
# # ==========================================
# try:
#     number = int(input('Enter a number: '))
#     result = 10 / number
# except (ValueError, ZeroDivisionError) as e:
#     print(f'Error occurred: {e}')  # نمایش پیام خطای رخ‌داده

# # ==========================================
# # 114. RAISE - ایجاد خطای دلخواه
# # ==========================================
# def check_age(age):
#     if age < 0:
#         raise ValueError('Age cannot be negative')  # ایجاد خطا
#     return age

# try:
#     check_age(-5)
# except ValueError as e:
#     print(f'Error: {e}')
#     # Error: Age cannot be negative

# # ==========================================
# # 115. RAISE - ارسال دوباره خطا
# # ==========================================
# def process_data(data):
#     try:
#         result = int(data)  # تبدیل داده به عدد صحیح
#         return result * 2
#     except ValueError:
#         print('Logging: Invalid data received')
#         raise  # ارسال دوباره همان خطا

# try:
#     process_data('abc')
# except ValueError:
#     print('Handled at higher level')

# # ==========================================
# # 116. CUSTOM EXCEPTION - ساخت خطای اختصاصی
# # ==========================================
# class InsufficientFundsError(Exception):
#     def __init__(self, balance, amount):
#         self.balance = balance  # موجودی حساب
#         self.amount = amount    # مبلغ درخواستی
#         super().__init__(
#             f'Insufficient funds: ${balance} available, ${amount} requested'
#         )

# def withdraw(balance, amount):
#     if amount > balance:
#         raise InsufficientFundsError(balance, amount)  # ایجاد خطای اختصاصی
#     return balance - amount

# try:
#     new_balance = withdraw(100, 150)
# except InsufficientFundsError as e:
#     print(f'Transaction failed: {e}')

# # ==========================================
# # 117. EXCEPTION CHAINING - زنجیره خطاها
# # ==========================================
# def parse_config(filename):
#     try:
#         with open(filename, 'r') as file:
#             data = file.read()
#             return int(data)  # تبدیل محتوای فایل به عدد
#     except FileNotFoundError:
#         # ایجاد خطای جدید بدون نمایش علت قبلی
#         raise ValueError('Configuration file is missing') from None
#     except ValueError as e:
#         # ایجاد خطای جدید همراه با علت خطای قبلی
#         raise ValueError('Invalid configuration format') from e

# config = parse_config('config.txt')

# # ==========================================
# # 118. ASSERT - بررسی یک شرط
# # ==========================================
# def calculate_square_root(number):
#     assert number >= 0, 'Cannot calculate square root of negative number'
#     return number ** 0.5  # محاسبه جذر با توان یک‌دوم

# try:
#     result = calculate_square_root(-4)
# except AssertionError as e:
#     print(f'Assertion failed: {e}')

# # ==========================================
# # 119. ISBN VALIDATION - اعتبارسنجی کد کتاب
# # ==========================================
# def validate_isbn(isbn, length):
#     # بررسی طول کد ISBN
#     if len(isbn) != length:
#         print(f'ISBN-{length} code should be {length} digits long.')
#         return

#     main_digits = isbn[0:length-1]  # جدا کردن ارقام اصلی
#     given_check_digit = isbn[length-1]  # دریافت رقم کنترلی

#     try:
#         # تبدیل ارقام اصلی به لیست اعداد صحیح
#         main_digits_list = [int(digit) for digit in main_digits]
#     except ValueError:
#         print('Invalid character was found.')
#         return

#     # محاسبه رقم کنترلی بر اساس نوع ISBN
#     if length == 10:
#         expected_check_digit = calculate_check_digit_10(main_digits_list)
#     else:
#         expected_check_digit = calculate_check_digit_13(main_digits_list)

#     # مقایسه رقم کنترلی واردشده با مقدار محاسبه‌شده
#     if given_check_digit == expected_check_digit:
#         print('Valid ISBN Code.')
#     else:
#         print('Invalid ISBN Code.')

# # ==========================================
# # 120. ISBN-10 - محاسبه رقم کنترلی
# # ==========================================
# def calculate_check_digit_10(main_digits_list):
#     digits_sum = 0

#     # ضرب هر رقم در وزن مربوط به خودش
#     for index, digit in enumerate(main_digits_list):
#         digits_sum += digit * (10 - index)

#     result = 11 - digits_sum % 11  # محاسبه رقم کنترلی

#     if result == 11:
#         expected_check_digit = '0'
#     elif result == 10:
#         expected_check_digit = 'X'
#     else:
#         expected_check_digit = str(result)

#     return expected_check_digit  # برگرداندن رقم کنترلی

# # ==========================================
# # 121. ISBN-13 - محاسبه رقم کنترلی
# # ==========================================
# def calculate_check_digit_13(main_digits_list):
#     digits_sum = 0

#     # وزن ارقام به‌صورت یکی‌درمیان 1 و 3 است
#     for index, digit in enumerate(main_digits_list):
#         if index % 2 == 0:
#             digits_sum += digit * 1
#         else:
#             digits_sum += digit * 3

#     result = 10 - digits_sum % 10  # محاسبه رقم کنترلی

#     if result == 10:
#         expected_check_digit = '0'
#     else:
#         expected_check_digit = str(result)

#     return expected_check_digit

# # ==========================================
# # 122. MAIN - دریافت ورودی و اجرای برنامه
# # ==========================================
# def main():
#     user_input = input('Enter ISBN and length: ')

#     try:
#         values = user_input.split(',')  # جدا کردن ورودی با کاما
#         isbn = values[0]
#         length = int(values[1])  # تبدیل طول به عدد صحیح
#     except IndexError:
#         print('Enter comma-separated values.')
#         return
#     except ValueError:
#         print('Length must be a number.')
#         return

#     # بررسی طول مجاز ISBN
#     if length == 10 or length == 13:
#         validate_isbn(isbn, length)
#     else:
#         print('Length should be 10 or 13.')

# # ==========================================
# # 123. FUNCTION CALL - اجرای برنامه
# # ==========================================
# # main()  # با حذف کامنت، برنامه اجرا می‌شود

# # ==========================================
# # 124. CLASS - ساخت کلاس
# # ==========================================
# class ClassName:
#     def __init__(self, name, age):
#         self.name = name  # ویژگی نام
#         self.age = age    # ویژگی سن

#     def sample_method(self):
#         print(self.name.upper())  # تبدیل نام به حروف بزرگ

# # ==========================================
# # 125. OBJECT - ساخت شیء و متد
# # ==========================================
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name.upper()} says woof woof!")

# # ساخت اشیا از روی کلاس
# # object_1 = ClassName(attribute_1, attribute_2)
# # object_2 = ClassName(attribute_1, attribute_2)

# # فراخوانی متدهای اشیا
# # object_1.method_name()
# # object_2.method_name()

# # ==========================================
# # 126. SELF - دسترسی به ویژگی‌های شیء
# # ==========================================
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(
#             f"{self.name.upper()} says woof woof! "
#             f"I'm {self.age} years old!"
#         )

# dog_1 = Dog("Jack", 3)
# dog_2 = Dog("Thatcher", 5)

# dog_1.bark()  # JACK says woof woof! I'm 3 years old!
# dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!

# # ==========================================
# # 127. CLASS ATTRIBUTE - ویژگی کلاس
# # ==========================================
# class Dog:
#     species = "French Bulldog"  # ویژگی مشترک کلاس

#     def __init__(self, name):
#         self.name = name  # ویژگی اختصاصی هر شیء

# print(Dog.species)  # French Bulldog

# dog1 = Dog("Jack")
# print(dog1.name)     # Jack
# print(dog1.species)  # French Bulldog

# dog2 = Dog("Tom")
# print(dog2.name)     # Tom
# print(dog2.species)  # French Bulldog

# # ==========================================
# # 128. INSTANCE ATTRIBUTE - ویژگی‌های نمونه
# # ==========================================
# class Car:
#     def __init__(self, color, model):
#         self.color = color  # رنگ خودرو
#         self.model = model  # مدل خودرو

# car_1 = Car("red", "Toyota Corolla")
# car_2 = Car("green", "Lamborghini Revuelto")

# print(car_1.model)  # Toyota Corolla
# print(car_2.model)  # Lamborghini Revuelto

# print(car_1.color)  # red
# print(car_2.color)  # green

# # ==========================================
# # 129. METHOD - تعریف متد در کلاس
# # ==========================================
# class Dog:
#     species = "French Bulldog"

#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         return f"{self.name} says woof woof!"  # برگرداندن متن

# jack = Dog("Jack")
# jill = Dog("Jill")

# print(jack.bark())  # Jack says woof woof!
# print(jill.bark())  # Jill says woof woof!

# # ==========================================
# # 130. INSTANCE METHOD - متد نمونه
# # ==========================================
# class Car:
#     def __init__(self, color, model):
#         self.color = color  # ویژگی نمونه
#         self.model = model  # ویژگی نمونه

#     def describe(self):
#         # ساخت توضیحات با استفاده از ویژگی‌های شیء
#         return f"This car is a {self.color} {self.model}"

# car_1 = Car("red", "Toyota Corolla")
# car_2 = Car("green", "Lamborghini Revuelto")

# print(car_1.describe())  # This car is a red Toyota Corolla
# print(car_2.describe())  # This car is a green Lamborghini Revuelto


# # ==========================================
# # 131. MAGIC METHODS - متدهای ویژه
# # ==========================================
# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages


# book1 = Book("Built Wealth Like a Boss", 420)
# book2 = Book("Be Your Own Start", 420)

# # print(len(book1))  # TypeError؛ متد __len__ تعریف نشده است
# print(str(book1))  # نمایش پیش‌فرض اطلاعات شیء
# print(book1 == book2)  # False؛ دو شیء متفاوت هستند


# # ==========================================
# # 132. __LEN__ - تعیین طول شیء
# # ==========================================
# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages

#     def __len__(self):
#         return self.pages  # تعیین مقدار len(book)

#     def __str__(self):
#         return f"'{self.title}' has {self.pages} pages"  # نمایش متنی شیء

#     def __eq__(self, other):
#         return self.pages == other.pages  # مقایسه تعداد صفحات


# book1 = Book("Built Wealth Like a Boss", 420)
# book2 = Book("Be Your Own Start", 420)

# print(len(book1))  # 420
# print(len(book2))  # 420
# print(str(book1))  # 'Built Wealth Like a Boss' has 420 pages
# print(str(book2))  # 'Be Your Own Start' has 420 pages
# print(book1 == book2)  # True؛ تعداد صفحات برابر است


# # ==========================================
# # 133. CART CLASS - ساخت سبد خرید
# # ==========================================
# class Cart:
#     def __init__(self):
#         self.items = []  # لیست محصولات سبد خرید

#     def add(self, item):
#         self.items.append(item)  # اضافه کردن محصول

#     def remove(self, item):
#         if item in self.items:
#             self.items.remove(item)  # حذف محصول
#         else:
#             print(f"{item} is not in cart")  # محصول وجود ندارد

#     def list_items(self):
#         return self.items  # برگرداندن لیست محصولات

#     # ==========================================
#     # 134. __LEN__ - تعداد محصولات
#     # ==========================================
#     def __len__(self):
#         return len(self.items)  # پشتیبانی از len(cart)

#     # ==========================================
#     # 135. __GETITEM__ - دسترسی با اندیس
#     # ==========================================
#     def __getitem__(self, index):
#         return self.items[index]  # پشتیبانی از cart[index]

#     # ==========================================
#     # 136. __CONTAINS__ - بررسی وجود محصول
#     # ==========================================
#     def __contains__(self, item):
#         return item in self.items  # پشتیبانی از in

#     # ==========================================
#     # 137. __ITER__ - قابل پیمایش کردن شیء
#     # ==========================================
#     def __iter__(self):
#         return iter(self.items)  # امکان استفاده از حلقه for


# # ==========================================
# # 138. CART OBJECT - استفاده از سبد خرید
# # ==========================================
# cart = Cart()

# cart.add("Laptop")
# cart.add("Wireless mouse")
# cart.add("Ergo keyboard")
# cart.add("Monitor")

# # پیمایش محصولات با حلقه
# for item in cart:
#     print(item, end=" ")
# # Laptop Wireless mouse Ergo keyboard Monitor

# print(len(cart))  # 4؛ تعداد محصولات
# print(cart[3])  # Monitor؛ محصول با اندیس 3

# print("Monitor" in cart)  # True
# print("banana" in cart)  # False

# cart.remove("Ergo keyboard")  # حذف محصول

# print(cart.list_items())  # ['Laptop', 'Wireless mouse', 'Monitor']

# cart.remove("banana")  # banana is not in cart

# # ==========================================
# # 139. OBJECT ATTRIBUTES - ویژگی‌های شیء
# # ==========================================
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand  # برند خودرو
#         self.model = model  # مدل خودرو

# my_car = Car('Lamborghini', 'Gallardo')

# print(my_car.brand)  # Lamborghini
# print(my_car.model)  # Gallardo

# # ==========================================
# # 140. GETATTR - دریافت ویژگی به‌صورت پویا
# # ==========================================
# # getattr(object, attribute_name, default_value)
# # دریافت مقدار ویژگی؛ در صورت نبودن، مقدار پیش‌فرض برگردانده می‌شود.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person = Person('John Doe', 30)

# print(getattr(person, 'name'))  # John Doe
# print(getattr(person, 'age'))   # 30
# print(getattr(person, 'city', 'Milano'))  # Milano

# # ==========================================
# # 141. GETATTR WITH INPUT - دریافت ویژگی از ورودی
# # ==========================================
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person = Person('John Doe', 30)

# attr_name = input('Enter the attribute you want to see: ')
# print(getattr(person, attr_name, 'Attribute not found'))

# # ==========================================
# # 142. DIR - مشاهده ویژگی‌های شیء
# # ==========================================
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person = Person('John Doe', 30)

# # پیمایش نام ویژگی‌های شیء با dir()
# for attr in dir(person):
#     # نادیده گرفتن متدهای ویژه و متدهای قابل فراخوانی
#     if not attr.startswith('__') and not callable(getattr(person, attr)):
#         value = getattr(person, attr)
#         print(f'{attr}: {value}')

# # Output:
# # age: 30
# # name: John Doe

# # ==========================================
# # 143. SETATTR - ایجاد یا تغییر ویژگی پویا
# # ==========================================
# # setattr(object, attribute_name, value)
# # ایجاد ویژگی جدید یا تغییر مقدار ویژگی موجود

# class Configuration:
#     pass

# # داده‌های دریافت‌شده در زمان اجرا
# settings_data = {
#     'server_url': 'https://api.example.com',
#     'timeout_sec': 30,
#     'max_retries': 5
# }

# config_obj = Configuration()

# # ساخت ویژگی‌ها با استفاده از کلیدها و مقادیر دیکشنری
# for attr_name, attr_value in settings_data.items():
#     setattr(config_obj, attr_name, attr_value)

# print(config_obj.server_url)   # https://api.example.com
# print(config_obj.timeout_sec)  # 30

# # ==========================================
# # 144. HASATTR - بررسی وجود ویژگی
# # ==========================================
# # hasattr(object, attribute_name)
# # اگر ویژگی وجود داشته باشد True و در غیر این صورت False

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# product_a = Product('T-Shirt', 25)

# required_attributes = ['name', 'price', 'inventory_id']

# for attr in required_attributes:
#     if not hasattr(product_a, attr):
#         print(f"ERROR: Product is missing the required attribute: '{attr}'")
#     else:
#         # دریافت ویژگی پس از بررسی وجود آن
#         print(f'{attr}: {getattr(product_a, attr)}')

# # Output:
# # name: T-Shirt
# # price: 25
# # ERROR: Product is missing the required attribute: 'inventory_id'

# # ==========================================
# # 145. DELATTR - حذف ویژگی پویا
# # ==========================================
# # delattr(object, attribute_name)
# # حذف ویژگی مشخص‌شده از شیء

# class UserSession:
#     def __init__(self, user_id, token):
#         self.user_id = user_id
#         self.auth_token = token  # اطلاعات حساس
#         self.temp_counter = 0    # ویژگی موقت

# session = UserSession(101, 'a1b2c3d4e5')

# # ویژگی‌هایی که باید حذف شوند
# attributes_to_clean = ['auth_token', 'temp_counter']

# # حذف ویژگی‌ها در صورت وجود
# for attr in attributes_to_clean:
#     if hasattr(session, attr):
#         delattr(session, attr)
#         print(f'Removed attribute: {attr}')

# print('\nFinal attributes remaining:')

# # نمایش ویژگی‌های باقی‌مانده
# for attr in dir(session):
#     if not attr.startswith('__') and not callable(getattr(session, attr)):
#         print(f' - {attr}: {getattr(session, attr)}')

# # Output:
# # Removed attribute: auth_token
# # Removed attribute: temp_counter
# #
# # Final attributes remaining:
# #  - user_id: 101

# # ==========================================
# # 146. CLASS METHODS - متدهای کلاس
# # ==========================================
# class MusicalInstrument:
#     def __init__(self, name, instrument_type):
#         self.name = name
#         self.instrument_type = instrument_type

#     # متدی برای اجرای یک عمل
#     def play(self):
#         print(f'The {self.name} is fun to play!')

#     # متدی برای برگرداندن اطلاعات
#     def get_fact(self):
#         return f'The {self.name} is part of the {self.instrument_type} family of instruments.'


# instrument_1 = MusicalInstrument('Oboe', 'woodwind')
# instrument_2 = MusicalInstrument('Trumpet', 'brass')

# instrument_1.play()
# print(instrument_1.get_fact())

# # ==========================================
# # 147. CLASS VALIDATION - اعتبارسنجی کلاس
# # ==========================================
# class Planet:
#     def __init__(self, name, planet_type, star):
#         # بررسی رشته بودن تمام ورودی‌ها
#         if not all(isinstance(value, str) for value in [name, planet_type, star]):
#             raise TypeError("name, planet type, and star must be strings")

#         # بررسی خالی نبودن ورودی‌ها
#         if not all(value.strip() for value in [name, planet_type, star]):
#             raise ValueError("name, planet_type, and star must be non-empty strings")

#         self.name = name
#         self.planet_type = planet_type
#         self.star = star

#     # برگرداندن اطلاعات گردش سیاره
#     def orbit(self):
#         return f"{self.name} is orbiting around {self.star}..."

#     # تعیین نمایش متنی شیء
#     def __str__(self):
#         return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


# planet_1 = Planet("Earth", "Terrestrial", "Sun")
# planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
# planet_3 = Planet("Neptune", "Ice Giant", "Sun")

# # چاپ اطلاعات اشیا
# print(planet_1)
# print(planet_2)
# print(planet_3)

# # اجرای متد orbit
# print(planet_1.orbit())
# print(planet_2.orbit())
# print(planet_3.orbit())

# # ==========================================
# # 148. EMAIL SYSTEM - سیستم مدیریت ایمیل
# # ==========================================
# import datetime


# # کلاس ایمیل
# class Email:
#     def __init__(self, sender, receiver, subject, body):
#         self.sender = sender
#         self.receiver = receiver
#         self.subject = subject
#         self.body = body
#         self.timestamp = datetime.datetime.now()
#         self.read = False

#     # علامت‌گذاری ایمیل به‌عنوان خوانده‌شده
#     def mark_as_read(self):
#         self.read = True

#     # نمایش کامل ایمیل
#     def display_full_email(self):
#         self.mark_as_read()
#         print('\n--- Email ---')
#         print(f'From: {self.sender.name}')
#         print(f'To: {self.receiver.name}')
#         print(f'Subject: {self.subject}')
#         print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
#         print(f'Body: {self.body}')
#         print('------------\n')

#     # نمایش خلاصه ایمیل
#     def __str__(self):
#         status = 'Read' if self.read else 'Unread'
#         return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


# # کلاس کاربر
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.inbox = Inbox()

#     # ارسال ایمیل به کاربر دیگر
#     def send_email(self, receiver, subject, body):
#         email = Email(sender=self, receiver=receiver, subject=subject, body=body)
#         receiver.inbox.receive_email(email)
#         print(f'Email sent from {self.name} to {receiver.name}!\n')

#     # نمایش صندوق ورودی
#     def check_inbox(self):
#         print(f"\n{self.name}'s Inbox:")
#         self.inbox.list_emails()

#     # خواندن ایمیل با شماره
#     def read_email(self, index):
#         self.inbox.read_email(index)

#     # حذف ایمیل با شماره
#     def delete_email(self, index):
#         self.inbox.delete_email(index)


# # کلاس صندوق ورودی
# class Inbox:
#     def __init__(self):
#         self.emails = []

#     # دریافت و ذخیره ایمیل
#     def receive_email(self, email):
#         self.emails.append(email)

#     # نمایش فهرست ایمیل‌ها
#     def list_emails(self):
#         if not self.emails:
#             print('Your inbox is empty.\n')
#             return

#         print('\nYour Emails:')
#         for i, email in enumerate(self.emails, start=1):
#             print(f'{i}. {email}')

#     # خواندن ایمیل بر اساس شماره
#     def read_email(self, index):
#         if not self.emails:
#             print('Inbox is empty.\n')
#             return

#         # تبدیل شماره کاربر به اندیس لیست
#         actual_index = index - 1

#         # بررسی معتبر بودن شماره
#         if actual_index < 0 or actual_index >= len(self.emails):
#             print('Invalid email number.\n')
#             return

#         self.emails[actual_index].display_full_email()

#     # حذف ایمیل بر اساس شماره
#     def delete_email(self, index):
#         if not self.emails:
#             print('Inbox is empty.\n')
#             return

#         actual_index = index - 1

#         if actual_index < 0 or actual_index >= len(self.emails):
#             print('Invalid email number.\n')
#             return

#         del self.emails[actual_index]
#         print('Email deleted.\n')


# # تابع اصلی برنامه
# def main():
#     tory = User('Tory')
#     ramy = User('Ramy')

#     # ارسال ایمیل
#     tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
#     ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')

#     # مشاهده، خواندن و حذف ایمیل
#     ramy.check_inbox()
#     ramy.read_email(1)
#     ramy.delete_email(1)
#     ramy.check_inbox()


# # اجرای برنامه فقط هنگام اجرای مستقیم فایل
# if __name__ == '__main__':
#     main()

# # ==========================================
# # 149. BUDGET APP - برنامه مدیریت بودجه
# # ==========================================

# # کلاس دسته‌بندی هزینه‌ها
# class Category:
#     def __init__(self, name):
#         self.name = name
#         self.ledger = []

#     # واریز مبلغ به دسته‌بندی
#     def deposit(self, amount, description=""):
#         self.ledger.append({
#             "amount": amount,
#             "description": description
#         })

#     # برداشت مبلغ از دسته‌بندی
#     def withdraw(self, amount, description=""):
#         if not self.check_funds(amount):
#             return False

#         self.ledger.append({
#             "amount": -amount,
#             "description": description
#         })
#         return True

#     # محاسبه موجودی
#     def get_balance(self):
#         return sum(item["amount"] for item in self.ledger)

#     # انتقال پول بین دسته‌بندی‌ها
#     def transfer(self, amount, category):
#         if not self.check_funds(amount):
#             return False

#         self.withdraw(amount, f"Transfer to {category.name}")
#         category.deposit(amount, f"Transfer from {self.name}")
#         return True

#     # بررسی کافی بودن موجودی
#     def check_funds(self, amount):
#         return amount <= self.get_balance()

#     # نمایش اطلاعات دسته‌بندی
#     def __str__(self):
#         title = self.name.center(30, "*")
#         lines = [title]

#         for item in self.ledger:
#             description = item["description"][:23]
#             amount = f"{item['amount']:.2f}"
#             lines.append(f"{description:<23}{amount:>7}")

#         lines.append(f"Total: {self.get_balance():.2f}")
#         return "\n".join(lines)


# # رسم نمودار درصد هزینه‌های دسته‌بندی‌ها
# def create_spend_chart(categories):
#     chart = "Percentage spent by category\n"

#     # محاسبه مجموع برداشت‌ها
#     total_spent = sum(
#         -item["amount"]
#         for category in categories
#         for item in category.ledger
#         if item["amount"] < 0
#     )

#     percentages = []

#     # محاسبه درصد هزینه هر دسته‌بندی
#     for category in categories:
#         spent = sum(
#             -item["amount"]
#             for item in category.ledger
#             if item["amount"] < 0
#         )

#         if total_spent == 0:
#             percentage = 0
#         else:
#             percentage = int(spent / total_spent * 100)

#         # گرد کردن درصد به پایین‌ترین مضرب ۱۰
#         percentage = percentage // 10 * 10
#         percentages.append(percentage)

#     # رسم محور عمودی نمودار از ۱۰۰ تا صفر
#     for value in range(100, -1, -10):
#         chart += f"{value:>3}| "

#         for percentage in percentages:
#             chart += "o  " if percentage >= value else "   "

#         chart += "\n"

#     # رسم خط افقی نمودار
#     chart += "    " + "-" * (len(categories) * 3 + 1)

#     # پیدا کردن طولانی‌ترین نام دسته‌بندی
#     max_length = max(len(category.name) for category in categories)

#     # نمایش عمودی حروف نام دسته‌بندی‌ها
#     for index in range(max_length):
#         chart += "\n     "

#         for category in categories:
#             if index < len(category.name):
#                 chart += category.name[index] + "  "
#             else:
#                 chart += "   "

#     return chart