# 1. Write a python script to print MySirG N times on the screen
"""
userInput = int(input("How Many Times You Want to Print MySirG : "))
count =1

while(userInput>=count):
    print("MySirG")
    count+=1

"""

# 2. Write a python script to print first N natural numbers
"""
userInput = int(input("Enter Number :"))
count = 1

while(userInput >= count):
    print(count)
    count+=1
"""

# 3. Write a python script to print first N natural numbers in reverse order
"""
userInput = int(input("Enter Number :"))
count = 1

while(userInput >= count):
    print(userInput)
    userInput-=1
"""

# 4. Write a python script to print first N odd natural numbers
"""
userInput = int(input("Enter Number :"))
count = 1
userInput = userInput*2
while(userInput >= count):
    if(count%2!=0):
        print(count)
    count+=1
"""

# 5. Write a python script to print first N odd natural numbers in reverse order
"""
userInput = int(input("Enter Number :"))
count = 1
userInput = userInput*2
while(userInput >= count):
    if(userInput%2!=0):
        print(userInput)
    userInput-=1
"""

#6. Write a python script to print first N even natural numbers
"""
userInput = int(input("Enter Number :"))
count = 1
userInput = userInput*2
while(userInput >= count):
    if(count%2==0):
        print(count)
    count+=1
"""

#7.Write a python script to print first N even natural numbers in reverse order
"""
userInput = int(input("Enter Number :"))
count = 1
userInput = userInput*2
while(userInput >= count):
    if(userInput%2==0):
        print(userInput)
    userInput-=2
"""

# 8. Write a python script to print squares of first N natural numbers
"""
userInput = int(input("Enter Number"))
count = 1

while(userInput >= count):
    print(count*count)
    count+=1
"""

# 9. Write a python script to print cubes of first N natural numbers
"""
userInput = int(input("Enter Number"))
count = 1

while(userInput >= count):
    print(count*count*count)
    count+=1
"""

# 10. Write a python script to print first 10 multiples of N
"""
userInput = int(input("Enter Number"))
count = 1

while(count<=10):
    print("{}*{}={}".format(userInput,count,(userInput*count)))
    count+=1
"""