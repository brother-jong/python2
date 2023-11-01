'''
    작성일: 2023년 11월 1일
    작성자: 컴공부 202395018 변형종
    설명: lab 7-8 함수는 튜플을 돌려줄 수 있다

        반지름을 입력받아 원의 넓이와 둘레를 계산히시오.
        넓이와 둘레를 계산하는 함수를 작성하시오.
        함수는 넓이와 둘레를 함께 돌려줍니다.(return)
        
        [함수]
        3. 반지름을 받아서 매개 변수에 저장
        4. 넓이와 둘레를 계산한다
        5. 넓이와 둘레를 돌려준다(힘수 호출한 곳으로)
            return 넓이, 둘레
        
        [메인]
        1. 반지름을 입력받는다.
        2. 함수 호출 -> 반지름을 가지고 호출
        6. 돌려받은 넓이와 둘레를 저장
            (넓이, 둘레)
        7. 출력
'''
import math

def calcircle(radius):
    area = math.pi * radius ** 2
    circum = 2 * math.pi * radius
    return area, circum

radius = float(input("반지름을 입력하세요: "))
area, circum = calcircle(radius)
print(f"넓이: {area:.2f}")
print(f"둘레: {circum:.2f}")
print(f"반지름: {radius:.2f}")

circle = calcircle(radius)
print(f"반지름이 {radius}의 원의 넓이는 {circle[0]:.2f}이고, 원의 둘레는 {circle[1]:.2f}이다.")