f = open('input.txt', 'r')
lines = f.readlines()


def countTrees(moveX, moveY):
    posX = 0
    posY = 0
    trees = 0
    CHARS_IN_ROW = 31
    while (posY + 1) < len(lines):
        posY += moveY
        posX += moveX
        if (posX >= CHARS_IN_ROW):
            posX = posX - CHARS_IN_ROW
        curentLine = list(lines[posY])
        char = curentLine[posX]
        if (char == '#'):
            trees += 1
            curentLine[posX] = 'X'
        else: 
            curentLine[posX] = 'O'
        print("".join(curentLine))
    return trees

print(countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2))
