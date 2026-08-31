x = 2
y = 3
z = 4

x + y * z # worst way to write any code
(x + y) * z # more readable 

40 + 2.23
print(40 + 2.23) # make sure both must have same data type

'hitesh' + 3 # worst code
int(2.23) or flot(40)

#operator overloading
'chai' + 'code' -> 'chaicode'

x, y, z
(2, 3, 4) #tuple # result of above line 
# when you use 2 or more variable as a comma separator  together then result will be come in form of tuple

#
repr('chai') -> "'chai'"
str('chai')  -> 'chai'
print('chai') -> chai

# math functions
import math # must install this library to utilize predifine methos

math.floor(3.5)  -> 3
math.floor(-3.5) -> 4
math.floor(3.9)  -> 3

math.trunc(2.8)  -> 2
math.trunc(-2.8) -> -2

#
oct(64) -> give octun value of 64
hex(64) -> give us hexa value of 64
bin(64) -> give us binary value of 64

int('64',8)  -> give us octul value of 64 # other way to find octan value
int('64',16) -> give us hexa value of 64
int('64',2)  -> give us binary value of 64

# left shift
x = 1
x << 2 # do left shift by 2 bit 

# random

import random

random.random()
random.randint(start,end) -> random.randint(1,10)

l1 = ['lemon', 'masala', 'ginger', 'mint']
random.choice(l1) -> every time randome value comes but from l1 list

random.shuffle(l1) -> whenever you execute this line every time shuffle method will shuffle you l1 randomly

-- from decimal import Decimal 
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') -> Decimal('0.3')
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') -> Decimal('0.0')

-- from fractions import Fractions 
myFra = Fractions(2, 7)










