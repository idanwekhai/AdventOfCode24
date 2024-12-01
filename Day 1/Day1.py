with open('input.txt') as f:
    numbers = [[line.strip('\n').split('   ')[0],
               line.strip('\n').split('   ')[1]]
              for line in f]
    
list_1 = sorted([int(x[0]) for x in numbers])
list_2 = sorted([int(x[1]) for x in numbers])

def part_1():
    distances = [abs((b - a)) for a, b in zip(list_1, list_2)]
    print(sum(distances))

def part_2():
    similarity_score = 0
    cache = {}
    for i in list_1:
        if i in cache:
            score = cache[i]
        else:
            score = list_2.count(i) * i
            cache[i] = score
        similarity_score += score
    print(similarity_score)

part_1()
part_2()