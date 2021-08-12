# print('khaled-python')

# if 5>2 :
#  print('five is greater than two ')


# x=5
# y=3
# s= 'Hello,Word'
# print(x+y,s)

# a=str(4)
# z=int(4)
# c=float(4)

# print(a,z,c)
# print(type(a),type(z),type(c))

# fos = ['banana','apple','ornge']
# x,y,z=fos
# print(x,y,z)


# def myfunc():
#     global A,C,B
#     A= "Khaled"
#     C=' '
#     B= "Ali"
#     a=A.upper()+C.upper()+B.upper()
# myfunc() 
# a = 'khaled ali code'
# if 'khaled' in a :
#     print('yes',a[0:5])

# print("naie" not in a)
# v=a.replace(" ", "|")
# b=a.split("|")
# # print(a.replace(" ", "|"))
# print(a,v,b)

# age = 30
# FN = "Khaled Naie {}"
# print(FN.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# x='i want to pay {2} dollars for {0} pieces of item {1}'
# print(x.format(quantity,price,itemno))

# txt = "khal \ted"
# print(txt)

# txt = "khal \bed"
# print(txt)


# x=["apple", "banana", "cherry"]
# X=["pineapple", "papaya"]
# x.extend(X)
# c = x
# i=0
# # c.remove("mango")
# # c.pop(2)
# # del c[0]
# # c.clear()
# while i < len(c)  :
#     print(c[i])
#     i= i +1

# [print(k) for k in c]
# new = []
# for d in c :
#     if "a" or "e" in d :
#         new.append(d)
# print(new)


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]
# newlist1 = [x for x in range(10) if x < 5]
# newlist2 = [x.upper() for x in fruits]
# newlist3 = ['hello' for x in fruits]
# newlist4 = [x if x != "banana" else "orange" for x in fruits]
# fruits.sort()

# print(newlist,newlist1,newlist2,newlist3,newlist4,fruits)


# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# g =  ["apple", "banana", "cherry"]
# mylist = list(g)
# print(mylist)

# v=["apple", "banana", "cherry"]
# mylist = v.copy()
# print(mylist)


x = ("apple", "banana", "cherry")
print(x)
y = list(x)
print(y)
y[1] = "kiwi"
x = tuple(y)

print(x)