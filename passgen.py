import random
import string

def randomPassword():
    chars = string.ascii_letters + string.digits
    size = 3
    return ''.join(random.choice(chars) for x in range(size,10))

n = 0 
while n < 30:
    print(randomPassword())
    n=n+1