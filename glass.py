glass = 2
floor = 100

for target in range(1,101):
    throw = 0
    start = 0
    end = 100
    for i in range(2, glass):
        throw+=1
        check = end - ((end - start) // 2)

        if check > target:
            end = check

        else:
            start = check
        

    len = end - start

    sum= 0
    n = 0
    while sum < len:
        n+=1
        sum+=n

    for i in range(n, 0, -1):

        throw+=1
        if start + i <= target:
            start += i
        else:
            end = start + i
            break
    
    print(start, end)
    for i in range(1, n):
        throw+=1
        if start + i > target:
            end = start + i
            break
        if start + i == end-1:
            break

    start = end - 1

    print(start, end, target, throw)