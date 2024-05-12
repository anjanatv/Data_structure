#Topic : List
#Exercise (score : 1)
#Q1. Create a list of 5 random numbers and print the list.
import random as ra
l1=[52,47,34,10,16]
result=ra.choice(l1)
print(result)

#Q2. Insert 3 new values to the list and print the updated list.
l1.extend([12,14,17])
print(l1)
#Q3. Access the third element in the list and print the element.
print(l1[2])
#Q4. Create a new list of 3 random strings and concatenate the two lists into a third list.
l2=["hello","welcome","home"]
l3=l1+l2
print(l3)
#Q5. Try to use a for loop to print each element in the list.
for i in l3:
    print(i)
#Topic : Dictionary
#Exercise (score : 1)
#Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
d1={"name":"John","age":"25","address":"New York"}
#Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.

d1["Phone"]="1234567890"
print(d1)
#Q3. Remove the key 'address' from the dictionary created in Q1.
del d1["address"]
print(d1)
#Q4.  Print the value of the key 'age' from the dictionary created in Q1.
print(d1.get("age"))
#Q5. Check if the key 'phone' exists in the dictionary created in Q1.
print(d1.keys())
#Topic: Set
#Exercise (score : 1)
#Q1.Create a set with values 1, 2, 3, 4, and 5.
s1={1,2,3,4,5}
print(s1)
print(type(s1))
#Q2. Add the value 6 to the set created in Q1.
s1.update("6")
print(s1)
#Q3. Remove the value 3 from the set created in Q1.
s1.remove(3)
print(s1)
#Q4. Print the length of the set created in Q1.
print(len((s1)))
#Q5. Create a new set by union of the set created in Q1 with another set {6, 7, 8}.
s2={6,7,8}
s3=s1|s2
print(s3)

#Topic: Tuple
#Exercise (score : 1)
#Q1. Create a tuple with values 1, 2, 3, and 4
t1=(1,2,3,4,)
print(type(t1))
#Q2. Print the length of the tuple created in Q1.
print(len(t1))
#Q3. Create a new tuple by concatenating the tuple from Q1 with another tuple (5, 6).
t2=(5,6,)
t3=t1+t2
print(t3)
#Q4. Print the first two values of the tuple created in Q3.
print(t3[0:2])
#Q5. Check if the value 4 exists in the tuple created in Q1.
print(t3.__getitem__(3))

#Topic : String, List -set-dictionary comprehension
#Exercise 1 (score : 2)
"""Write a program that asks the user to enter his/her full name and the program process 
and manipulate the text of his/her name."""
#An example run of the program (numbers in bold are typed in by the user)
#Please enter your first name: Peter
#Please enter your last name: Cambridge
#Your full name is PETER CAMBRIDGE
#Your initials are P C
#First name length is 5 letters
#Last name length is 9 letters
#Full name length is 14 letters
#First name starts with P
#First name ends with R
#Last name starts with C
#Last name ends with E
#First name indexes are 0 – 4
#Last name indexes are 0 – 8
#First name trims 1 Pet
#First name trims 2 eter
#Last name trims 1 Cam
#Last name trims 2 bridge
n=input("Please enter your first name:")
l=input("Please enter your last name:")
name=n+l
print("Your full name is",name)
print("Your initials are", l)
print("First name length is", n.__len__())
print("Last name length is", l.__len__())
print("Full name length is", name.__len__())
print("First name starts with",n[0])
print("Last name starts with", l[0])
print("Last name ends with", l[-1])
print("First name indexes are 0 -", n[-1])
print("Last name indexes are 0 -",l[-1])
print("First name trims 1", n[0:3])
print("First name trims 2", n[3:])
print("Last name trims 1", l[0:3])
print("Last name trims 2", l[3:])


#Exercise 2 (score : 1)
"""Write a program that asks the user to enter his/her name and then partly encrypt and display it.
Name: John
Encrypted name : J**n"""
s1=input("enter your name:")
print(s1[0]+"*"*(len(s1)-2)+s1[-1])

#Exercise 3 (score : 1)
"""Write a Python program to count the number of strings where the string length is 2 or more and 
the first and last character are same from a given list of strings
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""
def strng_count (strings):
    count=0
    for string in strings:
        if len(string) >=2 and string[0]==string [-1]:
            count+=1
        return count

str=["abc" ,"xyz" ,"aba", "1221"]
res=strng_count(str)
print(res)


#def strng_count(list):
#Exercise 4 (score : 1) 
#Find all of the numbers from 1-1000 that are divisible by 7 using list comprehension.

divisibility= (i for i in range (1,1000) if i/7==0)
print(divisibility)

#Exercise 5 (score : 1) 
"""Create dictionary from a list where the keys are the elements of the list and value of the dictionary is 
result after dividing the element by 3"""
list1=[9,12,15,10,4,7]
dict1={num:num/3 for num in list1}
print(dict1)
