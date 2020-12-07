f = open('input.txt', 'r')
lines = f.readlines()
# part 1
correct = 0
for line in lines:
    line = line.replace(" ", "")
    firstHalf, password = line.split(':')
    firstNum, secondNumAndChar = firstHalf.split('-')
    char = secondNumAndChar[-1]
    secondNum = secondNumAndChar[:-1]
    counter = 0
    for character in password:
        if (char == character):
            counter += 1
    if (int(firstNum) <= counter <= int(secondNum)):
        correct += 1

print(correct)

# part 2
correct = 0
for line in lines:
    line = line.replace(" ", "")
    firstHalf, password = line.split(':')
    firstNum, secondNumAndChar = firstHalf.split('-')
    char = secondNumAndChar[-1]
    secondNum = secondNumAndChar[:-1]
    firstNum = int(firstNum)
    secondNum = int(secondNum)
    counter = 0
    if (password[firstNum -1] == char):
        counter += 1
    if (password[secondNum -1] == char):
        counter += 1
    if (counter == 1):
        correct += 1
print(correct)
