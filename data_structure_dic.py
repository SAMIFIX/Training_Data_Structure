"""
Data Structure in Python:
هياكل البيانات في البايثونّ
    * List  ليست
    * Tuples  تيوبليس
    > Dic  ديكشنريس
    * sets  سيت
    * Frozensets فروزن سيت
"""


"""
3. Dictionaries

Methods in dic:
    * clear
    * copy
    * fromkeys
    * get
    * items
    * keys
    * pop
    * popitem
    * setdefault
    * update
    * values

"""

# create dic
fish = {
    'key':'value'
}
# show type
print(type(fish))

jack = {
    'upper':'head',
    'down':'football shoes'
}

# print(jack.values())

jack.update({'upper':'hair', 'No':'Yes'})

keys = {'upper', 'down'}
values = 'Hair'

jack_mother = jack.fromkeys(keys, values)

print('jack_mother',jack_mother)


jack_son = jack_mother.copy()

print('jack_son',jack_son)


# pop item value from key
item = jack_mother.pop('upper')
print(item)

# pop from right side key and value
item2 = jack.popitem()
print(item2)


print(jack.get('upper'))


