'''
* 내장함수 range()
- 순차적으로 증가하는 정수의 순차적 자료형을 만들 때
대괄호 안에 데이터들을 콤마로 일일히 나열하는 것은
한계가 있기 때문에, range()함수를 통해 보다 쉽게
순차형 반복 범위를 지정할 수 있습니다.
ex) range(begin, end, step)
- begin은 값이 포함되지만(이상), end는 값이 포함되지 않습니다. (미만)
'''

list1 = [1,2,3,4,5,6,7,8,9,10]

for n in list1:
    print(n, end=' ')

print('\n'+'-' * 40)

for n in range(1, 11, 1):
    print(n, end=' ')