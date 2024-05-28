'''
* 반복문 for ~ in
- 파이썬의 for문은 시퀀스 자료형 내부의 데이터를 순차적으로 꺼내서
반복 작업하는 반복문 입니다.
- 시퀀스 자료형이란 여러 개의 값들을 모아놓은
집합 형태를 말하며, 대표적으로 문자열, 리스트 등이 있습니다.
- 리스트란 []안에 데이터들을 순차적으로 나열해 놓은 일종의
순차적 배열입니다.
for 제어변수 in 시퀀스 자료형:
    반복 실행문
'''

for num in [1,2,3,4,5,6,7,8,9,10]:
    print('반복문 돌아라~', num)

total = 0
for n in [1,2,3,4,5,6,7,8,9,10]:
    total += n
    print(total)