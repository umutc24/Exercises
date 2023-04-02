'''Meta interview, interview question 2, checking
   if we can split a giving array into two equal sub_arrays
   Umut Ceylan '''


input1 = input("Enter the elements of your list seperated by space please: ")
a = input1.split()
for i in range(len(a)):
    a[i] = int(a[i])
# a = [1,2,3,6]
sumOfArray = 0
sumNow = 0
aLeft = []
aRight = []


for i in range(len(a)):
    sumOfArray = sumOfArray + a[i]

halfOfArray = sumOfArray / 2

for i in range(len(a)):
    sumNow = sumNow + a[i]
    if sumNow == halfOfArray:
        aLeft = a[:a[i]]
        aRight = a[a[i]:]
    else:
        print("List is not splittable")
print(aLeft)
print(aRight)
