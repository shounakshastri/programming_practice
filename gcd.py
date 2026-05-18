#Code to find the GCD of two numbers
def gcd(a:int , b:int) -> int:
    while b:
        a, b = b, a%b
    return a
    
print(gcd(146, 148))