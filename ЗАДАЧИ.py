

# 🟢 Задача 1 — Магазин фруктов

# Есть строка:

# apple 10 banana 5 apple 7 orange 8 banana 6 apple 3

# Напиши функцию:

# def fruits(text):
#     items = text.split()

#     s = {}

#     for i in range(0, len(items), 2):
#         name = items[i]
#         score = items[i + 1]
    
#     total = 0 
#     for i in s:
#         total = sum(s[i])

#     best = None
#     minst = 0 

#     for i in s:
#         if s[i] > minst:
#             minst = s[i]
#             best = i 
#     # return("k": s
#            "total": total,
#            "best": best,
#            "minst": minst)

# w = fruits("hassan 10 mango 20 appel 30")
# print(w)




# def drinks(text):
#     name = text.split()

#     s = {}

#     for i in range(0, len(name), 2):
#         data = name[i]
#         score = int(name[i + 1])

#         if data in s:
#             s[data].append(score)
#         else:
#             s[data] = [score]

#     total = {} 
#     for i in s:
#         total[i] = sum(s[i])

#     big_name = None
#     big_score = 0 

#     for i in total:
#         if s[i] > big_score:
#             big_score = s[i]
#             big_name = i 
#     min_score = float("inf")
#     min_name = None

#     for i in total:
#         if s[i] > min_score:
#             min_score = s[i]
#             min_name = i 

#     avg = {}

#     for i in s:
#         avg[i] = sum(s[i]) / len(s[i])

#     count = len(s)

#     count_score = 0 

#     for i in s:
#         count_score += len(s[i])

#     return {"products": s,
#            "total": total, 
#            "big_name": big_name,
#            "big_score": big_score,
#            "min_score": min_score,
#            "min_name": min_name,
#            "avg": avg,
#            "count": count,
#            "count_score": count_score}

# s = drinks("mango 10 arbyz 2 appel 300")
# print(s)    




# Есть строка:

# apple 10 5 banana 20 2 apple 15 3 orange 8 10 banana 25 4 apple 12 6

# Каждые 3 элемента — это:

# товар
# цена
# количество
# 🟢 Шаг 1 (только его)

# Напиши функцию:

# def shop(text):

# Внутри:

# сделай split();
# создай пустой словарь;
# пройди по данным циклом с шагом 3;
# собери словарь такого вида:
# {
#     "apple": [
#         [10, 5],
#         [15, 3],
#         [12, 6]
#     ],
#     "banana": [
#         [20, 2],
#         [25, 4]
#     ],
#     "orange": [
#         [8, 10]
#     ]
# }

# Пока ничего больше не считай.




# def shop(text):

#     names = text.split()

#     items = {}

#     for i in range(0, len(names), 3):
#         data = names[i]
#         score = int(names[i + 1])
#         count = int(names[i + 2])

#         if data in items:
#             items[data].append([score, count])
#         else:
#             items[data] = [[score, count]]
#     return items
# s = shop("hasan 9 0 usama 10 8 omar 11 8")
# print(s)




# def scores(text):
#     names = text.split()

#     s = {} 

#     for i in range(0, len(names), 3):
#         data = names[i]
#         score = int(names[i + 1])
#         count = int(names[i + 2])

#         if data in s:
#             s[data].append([score, count])
#         else:
#             s[data] = [[score, count]]
#     revenue = {}

#     for name in s:

#         total = 0 

#         for d in s[name]:
#             w = d[0]
#             q = d[1]

#             total += w * q
#         revenue[name] = total 
#     return revenue

# g = scores("hasan 2 4 usama 4 6 papa 7 9")        
# print(g)

# 📌 1. Создай словарь
# revenue = {}
# 📌 2. Пройди по товарам
# for name in items:
# 📌 3. Для каждого товара:
# возьми список [price, count]
# посчитай:
# price * count
# сложи всё в сумму
# 📌 4. Запиши результат
# revenue[name] = total
# 🧠 ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

# Для теста:

# shop("hasan 9 0 usama 10 8 omar 11 8")

# ожидаемый результат:

# {
#     "hasan": 0,
#     "usama": 80,
#     "omar": 88
# }




