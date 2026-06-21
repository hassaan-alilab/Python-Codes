def rtriangle(length):
    print(f"Printing triangle of length {length}")
    i,j=1,0
    for i in range(1,length+1):
      for j in range(i):
        print("*",end=" ")
      print()
def square(len):
    print(f"Printing Square of length {len}")
    for i in range(len):
      for j in range(len):
          print("*",end="")
      print()
def altrnoftriangle(le):
    print(f"triangle with alternative method of length {le} ")
    for i in range(1,le+1):
       print("*" * i)
    print()

def invtriangle(leng):
   print(f"Printing inverted triangle {leng}")
   for i in range(leng,0 ,-1):
       print("*" * i)
   print()
#invtriangle(5)
#here our time complexity is O(n^3)
def ltriangle(len):
    print(f"Printing left trianlge of length {len}")
    for i in range(1, len + 1):
      
        for k in range(len-i):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        print()
#ltriangle(5)
#let's do some alternatiive method with time complexity O(n)
def altltriangle(len):
   print(f"Printing Inverted Trianlge with Alternative of length {len}")
   for i in range(1,len+1):
      space=" " *(len -i)
      stariks="*"*i
      print(space + stariks)
#altltriangle(5)
def pyramid(length):
    #code works for only odd sizes with time complexity O(n)
    print(f"Printing triangle of length {length}")
    if length % 2 != 0:
        for i in range(1, length + 1, 2):
        
            spaces = " " * ((length - i) // 2)
            stars = "*" * i
            print(spaces + stars)
pyramid(8)

 #let's do so,ething crazy witht his code and turn it into generic version with O(n
def gpyramid(len):
    print(f"Generic Code for Pyramid of length {len}")       
    if len % 2 !=0 :
        for i in range(1,len+1,2):
            spaces=" " *((len -i )//2)
            starik=((i*2+1)* "*")
            print(starik+spaces)
    else:
        for i in range(2, len + 1, 2):
            spaces = " " * ((len - i) // 2)
            stars = "*" * i
            print(spaces + stars)

gpyramid(6)     
        

