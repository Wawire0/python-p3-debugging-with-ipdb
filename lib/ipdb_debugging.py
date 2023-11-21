import ipdb_debugging

def plus_two(num):
    num = num + 2
    ipdb.set_trace()
    return num

print(plus_two(3))

