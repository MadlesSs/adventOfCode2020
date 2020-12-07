input = open('input.txt', 'r')
lines = input.readlines()

# part 1
def part1():
    for first in lines:
        for second in lines: 
            firstNum = int(first)
            secondNum = int(second)
            if (firstNum + secondNum == 2020):
                print(firstNum * secondNum)
                return
            
part1()
# part 2 
def part2():
    for first in lines:
        for second in lines: 
            for third in lines: 
                firstNum = int(first)
                secondNum = int(second)
                thirdNum = int(third)
                if (firstNum + secondNum + thirdNum == 2020):
                    print (firstNum * secondNum * thirdNum)
                    return
part2()
