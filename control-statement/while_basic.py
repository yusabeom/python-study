'''
* 반복문 (loop)
- 반복문은 유사한 명령을 횟수를 지정하여 반복 실행하는 제어문 입니다.
- 파이썬의 반복문 키워드는 while, for ~ in 이 있습니다.
'''

# while문에 필요한 3요소: 제어변수begin, 조건식end, 증감식step

i = 1 #begin
total = 0

while i <= 10: # end
    total += i
    i += 1 # 파이썬은 증감 연산자가 없습니다.

print('1부터 10까지의 누적합: ',  total)

'''
- 정수를 2개 (x, y) 입력받아 x부터 y까지의
 누적합계를 while을 사용하여 구하는 코드를 만드세요.
 ex) "x부터 y까지의 누적합계: z"
- 처음에는 x가 무조건 작은 값이 들어올 것이다 라고 가정하고 
 작성하세요.
그 후, 만약 x가 y보다 더 큰 값이 들어왔을 때는,
어떻게 대처할 지 생각해 보세요. (while을 2번쓰는 건 아니에요~)
'''

x = int(input('x를 입력하세요: '))
y = int(input('y를 입력하세요: '))
total = 0

if x > y:
    x, y = y, x

while x <= y:
    total += x
    x += 1
print(total)