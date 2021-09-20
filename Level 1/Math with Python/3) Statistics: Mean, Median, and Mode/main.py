def mean(*args):
    return sum(args) / len(args)


def median(*args):
    lst = sorted(args)
    if len(lst) % 2 == 0:
        return mean(lst[len(lst) // 2 - 1], lst[len(lst) // 2])
    else:
        return lst[len(lst) // 2]


def mode(*args):
    other = []
    for i in args:
        if args.count(i) > 1 and i not in other:
            other.append(i)
    return other


print(mean(4, 1, 8, 9, 6, 2))
print(median(2, 5, 3, 4, 9, 6, 0, 1, 5, 7))
print(mode(1, 2, 5, 5, 6, 6))
