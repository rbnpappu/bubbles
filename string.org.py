sentence=input("enter a string")
string=sentence.lower()
string=sentence.upper()
count=0
list1=["a","e","i","o","u"]
for char in sentence:
    if char in list1:
        count=count+1
print("no of vowels are%d",count);
    
