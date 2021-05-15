import copy


def matchingUpper(x, y):
    for i in range(6):
        if x[0][i] != y[-1][i]:
            return False
    return True


def matchingRight(x, y):
    for i in range(6):
        if x[i][-1] != y[i][0]:
            return False
    return True


def chain(pieces, data):
    for piece in data:
        if (len(pieces) % 15 == 0 or matchingRight(pieces[-1], piece)) and (len(pieces) < 15 or matchingUpper(piece, pieces[-15])):
            data2 = copy.copy(data)
            data2.remove(piece)
            if len(pieces) == 224:
                return pieces + [piece]
            result = chain(pieces + [piece], data2)
            if result is not None:
                return result
    return None


if __name__ == '__main__':
    data = []
    with open("05-2-input.txt", "r") as file:
        for _ in range(225):
            piece = []
            for _ in range(6):
                line = file.readline()
                if line[-1] == '\n':
                    line = line[:-1]
                while len(line) != 6:
                    line += " "
                piece.append(line)
            data.append(piece)
            file.readline()

    c = 0
    curr = 0
    while c < 225:
        if matchingUpper(data[curr], data[c]) or matchingRight(data[c], data[curr]):
            curr = c
            c = 0
        c += 1

    pieces = [data[curr]]
    data.remove(data[curr])
    pieces = chain(pieces, data)

    output = ["" for _ in range(15 * 5 + 1)]
    for i, piece in enumerate(pieces):
        for y in range(5 if i < 15 * 14 else 6):
            output[int(i / 15 * 5) // 5 * 5 + y] += piece[y] if i % 15 == 14 else piece[y][:-1]
    for line in output:
        print(line.replace("'", " ").replace("`", " "))  # cela dodatna naloga v 1 vrstici
