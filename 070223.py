"""def funk(variable):
	res=[]
	for i in range(len(variable)-1,-1,-1):
		res.append(variable[i])
	res=''.join(res)
	return res
n = reversed(input())
print(n)"""
"""board = [['*' for i in range(8)] for j in range(8)]
board[0][0] = "Rook"
for item in board:
	print(item)"""
import random as rnd
"""temper = [[rnd.randrange(14,60) for hour in range(24)] for day in range(30)]
for item in temper:
	print(item)"""

"""total = []
for i in temper:
	sum = 0
	for j in i:
		sum += j
	else:
		total.append(sum / 24)
print(total)"""

"""high = -273
for item in temper:
	for temp in item:
		if temp > high:
			high = temp
print(f"Higest temperature is {high}")"""

#Работает()
"""koolvoDnei = 0
for i in range(30):
	if temper[i][15] > 16:
		koolvoDnei += 1
print(f"Дней когда температура 16:00 была выше 16 градусов: {koolvoDnei}")"""

"""hotell = [[[rnd.choice([1,0])for r in range(20)] for floor in range(30)] for corps in range(3)]
hotell[0][24][2] = False

for i in hotell:
	print(i)

ncorp = int(input())
etax = int(input())
komnata = 0
def foo(x,y = 1):
	for i in  """

"""def factor(x):
	if x <= 0:
		return 1
	else:
		return x * factor(x - 1)
print(factor(4))"""

def fibanfchiN(x):
	if x < 2:
		return x
	else:
		return fibanfchiN(x - 1) + fibanfchiN(x - 2)
print(fibanfchiN(10))
