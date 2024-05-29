'''
# 인수의 기본값
- 파이썬에서는 인수의 기본값을 설정하여, 자주 바뀌지 않는
매개값은 기본값으로 처리할 수 있게 합니다.
'''
def calc_stepsum(begin, end, step=1):
    sum = 0
    for n in range(begin, end+1, step):
        sum += n
    return sum

print(calc_stepsum(1, 10))
print(calc_stepsum(1, 10, 2))

# 기본값이 지정된 매개변수를 오른쪽으로 몰아 주셔야 합니다.
def calc_sum(end, begin=0, step=1):
    sum = 0
    for n in range(begin, end+1, step):
        sum += n
    return sum

print(calc_sum(100))