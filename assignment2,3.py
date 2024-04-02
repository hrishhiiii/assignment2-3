# length = 7
# breadth = 4
# area = length * breadth
# perimeter =2 * (length + breadth)
# print("area of the rectangle=",area)

# list:

# a = [2,4,6,8]
# b =a[1:3]
# print(b)
# a.append(10)
# print(a)
# a.insert(3,7)
# print(a)
# a.remove(2)
# print(a)
# print(a[0])
# l=len(a)
# print(l)
# list1= [1,2,3]
# list2=[4,5,6]
# c = list1 + list2
# print(c)
# print(list1 * 2)


#1

# X = [[12,7],
#     [4 ,5],
#     [3 ,8]]
# result = [[0,0,0],
#          [0,0,0]]
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[j][i]=X[i][j]
# for r in result:
#     print(r)

# #4
# d1 ={1: 'a',2: 'b'}
# d2 ={2: 'c',4: 'd'}
# print(d1 | d2)

#6
# a =[8,10,19]
# total=sum(a)
# print("sum of all elements in the given list:",total)
        
        
#10
# numbers =[2,4,8]
# doubled_numbers = [num * 2 for num in numbers]
# print(doubled_numbers)

# 11
# dic=dict.fromkeys(range(5), True)
# print(dic)

#2
# def capitalize_lines():
#     lines = []
#     while True:
#         line = input("Enter a line (or press Enter to stop): ")
#         if not line:
#             break
#         lines.append(line.upper())
#     print("\nCapitalized lines:")
#     for line in lines:
#         print(line)
# capitalize_lines()

#7
# def generate_square_dictionary(n):
#     square_dict = {}
#     for i in range(1, n+1):
#         square_dict[i] = i * i
#     return square_dict
# def main():
#     n = int(input("Enter a number (n): "))
#     square_dict = generate_square_dictionary(n)
#     print("Dictionary containing (i, i*i) pairs:")
#     print(square_dict)
# if __name__ == "__main__":
#     main()
#8
# def count_letters_and_digits(sentence):
#     letters = sum(c.isalpha() for c in sentence)
#     digits = sum(c.isdigit() for c in sentence)
#     return letters, digits
# def main():
#     sentence = input("Enter a sentence: ")
#     letter_count, digit_count = count_letters_and_digits(sentence)
#     print("Number of letters:", letter_count)
#     print("Number of digits:", digit_count)
# if __name__ == "__main__":
#     main()

#9
# def my_filter(func, iterable):
#     return [item for item in iterable if func(item)]
# def my_map(func, iterable):
#     return [func(item) for item in iterable]
# def my_reduce(func, iterable, initial=None):
#     it = iter(iterable)
#     if initial is None:
#         try:
#             initial = next(it)
#         except StopIteration:
#             raise TypeError('reduce() of empty sequence with no initial value')
#     accumulator = initial
#     for x in it:
#         accumulator = func(accumulator, x)
#     return accumulator
# even_numbers = my_filter(lambda x: x % 2 == 0, range(10))
# doubled_numbers = my_map(lambda x: x * 2, range(10))
# sum_of_numbers = my_reduce(lambda x, y: x + y, range(10))
# print("Even Numbers:", even_numbers)
# print("Doubled Numbers:", doubled_numbers)
# print("Sum of Numbers:", sum_of_numbers)

#13
# def remove_even_numbers(lst):
#     """
#     Removes even numbers from a list.
#     Args:
#     lst (list): The input list of numbers.
#     Returns:
#     list: List with even numbers removed.
#     """
#     return [num for num in lst if num % 2 != 0]
# def main():
#     num_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
#     result_list = remove_even_numbers(num_list)
#     print("List after removing even numbers:", result_list)
# if __name__ == "__main__":
#     main()

#14
# squares = [i ** 2 for i in range(1, 31)]
# print("First 5 elements:")
# print(squares[:5])
# print("\nLast 5 elements:")
# print(squares[-5:])

#15
# def insert_string_at_beginning(string, lst):
#     return [string + item for item in lst]
# given_string = "daa "
# my_list = ["hi", "poda", "myyy"]
# result_list = insert_string_at_beginning(given_string, my_list)
# print(result_list)

#16
# num = [10,18,1]
# colour =['blue','white','black']
# value = [3,100]
# for(a,b,c) in zip(num,colour,value):
#     print(a,b,c)

