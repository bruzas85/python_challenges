# С клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел считан в качестве строки.
# Как превратить list строк в list чисел?

# numbers = input('Enter numbers: ')
# print(numbers)
# numbers = numbers.split()
# print(numbers)

numbers = input("Enter numbers: ")
numbers = list(map(int, numbers.split()))
print(numbers)


