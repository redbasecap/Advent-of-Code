# create a function to calculate the 10001st prime number 

def prime(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        count = 2
        num = 3
        while count < n:
            num += 2
            if all(num % i != 0 for i in range(3, int(num**0.5)+1, 2)):
                count += 1
        return num

print(prime(3000000001))