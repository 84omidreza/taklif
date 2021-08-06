import random

while True:
    n = int(input('your n is:'))

    a= random.sample(range(0, 100000000),n)
    print(a)