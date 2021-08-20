from random import randrange


n = randrange(1000)

while True:
    v = int(input())
    if n == v:
        print("You Win!")
        break
    print('smaller' if (n < v) else "bigger")

#while True:
   # print("You Win!")   This would print "You Win" forever 