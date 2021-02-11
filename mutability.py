"""
Mutable :
هي امكانيه تغير القيمه للمتغير
Immutable:
غير ممكن تغير القيمه للمتغير



Mutable Object:
list, dict, set

Immutable Object:
Integer, float, string, tuple, bool , frozenset
"""



# Example in Mutable Objects:

# list
sami = []
sami.append(1)
sami.append("Hello")
sami.append("For")
sami.append(True)

print('Mutable list: Before change=> ', sami)

sami[1]= 'No'
sami[3]= 'No'

print('Mutable list: After change=> ', sami)


# Immutable Objects:

yes = 1
print('yes before change: ',yes)
print('yes id: ',id(yes))
yes = 2
print('yes after change: ',yes)
print('yes id: ',id(yes))




class Mutability:
    def __init__(self, id=None):
        self.id = id
    def get_id(self):
        if self.id is not None:
            return print(self.id)
        return None
    def set_id(self, id):
        self.id = id
    def get_id_addresses(self):
        if self.id is not None:
            return print(id(self.id))
        else:
            return None


mu = Mutability()



mu.set_id(1)
mu.get_id()
mu.get_id_addresses()
print(id(mu))

mu.set_id(2)
mu.get_id()
mu.get_id_addresses()
print(id(mu))



# tuple

jack = 1,2,'Yes', 'No'

# print('jack clothes: ', jack)
# print('jack type: ', type(jack))

jack[2] = 4
print(jack)



