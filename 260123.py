"""print(mystr[1])
mystr[1] = "DDD"
print(mystr[1])

mystr = "asdfgh 2asdzxcqw 4htnjur"
print(len(mystr))
str1 = mystr.capitalize()
str2 = mystr.title()
mystr.upper()
mystr.lower()
mystr.swapcase()
print(str1)
print(mystr)
print(str2)
print(mystr.count("a", 7 , -1))
print(mystr.find("atysd"))
mystr.rfind("asd")
mystr.index()
mystr.rindex()

print(mystr.endswith("ur"))#True / False
mystr.startswith("последовательность")
mystr.istitle()
mystr.isalnum()#проверка на буквы и цифры
mystr.isalpha()#проверка только на буквы
mystr.isdigit()#проверка только на цифры
mystr.islower()#вся строка ввниз
mystr.isupper()#вся строка вверх
mystr.isspace()#проверка на пробелы
"""

"""str5 = "Lorem"
print(str5.center(11,"~"))
print(str5.expandtabs(tabsize = 4))
print(str5.ljust(20,"~"))
print(str5.rjust(20,"%"))
chislo1 = 12
chislo2 = 13
print("qweasdzxc {0} !! {1}".format(chislo1,chislo2))
str5.lstrip(" ")
arr = []
arr = str5.split("o")
print(arr)"""

import random
import string
alph = string.ascii_letters
digit = string.digits
symb = string.punctuation
temp = alph.lower() + alph + digit + symb
password = ""
for i in range(9):
	p = random.choice(temp)
	password += p
print(f"Ваш новый пароль {password} из [{i + 1}] символов")

if password.isalpha() or password.isdigit():
	del password
