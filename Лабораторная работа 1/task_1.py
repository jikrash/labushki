numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

for i, number in enumerate(numbers):
    if number is None:
        missing_index = i
        break

sum_numbers = 0

for i in range(len(numbers)):
    if i != missing_index:
        sum_numbers += numbers[i]

average = sum_numbers / len(numbers)
numbers[missing_index] = average

print("Измененный список:", numbers)
