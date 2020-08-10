# Generators are used to store inifinte amounts of data in finite amounts of memory


def infinite_seq():
    num = 0
    while True:
        yield num
        num += 1