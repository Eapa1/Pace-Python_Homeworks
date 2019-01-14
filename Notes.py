###Declaring a lists
##num= [2,5,8,10]
##print(num)
##name= ['A1', 'BO', 'Mia', 'Di']
##print(name)
##num2 = list (range(5))
##print(num2)
##
##num3= [0] * 5
##print(num3)
##
##name2= ['jane','john'] * 2
##print (name2)

###Iterating over a list
##lst= [22,29,35,40,50]
##for i in lst:
##    print(i)

###Length Function
##lst=[22,29,35,40,50]
##n=len(lst)
##print(n)

###List are mutable
##lst=[22,29,35,40,50]
##print(lst)
##lst[0]=2
##lst[1]=5
##print(lst)

###Concatnating
##lst1=[22,29,35,40,50]
##lst2=[3,5,6,11,15]
###lst3= lst1+lst2
###print(lst3)
##lst1 += lst2
##print(lst1)
##print(lst1)

#Slicing
##lst=[22,29,35,40,50]
##print(lst)
##print(lst[1:3] #Create a slice from the index 1 to index 3
##print(lst[0:3])
##print(lst[:3])
##print(lst[-3:])
##print(lst[2:5])
##print(lst[2:5])
##print(lst(:))
##print(lst[2:7])


##num=[1,2,3,4,5,6,7,8,9,10]
##print(num[1:8:2])

#Finding items with in operator
##def main():
##    cars= ['Audi', 'Honda', 'BMW', 'Lexus', 'Ferrari']
##    search= input('search for car brand:')
##    if search in cars:
##        print('Found', search)
##    else:
##            print("Didn't find", search )
##main()

#Build in Functions
#Append:
##names=['Ann', 'Brad', 'Chou']
##names.append ('David')#Append=Add
##print(names)

#Empty List
##list1=[]
##list1.append('jane')
##print(list1)
##list1.append('john')
##print(list1)

#While statement
##num = [5, 9,16,21,28]
##i=0
##while i<4:
##    print(num[i])
##    i +=1


#Insert Method
#Insert at a specific position. If inserted in the middle.
#The elements on the right will move right.
##list1= [1,3,4,7,8]
##print(list1)
##list1.insert(0,5)
##print(list1)
##list1.insert(3,12)
##print(list1)



###Sort
##list1 = [1,9,4,7,12]
##list1.sort()
##print(list1)

#Sort & reverse
##list1= ['GOOG', 'TWTR', 'FB', 'SNAP']
##list1.sort()
##print(list1)
##list1.reverse()
##print(list1)

#Delete (deletes using index number)
##list1=['monday',22 ,30 ,45]
##print(list1)
##del list1[2]
##print(list1)

#Max/min Value
##names=['spring', 'summer', 'Fall','winter']
##print(names)
##print(max(names))
##num = [5,9,16,21,28]
##print(max(num))
##print(min(names))
##print(min(num))

#Copying a list
##list1=[1,2,3,4]
##print(list1)
##list2= list1
##print(list2)
###Another way of doing it
##list2=[]
##for i in list1:
##    list2.append(i)
##print(list2)
###Yet another way of doing it
##list2=[]+list1
##print(list2)

#Processing lists
#Sum of the elements
##def main():
##    total=0
##    list1=[1,3,5,7]
##    print(list1)
##    for value in list1:
##        total += value
##        print(total)
##main()

#Average
##def main():
##    total = 0
##    list1=[1,3,5,7]
##    print(list1)
##    for val in list1:
##        total += val
##        print ("total is:", total)
##        avg= total/len(list1)
##        print ('Average is:' , avg)
##
##main()

#Two dimensional list
##teams=[['A1', 'BO', 'Lee'],
##       ['Sam', 'Xi','Mo'],
##       ['Tom', 'Jay', 'Di']]
##print(teams)
##print(teams[0] [1])
##print(teams[1] [1])
##print(teams[1] [2])

#Tuples
tup1=(1,2,3,4)
print(tup1)

#For Loop
tup2= ('Mon', 'Tues', 'Wed')
for n in tup2:
    print(tup2)
#Indexing
for i in range (len(tup2)):
    print(tup2[i])
#convert a tuple into a list and a list into a tuple
    #Build in list() and tuple() functions
tup1=(1,2,3,4,5)
list1 = list(tup1)
print(list1)

str_list= ['one', 'uno', 'un']
str_tuple= tuple(str_list)
print(str_tuple)
