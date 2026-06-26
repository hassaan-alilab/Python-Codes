'''#in this file we will practice dictionary and sets
#we are starting with dictionary
#used to store key:value pairs in a data structure
#we can save tuples and lists inside a dictionary ......
#creation
dict={}#empty dictionary
#print(dict)
#simple dictionary
dict={"name":"Ali Hassaan",
      "marks":"95.4",
      "section":"SE-4B"
    }
print(dict)

#when keys have multiple values
dict={"name":"Ali Hassaan",
      "marks":"95.4,89.3,93.2",
      "section":"SE-4B"
    }
print(dict["marks"])#if we input wrong key it willl throw an error so that's we prefre to use function given below
print(dict.get("marks"))#it will print an error and code after it will execute

#Nested dictionary means we are saving a dictionary inside a dictionary like lists,tuples etc
dict={
    "name":"Ali Hassaan",
    "class":"SE-4B",
    #to save courses with marks obtain
    "result": {"DB":"91.4",
              "OS":"78.5",
              "PST":"90.3"
            }
}
print(dict)
print(dict["result"]["OS"])#printig from specific address

#methods
print(dict.keys())#main keys not nested one
print(dict.values())#bringd all values
print(dict.items())#all items in key value pairs
print(dict.get("name"))#to print specific key value pair from dictionary
dict.update({"section":"SE-4B"})#used to add new key value pairs
print(dict)'''

#Here we go with the Sets
#sets will never contain duplicates
#sets are mutable and it's element are immutable that's why we can't add lists and dictionary 
# we don't add mutable elments in set because because they effect our hashing facility whenever a new change occurs we have to hash each change differently 
#means if 5-changes are occured we have to hash all those 5 changes one by one
#mainly these are used to remove duplicates from data
#sets are unordered means there are no indexes
'''lis=[1,2,2,2,2,4,5,4,6,7,7,8,7,8]
print(type(lis))
s=set(lis)
print(type(s))
print(s)#all duplicates will be removed from a list through type casting and set operations
'''

#creation of sets
s ={1,2,3,2,2,5,6,7,8,4,5}
#creating null set
ns=set()
print(type(ns))
#Methds
s.add(9)#adds value in set
s.remove(8)#remves specific item
print(s)
#emptieses the set it will delete all values of a set
#s.clear()

#deletes a random value
s.pop()
print(s)
set1 ={1,2,3,4,2,3,4,6,7,8,9}
set2={13,12,14,15,16,17,1,2,3,4}
print(set1.intersection(set2))#takes intersection
print(set1.union(set2))#takes union same as math and removes same values
