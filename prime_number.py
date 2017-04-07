
def generate_prime(n):
    
    """generate prime numbers bt 1 to n."""

	prime_list = []

    if n == 0 or n == 1:
        return "number is not prime."

    if n < 2:
        return "number less than two are not prime."

    if not type(n) == int:
        return "strings not allowed."

    for i in range(2, n + 1):
        if i > 1:
            for x in range(2, i):
                if (i % x) == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


