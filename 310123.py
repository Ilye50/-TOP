#\n \t
"""mystr = r"Lorem ipsum '\n' dolor sit amet,"\
        r"consectetur adipiscing elit" \
        r"Lorem ipsum "\
        r"dolor sit amet\, consectetur adipiscing elit"
print(mystr)
str1 = r"\123"
str2 = r"\\123"
str3 = f"{str1 + str2}"
print(str1,str2,str3)
login = input("Get Login: ")"""
"""message = "Your login in sistem as: {name},{age}".format(age = "123",name = "Lo",)
print(message)"""

"""text = "asdasd {0:12.2f}".format(1234.545)"""
"""text = "asdasd {n:b}".format(n = 255)"""
"""text = "asdasd {n:-} {d:-}".format(n = 255,d = -14)"""
"""text = "asdasd {n: } {d: }".format(n = 255,d = -14)"""
"""text = "asdasd {n:^10} {d:>10}".format(n = 255,d = -14)"""
"""text = "asdasd {n:^10.1f} {d:>10}".format(n = 123.124242,d = -14)
print(text)"""

"""from string import Formatter , Template
form  = Formatter()
str5 = "{} asdasdasd {Login} qweqweqwe"
print(form.format(str5 , "Hello" , Login = "SFM"))
templ = Template("$login has rights to &loginRights in the $appName")
suorce = templ.substitute(login = "ADM",
                          loginRights = "RW",
                          appName = "Root App")
print(suorce)"""

"""
. произвольный символ (кроме символа новой строки)
^ начало последовательности символов
$ конец последовательности символов
* любое количество повторений предшествующих символов 0>
+ любое количество повторений предшествующих символов 1>
? 0 или 1 повторение предшествующего символа
{n} n - заданное число повторение предшествующего символа
[] любой символ из перечисленных внутри
\ - экранирование метосимволов
| логическое или
() группировка, выражение рассматривается как один

\d одна десятичная цифра
\D один любой символ кроме десятичной цифры
\s один пробельный символ
\S один не пробельный символ
\w один любой символ (буквы цифры и _)
[^..] - любой символ кроме тех что перечисленны в скобках
\b - начало слова , слева пусто или не буквенный символ
\B - слева и справа буквенные символы
"""
"""part\D001 part#001 part@001
user-\S00[string.digits] user-F004 user-005
\w\w666 ff666 fa666
PYTHON\W PYTHON(!@#$%^&*()?><)
[0-9][1-4 A-Ea-e] asdasdasd'5B'asdasdasd
([^A-Da-d]) (f)(F)
"""
"""user\d{6} user111111
user\d{3,5} user33355
user\d{3,} user11192034920394
user\d{,3} user123
coma? coma coming come com comaa
coma+ comaa comaaaa"""
"""user\d* user user1234567890
user\d+ """
import re, string

"""re.search() "первое совпадение с шаблоном"
re.findall() "все совпадения с шаблоном вернёт список"
re.match() "начало строки"
re.sub()"""
"""str = "My cell phone numbers: Vodafone +38(095)1234567; " \
      "Cellcom +38(067)9875612"
obj = re.search(r"Vodafone \+38\(095\)(\d{7}); Cellcom \+38\(067\)(\d{7})",str)
print(obj.group(1))
print(obj.start(2),obj.end(2))
print(obj.span(2))"""
str = "2021 - 2022 Competition Calendar:30.11.2021" \
      " 2021 Grand Prix Series; 14.01.2022 -" \
      "Grand Pemio D`Italia 03.09.2020"
odj = re.findall(r"\d{2}\.\d{2}\.\d{4}",str)
print(odj)