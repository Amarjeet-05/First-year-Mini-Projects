import random
import string
n = input("Enter a message : ")
split = n.split(" ")
length = 3
new = [] #empty list is made for storing the words in a list
code = input("1 for coding and 0 for decoding : ")
code = True if(code=='1') else False
if(code):
    for ele in split:
        if(len(ele) >= 3):
            r1 = ''.join(random.choices(string.ascii_letters, k=length))
            r2 = ''.join(random.choices(string.ascii_letters, k=length))
            str = r1 + ele[1:] + ele[0] + r2 #we make str to store the value and append it into the 'new' list
            new.append(str)
        else:
            new.append(ele[::-1]) #it is a way to reverse the string

# print(new)   #it print in the form of a list
    print(" ".join(new)) #The join() method iterates through the elements of the provided iterable and combines them into a single string, inserting the separator string between each element.

else:
    for i in split:
        if(len(i) >= 3):
            str = i[3:-3] #this is used to remove first and last three characters
            str = str[-1] + str[:-1] #here in second equation we use[:-1] so it cannot print -1th element
            new.append(str)
        else:
            new.append(i[::-1])
    print(" ".join(new))