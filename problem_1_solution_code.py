#sum of multiples of 3 and 5
listOfNum=[num for num in range(1000) if (num%3==0 or num %5==0)]
print(sum(listOfNum))
