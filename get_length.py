def get_length(inputList):
    count = 0
    for _ in inputList:
        count += 1

    return count


def get_sum(inputList):
    total = 0
    for num in inputList:
        total += num

    return total


def get_mean(inputList):
    mean = get_sum(inputList) / get_length(inputList)

    return mean


if __name__ == '__main__':
    number = [12, 34, 56, 78, 19, 10]

    print(f'The length of the array is {get_length(number)}')
    print(f'The sum of the array is {get_sum(number)}')
    print(f'The mean of the array is {get_mean(number):.2f}')
