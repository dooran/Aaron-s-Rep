# Manuel Duran 1584885
if __name__ == '__main__':
    data = input().split()

    for i in range(len(data)):
        data[i] = int(data[i])

    data.sort()

    for num in data:
        if num >= 0:
            print(num, end=' ')
