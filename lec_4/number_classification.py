input_numbers = input("Enter a list of numbers separated by spaces: \n") 
numbers = [int(num) for num in input_numbers.split()]
even_numbers = []
odd_numbers = []

def classify_numbers(numbers):

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers


classify_numbers(numbers)
print(even_numbers, odd_numbers)