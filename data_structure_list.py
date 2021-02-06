"""
Data Structure in Python:
هياكل البيانات في البايثونّ
    * List  ليست
    * Tuples  تيوبليس
    * Dic  ديكشنريس
    * sets  سيت
    * Frozensets فروزن سيت
"""


"""
1. list
"""

# create list
sami = []
print('create new list `sami`, show type of sami list: ', type(sami))

"""
This is comments

Methods with list:
الاوامر والدالات المرتبطه باللست :
    * append() - اضافه عنصر ما الى اللست
    * extend() - اضافه كل عناصر** اللست الى لست اخرى
    * insert() - اضافه** عنصر جديد **حسب الفهرس او الموقع المحدد في اللست
    * remove() - حذف عنصر ما من اللست
    * pop() -  اخذ عنصر من اللست  وحذفه من نفس اللست مع امكانيه ربطه بمتغير اخر 			
    * clear() - حذف جميع العناصر في اللست
    * index() - اظهار موقع العنصر في اللست			
    * count() - اظهار عدد تكرار العنصر في اللست
    * sort() - ترتيب العناصر بشكل تصاعدي			
    * reverse() - عكس ترتيب العناصر في اللست		
    * copy() - نسخ العناصر في اللست
			

"""

# method append in list
sami.append(1)
sami.append('Hello World')
sami.append(False)
print('method append to sami list:', sami)


# method extend in list
# create new list
sami2 = []



# method extend new list(sami2) with previous list(sami)
sami2.extend(sami)
print('method extend sami2 using sami: ',sami2)



# method insert in list
sami2.insert(0, 'new fish')
sami2.insert(3, 'added now')
print('method insert to `sami2`: ', sami2)


# method remove - an item from list by value
sami2.remove('new fish')
print("method remove - `new fish`  from sami2 list: ", sami2)


# method pop
item = sami2.pop(3)
print('method pop, from sami2 list: ', sami2)
print('method pop item and return it to new item: ', item)
print('item type', type(item))


# method clear - remove all items in list
sami2.clear()
print('method clear - sami2 list clear', sami2)


# method index
# first append new items from 0 to 10
for i in range(0,10):
    sami2.append(str('#'+str(i)))




print('append new items to sami2 list: ',sami2)

# return index number of key value
print('method index - return index number of key: ', sami2.index('#2'))


# method count - return number of repate item in list
# append item already in list

sami2.append('#0')
sami2.append('#0')
sami2.append('#0')
sami2.append('#1')
sami2.append('#0')
print('sami after append new items', sami2)
print('method count #0: ', sami2.count('#0') )
print('method count #1: ', sami2.count('#1') )

# method sort, keep in mind it worked out only with same items not mixed items

sami2.sort()
print('method sort :',sami2)


# NOTE:
# error raise if we try append integer value
# so be careful, but it can be fixed, later will go deeper
# sami2.append(2)
# sami2.sort()
# print(sami2)

# method reverse, just reverse items
sami2.reverse()
print('method reverse :', sami2)


# method copy , shallow copy of items in list
tabogah = sami2.copy()

print('method copy: ',tabogah)


"""
2. Tuples
"""
