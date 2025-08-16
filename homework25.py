s = int(input("Enter the starting number : "))
e = int(input("Enter the ending number : "))
if s % 2 == 0:
    odd = [i + 1 for i in range(s , e, 2)]
else:
    odd = [i for i in range(s , e+1, 2)]
print(odd)

