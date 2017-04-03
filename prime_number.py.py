
def generate_prime(n):
    prime_list = []
    for num in range(n+1):
        if prime(num):
            prime_list.append(num)
        else: continue   
    return(prime_list)


