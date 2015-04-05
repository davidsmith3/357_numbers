def find_max(base, n):
    max = 0
    result = base ** max
    while result < n:
        max += 1
        result = base ** max
    return max

def count_numbers(n):
    result_set = set()

    three_max = find_max(3, n)
    five_max = find_max(5, n)
    seven_max = find_max(7, n)

    for i in range(0, three_max):
        for j in range(0, five_max):
            for k in range(0, seven_max):
                result = (3 ** i) * (5 ** j) * (7 ** k)
                if result < n:
                    result_set.add(result)


    print(len(result_set))
