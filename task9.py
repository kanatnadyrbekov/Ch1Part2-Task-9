a = int(input("Factorial:"))
fact = 1
for b in range(1, a + 1):
    fact = fact * b
    print(f"factorial of {a}: ", end='')
    print(fact)