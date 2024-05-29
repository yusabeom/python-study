'''
* 집합 (set)

- 집합은 여러 값들의 모임이며, 저장 순서가 보장되지 않고
 중복값의 저장을 허용하지 않습니다.

- 집합은 사전과 마찬가지로 {}로 표현하지만, key:value
쌍이 아닌, 데이터가 하나씩 들어간다는 점이 사전과는 다릅니다.

- set()함수는 공집합을 만들기도 하며, 다른 컬렉션 자료형을
집합 형태로 변환할 수도 있습니다.

# []-list(), tuple(), {}-dict(), set()
'''

names = {'홍길동', '김철수', '박영희', '고길동', '홍길동'}
print(type(names))
print(names)

for x in names:
    if x == '김철수':
        print(x)
        break

# 내장함수 set()
s = set()
print(type(s))
print(s)