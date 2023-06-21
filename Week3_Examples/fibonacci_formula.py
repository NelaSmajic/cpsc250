import math
import decimal as dec


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        t1 = 0
        t2 = 1
        t3 = 0
        for i in range(2, n+1):
            t3 = t2 + t1
            t1 = t2
            t2 = t3
        return t3


def fibonacci_phi(n):
    global phi
    return int((phi**n-(-1/phi)**n)/math.sqrt(5))


def fibonacci_phin(n):
    global phin
    global one, two, five, onehalf
    return round((phin**n-(-one/phin)**n)/five**onehalf)


if __name__ == "__main__":

    nth_term = 300

    dec.getcontext().prec = 100

    one = dec.Decimal(1)
    two = dec.Decimal(2)
    five = dec.Decimal(5)
    onehalf = dec.Decimal(0.5)

    phi = (1 + math.sqrt(5)) / 2

    phin = (one + five ** onehalf) / two

    print(one)
    print(two)
    print(five)
    print(onehalf)

    print(phi)
    print(phin)

    if nth_term % 10 == 0:
        ending = "th"
    elif nth_term % 10 == 1:
        ending = "st"
    elif nth_term % 10 == 2:
        ending = "nd"
    elif nth_term % 10 == 3:
        ending = "rd"
    else:
        ending = "th"

    print(f"The actual       {nth_term}{ending} term of the Fibonacci sequence is {fibonacci(nth_term)}")
    print(f"The Python math  {nth_term}{ending} term of the Fibonacci sequence is {fibonacci_phi(nth_term)}")
    print()
    print(f"The Decimal math {nth_term}{ending} term of the Fibonacci sequence is {fibonacci_phin(nth_term)}")