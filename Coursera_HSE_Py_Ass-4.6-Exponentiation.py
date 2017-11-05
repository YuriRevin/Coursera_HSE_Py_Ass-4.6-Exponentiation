def exp(exp_a, exp_n):
    if exp_n == 0:
        return 1
    if exp_a > 0 and exp_n > 0:
        return exp_a * exp(exp_a, exp_n - 1)


a = float(input())
n = int(input())
print(exp(a, n))
