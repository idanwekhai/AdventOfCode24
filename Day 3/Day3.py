import re

with open('input.txt') as f:
    text = f.read()

def find_muls(input_text):
    pattern = r'mul\(\d+,\d+\)'
    return re.findall(pattern, input_text , re.S)

def find_funcs(input_text):
    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
    return re.findall(pattern, input_text , re.S)

def process_mul(text):
    numbers = text[4:-1]
    return list(map(int, numbers.split(',')))

def part_1():
    all_muls = find_muls(text)
    total = 0
    for i in all_muls:
        numbers = process_mul(i)
        muliply = numbers[0] * numbers[1]
        total += muliply
    return total

def part_2():
    all_funcs = find_funcs(text)
    total = 0
    dont_mul = False
    for i in all_funcs:
        if i == "don't()":
            dont_mul = True
        elif i == "do()":
            dont_mul = False
        if dont_mul:
            pass
        elif dont_mul == False and i[:3] == "mul": 
            numbers = process_mul(i)
            muliply = numbers[0] * numbers[1]
            total += muliply
    return total

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")