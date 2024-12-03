with open('input.txt') as f:
    reports = [list(map(int, line.strip('\n').split(' '))) for line in f]


# def checker(diff):
#     for i in diff:
#         if i not in [1, 2, 3]:
#             return False
#     return True

def checker_1(diff):
    if max(diff) >  3 or min(diff) < 1:
            return False
    return True

def arr_diff(arr):
    return [abs(arr[i] - arr[i - 1]) for i in range(1, len(arr))]

count = 0
for report in reports:
    print(report)
    print(arr_diff(report))
    if (sorted(report) == report) or (sorted(report) == report[::-1]):
        diff = set(arr_diff(report))
        if checker_1(diff):
            count += 1
    else:
        pass
print(count)

