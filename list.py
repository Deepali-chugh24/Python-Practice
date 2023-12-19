# WAP to create a function that will tell the sum of maximum and minimum number in a list of numbers
def SumMaxMin(x):
    return(max(x)+min(x))

print(SumMaxMin([1,2,3,4,5,6,]))


    


# WAP to create a function to tell the count the consonants in any given string.

# def countCos():
#     a=0
#     b=0
#     i=input("enter any string").lower()
#     for x in range(len(i)):
#         if i[x] in ('a','e','i','o','u'):
#             b+=1    
#         elif(i[x]>='a'and i[x]<='z'):
#             a+=1
#     print("total number of consoants",a) 


# countCos()


# WAP to create a function that will tell the word which has minimum length in any given string

# def minlength(a):
#     # for i in a:
#     b=a.split(len())
#     c=print(min(b))
    
#     print(c)

# minlength('nitsimran sinhg ')

    
def min_word(str1):
    min_word = str1.split()
    for word in str1.split():
        if len(word) <= len(min_word):
            min_word = word
    return min_word
print(min_word('nitin sdi asds'))


