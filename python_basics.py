
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
 

print("pa")


