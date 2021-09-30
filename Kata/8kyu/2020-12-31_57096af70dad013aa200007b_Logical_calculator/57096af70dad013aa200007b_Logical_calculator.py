from functools import reduce

def logical_calc(array, op):
    if op == "AND":
        return reduce(lambda x, y: x * y, array, 1) != 0
    elif op == "OR":
        return sum(array) > 0
    else:
        ans = array[0]
        for i in range(1, len(array)):
            ans = (ans != array[i])
        return ans
