def sum_of_even_numbers(n):
    sum_even = 0
    
    for i in range(2, n+1, 2): 
        sum_even += i
    
    return sum_even

# Example usage:
n = int(input("Enter a number: "))
print("Sum of even numbers up to", n, "is:", sum_of_even_numbers(n))
