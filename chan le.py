input = [0,1,2,3,4,5,6,7,8,9]
even, odd = [], []

for num in input:
    if num % 2 == 0:
        even.append(num)
        x = sorted(even)
        result1 = slice(0,9,1)
        print(result1)
    else:
        odd.append(num)
        y = sorted(odd, reverse = True)

print (x + y)