#12
# lst =[]
# num = int(input("how many numbers: "))
# for n in range(num):
#     numbers =int(input("enter numbers: "))
#     lst.append(numbers)
# print("maximum number in list: ",max(lst),"\minimum number in list:",min(lst))

#17
# d ={0:10,1:20}
# print(d)
# d.update({2:30})
# print(d)

#18
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# new_dict = {}
# new_dict.update(dic1)
# new_dict.update(dic2)
# new_dict.update(dic3)
# print("Concatenated Dictionary:")
# print(new_dict)

#19
# dt ={'a':'messi','b':'antonella','c':'thiago'}
# for key, value in dt.items():
#     print(key,value)

#21
# pets = {
#     'Willie': 'Dog',
#     'Mittens': 'Cat',
#     'Nemo': 'Fish'
# }

# for name, kind in pets.items():
#     print(f"{name} is a {kind}.")


#20
# def returnsum(dict):
#     return sum(dict.values())
# dict = {'a':100,'b':200,'c':500}
# print("sum:",returnsum(dict))

#22
# def create_new_dict(subject_marks):
#     new_dict = {}
#     for subject, mark in subject_marks.items():
#         new_dict[subject] = mark
#     return new_dict
# subject_marks = {'English': 40,'Maths': 60, 'Hindi': 30,'Chemistry': 46,'Physics': 70}
# new_dict = create_new_dict(subject_marks)
# print(new_dict)

#23
# def count_letters_digits(sentence):
#     num_letters = 0
#     num_digits = 0
#     for char in sentence:
#         if char.isalpha():
#             num_letters += 1
#         elif char.isdigit():
#             num_digits += 1
#     return num_letters, num_digits
# sentence = "Hello 123 World!"
# letters, digits = count_letters_digits(sentence)
# print("Number of letters:", letters)
# print("Number of digits:", digits)

#24
# def generate_square_dict(n):
#     square_dict = {num: num**2 for num in range(1, n+1)}
#     return square_dict
# n = 5
# result_dict = generate_square_dict(n)
# print(result_dict)

#25
# def find_sum(numbers):
#     return sum(numbers)
# def find_average(numbers):
#     return sum(numbers) / len(numbers)
# def find_maximum(numbers):
#     return max(numbers)
# def find_minimum(numbers):
#     return min(numbers)
# integer_list = [23, 45, 12, 67, 89, 34]
# total_sum = find_sum(integer_list)
# print("Sum of all elements:", total_sum)
# average = find_average(integer_list)
# print("Average of all elements:", average)
# maximum_element = find_maximum(integer_list)
# minimum_element = find_minimum(integer_list)
# print("Maximum element:", maximum_element)
# print("Minimum element:", minimum_element)

#26
# def find_union(set1, set2):
#     return set1.union(set2)
# def find_intersection(set1, set2):
#     return set1.intersection(set2)
# def check_subset(set1, set2):
#     return set1.issubset(set2)
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# union_set = find_union(set_a, set_b)
# print("Union of sets:", union_set)
# intersection_set = find_intersection(set_a, set_b)
# print("Intersection of sets:", intersection_set)
# subset_check = check_subset(set_a, set_b)
# print("Is set A a subset of set B?", subset_check)

#27
# squares = [num ** 2 for num in range(1, 11)]
# print("List of squares of numbers from 1 to 10:", squares)

#28
# empty_tuple = ()
# integer_tuple = (1, 2, 3, 4, 5)
# mixed_tuple = (1, 'hello', 3.14, True, [1, 2, 3])
# print("Empty Tuple:", empty_tuple)
# print("Tuple with five integer elements:", integer_tuple)
# print("Mixed-type tuple:", mixed_tuple)

#29
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# concatenated_tuple = tuple1 + tuple2
# print("Concatenated tuple:", concatenated_tuple)
# multiplied_tuple = tuple1 * 3
# print("Multiplied tuple:", multiplied_tuple)
# third_element = tuple1[2]
# print("Third element of the tuple:", third_element)

#30
# my_tuple = (1, 2, 3, 4, 5, 3, 6, 3)
# element_count = my_tuple.count(3)
# print("Count of occurrences of '3' in the tuple:", element_count)
# element_index = my_tuple.index(4)
# print("Index of '4' in the tuple:", element_index)










