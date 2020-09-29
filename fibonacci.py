def Solution(target):
    def calcFibo(target):
        fib_num = []
        i = 2
        fib_num.append(2)   # assume F1 and F2 are 2 and 3, not 1 and 1 from the original condition
        fib_num.append(3)
        while True:
            next = (fib_num[i - 1] + fib_num[i - 2])
            if next > target:
                break
            fib_num.append(next)
            i += 1
        return fib_num

    result = []
    fib_list = calcFibo(target)

    def possibleCom(left, stack):
        if left == 0:
            result.append(stack)
            return

        for item in fib_list:
            if item > left: break
            if stack and item < stack[-1]:
                continue
            else:
                possibleCom(left - item, stack + [item])    #recursive call

    possibleCom(target, [])
    return result
