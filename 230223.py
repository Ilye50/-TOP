"""class Transport:
	def __int__(self):
		self.__name = "Car"
		
	def get_name(self):
		self.__name = str(input())
		return  self.__name

object_transport = Transport()
print(object_transport.name)
object_transport.get_name()
print(object_transport.get_name())"""

"""class Stack:
	def __init__(self):
		self.__stacklist = []
		
		
	def getList(self):
		return self.__stacklist

	def push(self, coin):
		self.__stacklist.append(coin)
	def pop(self):
		coin = self.__stacklist[-1]
		self.__stacklist.pop()
		return coin


class SumStack(Stack):
	def __init__(self):
		Stack.__init__(self)
		self.__sum = 0
	
	def getSum(self):
		return self.__sum
	def push(self, coin):
		self.__sum += coin
		Stack.push(self, coin)

	def pop(self):
		coin = Stack.pop(self)
		self.__sum -= coin
		return coin

myStack = Stack()
myStack.push(1)
myStack.push(5)
myStack.push(3)
print(myStack.pop())

obj_coin = SumStack()
for i in range(1, 5):
	obj_coin.push(i)


print(obj_coin.pop())
print(obj_coin.pop())
print(obj_coin.getSum())

print(obj_coin.getList())

print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(100):
	obj_coin.push(5)
	
print(obj_coin.getList())
print(obj_coin.getSum())
"""

"""class Drob:
	def __init__(self):
		self.__chisl = int(input())
		self.__znamen = int(input())
	def getSum(self):
		return int(self.__chisl) + int(self.__znamen)
	def getMinus(self):
		return int(self.__chisl) - int(self.__znamen)
	def getChasn(self):
		return int(self.__chisl) / int(self.__znamen)
	def getProis(self):
		return int(self.__chisl) * int(self.__znamen)

myDrob = Drob()
print(myDrob.getSum(),myDrob.getMinus(),myDrob.getChasn(),myDrob.getProis())"""


class Car:
	def __init__(self):
		self.__carName = str(input())
		self.__carDr = str(input())
		self.__carPro= str(input())
		self.__carVD = str(input())
		self.__carColor = str(input())
		self.__carPrise = str(input())
		self.shotchuck = 0
	def getCarName(self):
		self.shotchuck += 1
		return self.__carName
	def getCarDr(self):
		self.shotchuck += 1
		return self.__carDr
	def getCarPro(self):
		self.shotchuck += 1
		return self.__carPro
	def getCarVD(self):
		self.shotchuck += 1
		return self.__carVD
	def getCarColor(self):
		self.shotchuck += 1
		return self.__carColor
	def getCarPrise(self):
		self.shotchuck += 1
		return self.__carPrise
	def getCarInfo(self):
		carInfo = [self.getCarName(),self.getCarDr(),self.getCarPro(),self.getCarVD(),self.getCarColor(),self.getCarPrise()]
		return carInfo
myCar = Car()
print(myCar.shotchuck)
print(myCar.getCarName(),myCar.getCarDr(),myCar.getCarPro(),myCar.getCarVD(),myCar.getCarColor(),myCar.getCarPrise())
print(myCar.shotchuck)
print(myCar.getCarInfo())
print(myCar.shotchuck)
