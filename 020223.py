"""import re
str = "qqweqweqweqweqeq --- qwe qwe --- -q -- -q - --  ; ;;; ;; ; ; ;  qwe"
re.sub(pattern,repl,obj)
newStr = re.sub(r"[-;]","~",str)
newStr = re.split(r"[-;]+",str)
print(newStr)"""
"""def foo(x,y = 2):
	return x ** y
print(foo(20))"""
"""def funk(x):
	def newFunk(y):
		return x + y
	return newFunk
chisl = funk(100)
print(chisl)
print(chisl(200))
def foo(*args):
	return args
foo(6,5,4,3,2,1,["a","s","d"])
cort = foo(6,5,4,3,2,1,["a","s","d"])
print(type(cort))
cort[0] = "0"
print(cort)
def fooF(**kwargs):
	return kwargs
print(fooF(a="Moscow",b="Berlin",c="Oslo"))"""
"""param = lambda x, y: x + y"""
"""param = lambda **args: args
print(param(asd="asdasd",qwe="qweqwe"))"""

"""chislo = str(input())
chislo = list(chislo)

def add(a,b,c,d,f,g):
	if  a+b+c == d+f+g:
		return True
	else:
		return False

print(add(int(chislo[0]),int(chislo[1]),int(chislo[2]),int(chislo[3]),int(chislo[4]),int(chislo[5])))"""

pole = [[1,2,3],[4,5,6],[7,8,9]]
victor = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
for i in range(3):
	for j in range(3):
		print(pole[i][j])












