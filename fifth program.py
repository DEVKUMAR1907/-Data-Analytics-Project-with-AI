# # print 1 to 5
# count = 1
# while count <=5:
#     print("desai",count)
#     count += 1
# print(count)

# # print 5 to 1
# i = 5
# while i>=1:
#     print(i)
#     i -=1
# print("loop ended")

# while loop pratice question 
# print 1 to 100

# i =1
# while i<=100:
#     print(i)
#     i +=1
# print("loop ended")

# # print 100 to 1

# i=100
# while i >=1:
#     print(i)
#     i-=1
# print("loop ended")

# print the multilication table of a number n.
# n=int(input("enter the number"))
# i=1
# while i<=10:
#     print(n*i)
#     i +=1

# print the elements of the follwing list using a loop: [1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]
# index = 0 
# while index < len(nums):
#     print(nums[index])
#     index +=1

# search for a number x in this tuple usinf loop: [1,4,9,16,25,36,49,64,81,100]
# nums =  [1,4,9,16,25,36,49,64,81,100]
# x=36
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("found",i)
#     else:
#         print("finding...")
#     i +=1

# break 

# i=0;
# while i<=5:
#     print(i)
#     if(i ==3):
#         break
#     i +=1
# print("loop break ")

# continue 

# i=0;
# while i<=5:
  
#     if(i ==3):
#         i +=1
#         continue
#     print(i)
#     i +=1
# print("loop break ")

# i=1;
# while i<=10:
  
#     if(i%2==0):
#         i +=1
#         continue
#     print(i)
#     i +=1
# print("loop break ")

# for loop  in list
# nums = [1,2,3,4,5,6,7,8,9,]
# for value in nums:
#     print(value)

# # for loop in tuple
# nums = (1,2,3,4,5,6,7,8,9,)
# for value in nums:
#     print(value)

# for loop in string 
# nums = "desai"
# for value in nums:
#     if (value == "s"):
#         print("letter found")
#         break
#     print(value)


# for loop question practice print the elements of thr following list using a loop:[1,4,9,16,25,36,49,64,81,100]
# num = [1,4,9,16,25,36,49,64,81,100]
# for value in num:
#     print(value)

# Search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100)
# num = (1,4,9,16,25,36,49,64,81,100)
# x=49
# inde =0 
# for value in num:
#     if(value == x):
#         print("number found",inde)
#     inde+=1

# for loop in range 

# sequence =range(8)
# for value in sequence:
#     print(value)

# # another way of loop in range 
# for value in range(30): #range(stop)
#     print(value)

# for value in range(21,30):#range(start,stop)
#     print(value)

# for value in range(2,10,2):#range(start,stop,step)
#     print(value)

# for value in range(2,100,2):#even number print in range in loop
#     print(value)

# practice question print numbers from 1 to 100.
# for value in range(1,100):
#     print(value)

# print numbers from 100 to 1.
# for value in range(100,0,-1):
#      print(value)

# print the multiplication table of a number n.
# n= int(input("enter the numbar "))
# for i in range(1,11):
#     print(n*i) 

# pass statement
# for i in range(5):
#     pass
# if i>5:
#     pass
# print("some useful work")

# pratice question WAP to find the sum of first n numbers.(using while).
# n=7
# sum =0 
# i=1
# while i<=n:
#     sum +=i
#     i+=1
# print("total sum =",sum)

# WAP to find the factorial of first n numbers.(using for).
n=5
fact=1
for value in range (1,n+1):
    fact*=value
print("factorial=",fact)