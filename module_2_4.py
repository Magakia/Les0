numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i  in numbers:
    count = 1
    for j in range(1,i):
        if i%j == 0 :
            count = count + 1
    if count == 2:
        primes.append(numbers[i-1])
    elif count > 2:
        not_primes.append(numbers[i-1])
print(primes)
print(not_primes)


