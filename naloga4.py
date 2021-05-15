if __name__ == '__main__':
    upper_inputs = [[0, int(i)] for i in input().split(" ")]
    n = len(upper_inputs)
    for i in range(n - 1, 0, -1):
        lower_inputs = [[int(i), int(i)] for i in input().split(" ")]
        for i2 in range(len(lower_inputs)):
            lower_inputs[i2][1] += upper_inputs[i2][1] if upper_inputs[i2][0] > upper_inputs[i2 + 1][0] else upper_inputs[i2 + 1][1]
        upper_inputs = lower_inputs
    print(upper_inputs[0][1])

