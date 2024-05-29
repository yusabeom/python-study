'''
* 리스트 (list)
- 리스트는 여러 개의 값을 집합적으로 저장하기 위해
사용하는 파이썬의 자료형 입니다.
- 다른 언어의 배열과 유사한 개념이며, 실제로 배열과
유사한 방식으로 데이터가 관리됩니다.
- [] (대괄호) 안에 요소를 콤마로 구분하여 나열합니다.
'''
list = [5, 6, 10, 'a', 5.67] # 어떤 타입이든 저장이 가능합니다.

for c in list:
    print(c)

print('리스트의 길이:', len(list))