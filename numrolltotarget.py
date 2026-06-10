def numRollsToTarget(n, k, target):
    if n == 0 and target == 0:
        return 1
    if n == 0 or target <= 0:
        return 0
    result = 0
    for i in range(1, k + 1):
        result += numRollsToTarget(n - 1, k, target - i)
    return result % 1_000_000_0

