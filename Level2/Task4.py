#Task4: Fibonacci Sequence
def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Get the number of terms from the user
n = int(input("Enter the number of terms for the Fibonacci sequence: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci_sequence(n)
    print("Fibonacci sequence:")
    print(result)

