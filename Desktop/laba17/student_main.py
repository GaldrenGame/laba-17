def number_generator(numbers):
    for num in numbers:
        yield num

def even_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

def odd_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_number_generator(limit):
    if limit >= 2:
        yield 2
    for num in range(3, limit + 1, 2):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root):
    if root:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.value
        yield from in_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.value

def dfs_traversal(graph, start_node):
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            yield node
            visited.add(node)
            stack.extend(reversed(graph.get(node, [])))

from collections import deque

def bfs_traversal(graph, start_node):
    visited = set()
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            yield node
            visited.add(node)
            queue.extend(graph.get(node, []))

def dict_keys_generator(dictionary):
    for key in dictionary:
        yield key

def dict_values_generator(dictionary):
    for value in dictionary.values():
        yield value

def dict_items_generator(dictionary):
    for item in dictionary.items():
        yield item

def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

def string_chars_generator(string):
    for char in string:
        yield char

def unique_elements_generator(input_list):
    seen = set()
    for item in input_list:
        if item not in seen:
            yield item
            seen.add(item)

def reverse_list_generator(input_list):
    for item in reversed(input_list):
        yield item

def cartesian_product_generator(list1, list2):
    for item1 in list1:
        for item2 in list2:
            yield (item1, item2)

import itertools

def permutations_generator(input_list):
    for perm in itertools.permutations(input_list):
        yield perm

def combinations_generator(input_list):
    for r in range(1, len(input_list) + 1):
        for combo in itertools.combinations(input_list, r):
            yield combo

def tuple_list_generator(tuple_list):
    for tup in tuple_list:
        yield tup

def parallel_lists_generator(*lists):
    iterators = [iter(lst) for lst in lists]
    while True:
        yield tuple(next(it) for it in iterators)

def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item

def nested_dict_generator(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)

def powers_of_two_generator(n):
    power = 0
    while power <= n:
        yield 2 ** power
        power += 1

def powers_of_base_generator(base, limit):
    power = 0
    while base ** power <= limit:
        yield base ** power
        power += 1

def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2

def cubes_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 3

import math

def factorials_generator(n):
    for num in range(n + 1):
        yield math.factorial(num)

def collatz_sequence_generator(start):
    while start != 1:
        yield start
        if start % 2 == 0:
            start = start // 2
        else:
            start = 3 * start + 1
    yield 1

def geometric_progression_generator(initial, ratio, limit):
    num = initial
    while num <= limit:
        yield num
        num *= ratio

def arithmetic_progression_generator(initial, difference, limit):
    num = initial
    while num <= limit:
        yield num
        num += difference

def running_sum_generator(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total

def running_product_generator(numbers):
    product = 1
    for num in numbers:
        product *= num
        yield product
