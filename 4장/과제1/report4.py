'''
    작성일: 2023년 9월 20일
    작성자: 컴공부 202395018 변형종
    설명: 파이썬의 random.randint(1, 100)을 이용하여 1에서 100 사이의 임의의 난수 2개를 생성하여라.
            다음으 로 두 수의 합을 묻는 질문을 사용자에게 던지도록 하자.
            만일 사용자가 두 수의 합을 맞추면 '잘했어요!!'를 출 력하여라. 만일 틀릴 경우 '정답은 000입니다.'를 출력하여라.
'''

import random

num1 = random.randrange(101)    # 첫번째 난수
num2 = random.randrange(101)    # 두번째 난수
num3 = int(input(f"{num1} + {num2} = "))     # 사용자에게 두 수의 합을 정수로 입력받기
hab = num1 + num2

if num1 + num2 == num3:         # 만약 두 난수의 합이 사용자에게 입력받은 값과 같다면
    print("잘했어요!!")          # 잘했어요 문장 출력
else :
    print(f"정답은 {hab} 입니다.")