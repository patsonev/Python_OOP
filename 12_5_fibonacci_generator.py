def fibonacci():
    first_num = 0
    second_num = 1
    yield first_num
    yield second_num
    while True:
        num = first_num + second_num
        yield num
        first_num = second_num
        second_num = num


generator = fibonacci()
for i in range(10):
    print(next(generator))