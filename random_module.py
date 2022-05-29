import random

print(random.randint(2,6))
print(random.randrange(2,6))
print(random.random())     #return float btw 0-1
print(random.uniform(2,5)) # retun float

l=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(l)
print(l)

p=[4,3,24,5,6,7,8,9,10]
c=random.choice(l)
print(c)