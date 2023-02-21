"""arr1 = [1,2,3,4,5]
arr2 = list("wqeasdzxc")
print(arr1, "``", arr2)

arr3 = [i*i for i in range(5)]
arr3 = [i+"~" for i in "cool"]
arr3 = [i*3 for i in "cool"]
arr3 = [i*i for i in range(1,11) if i % 2 == 0]
print(arr3)

customers = ["1chel","2chel","3chel","4chel","5chel"]
problemUser = [i for i in customers if i != "2chel" and i != "4chel"]
print(customers)
print(problemUser)

table = [[x*y for x in range(1,4)] for y in range(1,4)]
print(table)
print(*table)

array1 = ["user", 12, 3.14 , False, True]
print(array1[-1])
print(len(array1))
print(array1[-4:-2])
print(array1[1:3])
print(array1[:-2])
print(array1[2:])
print(array1[0:5:3])
print(array1[::-1])

array1 = [5 ,2 ,9]
array2 = ["asd","zxc","qwe"]
print(sum(array1))
print(sorted(array2))
print(sorted(array1))

arr5 = [123,456]
arr6 = [678,890]
print(arr5 + arr6)
arr7 = [456, 213]
arr8 = [231, 843]
arr7.append("BOB?")
print(arr7)
arr8.insert(1, "TOM?")
arr8.extend(["fff", "TOM?", "ttt"])
print(arr8)
arr8.remove("TOM?")
print(arr8)
arr8.pop()
print(arr8)
arr8.clear()
print(arr8)

del arr8

arr8.count("TOM?")
print(arr8)
arr8.sort(reverse = True)
print(arr8)
"""














