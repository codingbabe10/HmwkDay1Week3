def fibonacci_sequence(n, a=0, b=1, iteration=0):
    if iteration <= n:
        print(f"Iteration {iteration}: {a}")
        fibonacci_sequence(n, b, a + b, iteration + 1)

fibonacci_sequence(1)

