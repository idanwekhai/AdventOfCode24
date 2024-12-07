from itertools import product
with open('input.txt') as f:
    text =  [line.strip('\n').split(': ') for line in f]

equations = []
for i in text:
    equations.append([int(i[0]), list(map(int, i[1].split(' ')))])

def express_eqa(nums, ops):
    expression = str(nums[0])
    for op, num in zip(ops, nums[1:]):
         if op == '||':
              expression = f'{eval(expression)}' + f'{num}'
         else:
              expression = f'({expression} {op} {num})'
    return expression

def part_1(ops = ['+', '*']):
    matched = []
    for k, v in equations:
        length = len(v)-1
        stragtegies = set(product(ops, repeat=length))
        for strategy in stragtegies:
            total = eval(express_eqa(v, strategy))
            if total == k:
                matched.append(k)
                break
    return sum(matched)

def part_2(ops = ['+', '*', '||']):
    matched = []
    for k, v in equations:
        length = len(v)-1
        stragtegies = set(product(ops, repeat=length))
        for strategy in stragtegies:
            total = eval(express_eqa(v, strategy))
            if total == k:
                matched.append(k)
                break
    return sum(matched)

print(part_1())
print(part_2())