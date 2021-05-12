#sum of even FibanocciSeries
fibanocciSeries=[1,2]
i=0
add=2
while True:
    i=fibanocciSeries[-1]+fibanocciSeries[-2]
    if i<4000000:
        fibanocciSeries.append(i)
        if i%2==0:
            add+=i
              
    else:
        break
print(add)
    


