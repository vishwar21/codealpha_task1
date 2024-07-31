

#a="Hello World"
#print(a[4:-1])

#ascii value
print(ord('a'))

a="abc"
print(a[-1])
last=a[-1]
temp=(ord(last)-ord('a')+3)%26+ord('a')
print(temp)
print(chr(temp))

#split 
a="Hello hii bro"
print(a.split(" "))

#strip for removing the space
a=    "heloo world    "
print(a.strip())

#i need to remove index  use find function is used to find the index of the string
#a="hello world"
#print(a.find('v'))   #-1 no such word in the string

#len and count len is used to finfd the total length of the string
a="hello world"
print(len(a))

print(a.count('l')) #count is used to count how many times the letter has occured

a="Hello World"
print(a.swapcase())  #it swaps the letters lower into capital and capital into small


# isAlpha and isDigit isalpha used to find letters and isdigit ti find the numbers

#a="Hello %7 World"
#for i in a:
 #   if i.isalpha() :
#        print(i)
#a="hello world"
#  #rint(a.replace("world","MCA"))
#print(a.replace("," " "))

