def bubble_sort(numbers):

    #copy
    sorted_numbers = numbers[:]

    n = len(sorted_numbers)
    comparisons = 0

    for num in range(n - 1):

        #compare
        for position in range(n - 1 - num):
            comparisons += 1

            if sorted_numbers[position] > sorted_numbers[position + 1]:
                temporary_value = sorted_numbers[position]

                sorted_numbers[position] = sorted_numbers[position + 1]
                sorted_numbers[position + 1] = temporary_value

    return sorted_numbers, comparisons


short_list = [7, 2, 9, 1, 5]

long_list = [
    18, 3, 25, 7, 12,
    1, 20, 9, 15, 4
]

another_list = [
    14, 2, 19, 8, 6,
    11, 3, 17, 5, 10,
    1, 16, 9, 13, 4
]


sorted_short, short_comparisons = bubble_sort(short_list)
sorted_long, long_comparisons = bubble_sort(long_list)
sorted_another, another_comparisons = bubble_sort(another_list)


print("Original short list:")
print(short_list)

print("Sorted short list:")
print(sorted_short)

print("Number of comparisons:")
print(short_comparisons)


print("Original long list:")
print(long_list)

print("Sorted long list:")
print(sorted_long)

print("Number of comparisons:")
print(long_comparisons)


print("Original 15-item list:")
print(another_list)

print("Sorted 15-item list:")
print(sorted_another)

print("Number of comparisons:")
print(another_comparisons)