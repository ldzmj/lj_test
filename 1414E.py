while True:
    t = int(input())
    if 90 <= t <= 100:
        print('A')
    elif 80 <= t <= 89:
        print('B')
    elif 70 <= t <= 79:
        print('C')
    elif 60 <= t <= 69:
        print('D')
    elif 0 <= t <= 59:
        print('E')
    else:
        print('Score is error!')