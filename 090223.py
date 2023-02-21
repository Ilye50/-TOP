"""four = lambda : 4
sqr = lambda x: x * x
pwr = lambda x, y: x ** y
for i in range(-4 , 4):
	print(sqr(i),end = " ")
	print(pwr(i,four()))

def printF(args, fun):
	for x in args:
		print(f"F({x}) = {fun(x)}")

def polynom(x):
	return (2 * x ** 2) - (4 * x) +2

printF([x for x in range(-4,4)],lambda x:(2 * x ** 2) - (4 * x) +2)

list1 = [x for x in range(6)]
list2 = list(map(lambda x: x ** 2,list1))
print(list2)
for x in map(lambda x: x ** x,list2):
	print(x)
"""

"""def moveTower(n,start,finish):
	if n == 1:
		print(f"Перенести диск {n} с {start} на {finish}")
	else:
		kol = 6 - start - finish
		moveTower(n-1,start,kol)
		print(f"Перенести диск {n} с {start} на {finish}")
		moveTower(n-1,kol,finish)

moveTower(6,1,3)
#(((1*2+1)*2+1)*2+1)*2+1
"""
import random
chislo = [random.randrange(0,101) for i in range(100)]
chislo = sorted(list(chislo))
print(chislo)
chislo = chislo
print(chislo)










