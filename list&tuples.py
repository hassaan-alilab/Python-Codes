#this file covers list & tuple along with readme to understand what they are conceptually
#creation of list
#only difference between list and strings lists are mutable
#only diff between list and arrays is types of data can be different inside a single list
#supports -ve indexing as well 
#supports list slicing as strings as well

'''a = [1,3,8,4,5]
print(a)
#slicing
print(a[0])
print(a[-1])#-ve indexing will print last
print(a[0:5])#of we do 0:4 then it will left our last number
#basic functions of list
a.append(6)#add this element at last
print(a)
a.sort()#sort the given list in ascenduing order 
print(a)
a.sort(reverse=True)#in descending order 
print(a)
a.sort()#sorting back for furthre operations
print(a.count(3))#print the no of occurence of a specific number
a.insert(1,7)
print(a)#this will move all values at i+=1 index
a.pop()
print(a)#removing the last digit 
a.remove(7)
print(a)#this will remove the value  7 and will move the other value at i-=1
a.reverse()
print(a)#reverses the whole list 
print(len(a))#print length of reverse'''

#tuples
#now we will discuss about tuples
#creation of tuples just use ( ) braces instead of []

"""tup =(1,4,3,2,6,7,8)
print(tup)
print(type(tup))
#if we didn't use "," in single value declaration in a tuple.python  will treat it  as integer/float/string etc not type tuple.
atup=(1,)#that is the declaration of single value
print(atup)
print(type(atup))
#follows the same string slicing as of strings and lists
print(tup[1:3])
#Methods 
print(tup.count(1))#shows count
print(tup.index(3))#index of first occurence
"""
#practice Questions 
'''#Q1.WAP to ask for 3 fvt movie names and store them in list
print("Please Enter 3 Fvrt movie names : ")
movienames=[]
for i in range(3):
   movie =input(f"Movie No {i+1} :")
   movienames.append(movie)

print("Names Saved inside a list ")
print(movienames)
'''

#Q2.WAP to check if a list contains a palindrome or not 
lwpal=[1,2,3,2,1]
c=lwpal.copy()
c.reverse()
if c !=lwpal:
   print("Not a Palindrome ")
else:
   print("Contains a Palindrome")

#Q3.WAP to count students with gade A in the following tuple
grade=('A','A','B-','B+','A',"A-",'A+')
print(type(grade))
print("Here are the number of students with Grade-A : ")
print(grade.count("A"))

#Q4.Sort the above given tuple from A to D
#the wrong approach is given below bcz tuuples didn't support .sort() method we  will use lis for it

'''grade.sort()
print(grade)'''

#the correct way of working
#first we will copy tuple in list form
gradelist=list(grade)
gradelist.sort()
print(gradelist)
