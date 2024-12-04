import re
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

with open('input.txt') as f:
    text =  [list(line.strip('\n')) for line in f]

grid = np.array(text)

def find_xmas(input_text):
    pattern = r'(?=(XMAS))|(?=(SAMX))'
    return re.findall(pattern, input_text)

def find_mas(input_text):
    pattern = r'MAS|SAM'
    return re.findall(pattern, input_text)

def part_1():
    count = 0
    for i in grid:
        row = ''.join(i)
        occurence = find_xmas(row)
        count += len(occurence)
    for j in grid.T:
        col = ''.join(j)
        occurence = find_xmas(col)
        count += len(occurence)
    for k in range(len(grid)):
        if k == 0:   
            diag = ''.join(np.diag(grid, k=k)) 
            occurence = find_xmas(diag)
            count += len(occurence)
        else:
            diag_upper = ''.join(np.diag(grid, k=k))
            diag_lower = ''.join(np.diag(grid, k=-k))
            if len(diag_upper) < 4:
                break
            occurence = find_xmas(diag_upper)
            count += len(occurence)
            occurence = find_xmas(diag_lower)
            count += len(occurence)
    ngrid = np.fliplr(grid)
    for j in range(len(grid)):
        if j == 0:   
            diag = ''.join(np.diag(ngrid, k=j))
            occurence = find_xmas(diag)
            count += len(occurence)
        else:
            diag_upper = ''.join(np.diag(ngrid, k=j))
            diag_lower = ''.join(np.diag(ngrid, k=-j))
            if len(diag_upper) < 4:
                break
            occurence = find_xmas(diag_upper)
            count += len(occurence)
            occurence = find_xmas(diag_lower)
            count += len(occurence)
    return count

def part_2():
    count = 0
    strides_out = sliding_window_view(grid, (3,3))
    for j in strides_out:
        for i in j:
            diag_1 = ''.join(np.diag(i))
            diag_2 = ''.join(np.diag(np.fliplr(i)))
            occurence_1 = find_mas(diag_1)
            occurence_2 = find_mas(diag_2)
            if len(occurence_1) == len(occurence_2) ==1:
                count += 1
    return count


print(part_1())
print(part_2())