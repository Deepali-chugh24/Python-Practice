#a=int(input("enter any number:"))
#print(list(range(a,0,-1)))


# i="*"
# for i in range(5):
#     i*="*"
#     print(i)

# n=5
# for i in range(1,i):
#     for a in range(1,i+1):
#         print(a,end="")
#         print("")

# num = 5
# for n in range(1, num):
#     for i in range(1, n+1):
#         print(i, end=" ")
#     print("")


#Write a program to read any Month Number in integer and display the number of days for this month.

month=int(input("Enter month number:"))

if ( month>12):
     print("Put valid month number")
if ( month==4 or month==6 or month==9 or month==11):
     print("This month have 30days in it")
elif month==2:
    print("This month have 28 days in it:")
else:
    print("This month have 31 days in it:")



unit=int(input("Enter number of units:"))

if ( unit<=100):
    print("No charge")
if(unit>100)and(unit<200):
     print("U need to pay:",unit*5)
if(unit>200):
     print("u meed to pay:",unit*10)