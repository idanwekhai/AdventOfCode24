from collections import defaultdict
with open('input.txt') as f:
    text =  [line.strip('\n').split('|') for line in f]

rules = []
idx = 0
for i in range(len(text)):
    if text[i] == ['']:
        idx = i
        break

rules = text[:idx]
pages = [list(map(int, i[0].split(','))) for i in text[idx+1:]]

order_map = defaultdict(list)
for i in rules:
    order_map[int(i[0])].append(int(i[1]))

def part_1():
    sum_middle = 0
    for i in pages:
        rules_temp = {}
        custom_order =  []
        for j in i:
            lst = order_map[j]
            lst = list(set(lst).intersection(set(i)))
            rules_temp[j] = lst
            lst.insert(0, j)
            custom_order.append(lst)
        custom_order = list(set([x for xi in custom_order for x in xi]))
        for k, v in rules_temp.items():
            idxs = [custom_order.index(i) for i in v]
            min_idx = min(idxs)
            if min(idxs) < custom_order.index(k):
                custom_order.remove(k)
                custom_order.insert(min_idx, k)
        if i == sorted(i, key=lambda x: custom_order.index(x)):
            sum_middle += i[len(i)//2]
    return sum_middle

def part_2():
    sum_middle = 0
    for i in pages:
        rules_temp = {}
        custom_order =  []
        for j in i:
            lst = order_map[j]
            lst = list(set(lst).intersection(set(i)))
            rules_temp[j] = lst
            lst.insert(0, j)
            custom_order.append(lst)
        custom_order = list(set([x for xi in custom_order for x in xi]))
        for k, v in rules_temp.items():
            idxs = [custom_order.index(i) for i in v]
            min_idx = min(idxs)
            if min(idxs) < custom_order.index(k):
                custom_order.remove(k)
                custom_order.insert(min_idx, k)
        if i != sorted(i, key=lambda x: custom_order.index(x)):
            i = sorted(i, key=lambda x: custom_order.index(x))
            sum_middle += i[len(i)//2]
    return sum_middle

print(part_1())
print(part_2())