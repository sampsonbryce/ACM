# Link for Problem: http://www.acmicpc-pacnw.org/ProblemSet/2014/div2.pdf
#
# Problem Name: Runes
# Location: Page 19


def check_op(op, answer):

    if op == "+":
        ans = int(num1) + int(num2)
        ans = int(ans)
        answer = int(answer)

        if ans == answer:
            print(sub)
            return True

    elif op == "-":

        ans = int(num1) - int(num2)
        ans = int(ans)
        answer = int(answer)

        if answer == ans:
            print(sub)
            return True

    elif op == "*":

        ans = int(num1) * int(num2)
        ans = int(ans)
        answer = int(answer)
        if answer == ans:
            print(sub)
            return True

    return False


cases = int(input())
equations = []

for i in range(0, cases):
    equations.append(str(input()))

for h in range(len(equations)):
    full = equations[h]
    lFull = [x for x in full]
    key = []
    op = ""
    number = False
    count = 0
    sub = ""
    opIndex = 0
    eqIndex = 0
    ops = ['+', '-', '*']

    for i in lFull:

        if i in ops:
            if lFull.index(i) != 0:
                opIndex = lFull.index(i)

        if i == "=":
            eqIndex = lFull.index(i)

        if i == "?":
            key.append(count)
        count += 1

    for a in range(10):

        num1 = ""
        num2 = ""
        answer = ""

        sub = str(a)

        for b in range(len(lFull)):
            if b in key:
                lFull[b] = sub

        for i in lFull[:opIndex]:
            num1 += i

        for i in lFull[(opIndex + 1):eqIndex]:
            num2 += i

        for i in lFull[(eqIndex + 1):]:
            answer += i

        if check_op(lFull[opIndex], answer):
            break
