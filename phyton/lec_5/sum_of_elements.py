def sum_of_elements(numbers, exclude_negative=False):
    summ = 0
    for num in numbers:
        if not exclude_negative or num >= 0:
            summ += num
    return summ

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = []
for num in user_input.split():
  numbers.append(int(num))

exclude_input = input("Do you want to exclude negative numbers? (yes or no): ")
if exclude_input == "yes":
    exclude_negative = True
else:
    exclude_negative = False

result = sum_of_elements(numbers, exclude_negative)

if exclude_negative:
    print("Sum of non-negative elements:", result)
else:
    print("Sum of all elements:", result)
