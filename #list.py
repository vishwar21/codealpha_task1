#list

a=["Hello",5,True]
print(a[-2 :])

a.insert(2,False)
print(a)

a.remove("Hello")  #for remove cant use index only string

a="10 4 1 2 3 4 5 6 7 8 9 10"
arr=list(map(int, a.split()))
print(arr)
n=arr.pop(0)
