if __name__ == '__main__':
    tocke = int(input())
    n = int(input())
    result = 0
    record = 0
    for i in range(n):
        tocke += int(input())
        if tocke >= 3200:
            result += 1
            record = max(result, record)
        else:
            result = 0
    print(record)

"""
3200
10
20
10
-35
20
15
-10
-20
20
-30
-10
"""