# 🚀 ЗАДАЧИ НА СЛОВАРИ (УРОВЕНЬ 2)
# 🟢 Задача 1 — Фрукты (база)
# apple 10 banana 5 apple 15 orange 7 banana 3 apple 8
# 📌 нужно:
# собрать словарь:
# {
#     "apple": [10, 15, 8],
#     "banana": [5, 3],
#     "orange": [7]
# }
# найти сумму каждого фрукта
# найти самый дорогой фрукт (по сумме)







# def scores(text):

#     names = text.split()

#     s = {}

#     for i in names:
#         if i in s:
#             s[i] += 1
#         else:
#             s[i] = 1

#     return s
# p = scores("papa mama papa mam mama pap pap pap pap")
# print(p)







# def scores(nums, target):
   
#     left = 0 
#     right = len(nums) - 1

#     while left < right:
#         t = nums[left] + nums[right]

#         if t == target:
#             return True, t
#         elif t < target:
#             left += 1
#         else:
#             right -= 1
#     return False 
# p = scores([1,2,3,4,5,6,7], 10)
# print(p)


# for i in range(len(nums)):

#     print("current:", nums[i])

#     # прошлые
#     for j in range(0, i):
#         print("  past:", nums[j])

#     # будущие
#     for j in range(i + 1, len(nums)):
#         print("  future:", nums[j])




# def scores(nums, target):

#     left = 0 
#     right = len(nums) - 1

#     while left < right:
#         d = nums[left] + nums[right]

#         if d == target:
#             print("число нашли ураа")
#             return True
#         elif d < target:
#             left += 1
#         else:
#             right -= 1
#     return False, "nooo"

# w = scores([1,2,3,4,5,6,7], 10)
# print(w)








# def scores(text):
#     left = 0 
#     for i in range(len(text) - 1):
#         d = text[i] > text[i + 1]
#     return d 
# s = scores([1,3,4,5,1,3,2,1])
# print(s)


# def generator_number(text):

#     for i in range(len(text)):

#         s = False 

#         for j in range(+ 1, len(text)):

#             if text[j] > text[i]:
#                 print(text[i], ">", text[j])
#                 s = True 
#         if not s:
#             print(text[i], ">", "no")
# w = generator_number([1,2,3,4,1,3,4,5,6,1])
# print(w)





# def scores(nums):

#     for i in range(len(nums)):

#         found = False 

#         for j in range(i + 1, len(nums)):
#             if nums[j] > nums[i]:
#                 print(nums[i], "nashol", nums[j])
#                 found = True
#                 break 
#         if not found:
#             print("ne nashol")
# s = scores([1,2,3,4,1,5,7,13,4])
# print(s)









# def scores(text):

#     for i in range(len(text)):

         
#         found = False 

#         for j in range(i + 1, len(text)):
#             if text[j] > text[i]:
#                 print(text[i], ">", text[j])
#                 found = True 
#             break 

#         if not found:
#             found = False 

# s = scores([1,2,3,4,1,5,6,1])
# print(s)




# def next_greater(nums):

#     for i in range(len(nums)):

#         found = False

#         for j in range(i + 1, len(nums)):

#             if nums[j] > nums[i]:
#                 print(nums[i], "->", nums[j])
#                 found = True
#                 break

#         if not found:
#             print(nums[i], "-> нет")


# next_greater([3, 1, 4, 2, 5])

# def next_smaller(nums):

#     for i in range(len(nums)):

#         found = False

#         for j in range(i + 1, len(nums)):

#             if nums[j] < nums[i]:
#                 print(nums[i], "->", nums[j])
#                 found = True
#                 break

#         if not found:
#             print(nums[i], "-> нет")


# next_smaller([5, 2, 8, 1, 6])






# def scores(text):

#     sum_text = text[0] + text[1]

#     first = text[0]
#     second = text[1]

#     for i in range(len(text) - 1):
#         currect = text[i] + text[i + 1]

#         if currect > sum_text:
#             sum_text = currect
#             first = text[i]
#             second = text[i + 1]

#     return first, second, sum_text
# s = scores([1,4,5,6,7,8,9,0])
# print(s)




def scores(text):

    for i in range(len(text)):

        found = False 

        for j in range(i + 1, len(text)):
            if text[j] > text[i]:
                found = True
                print("число", text[i], "больше", text[j])
                break 
        if not found:
            print("число", text[i], "меньше", text[j])
s = scores([1,3,4,1,4,3,2,5,6,7,8,10,12,43,4,1,44])
print(s)