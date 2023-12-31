'''
    작성일: 2023년 10월 4일
    작성자: 컴공부 202395018 변형종
    설명: 더하기 암산 문제 만들기
            2개의 수로 더하기 결과를 맞추는 게임
            2개의 수는 1~100사이 랜덤으로 출제 됨.
            사용자가 0을 입력하면 프로그램은 종료.
            즉, 사용자가 0을 입력하기 전까지는 무한 반복하여 문제 풀기
            정답을 맞추면 참 잘했어요! 출력
            틀리면 정답을 알려주고 정답은 00입니다. 틀렸습니다. 출력
            
    문제 분석: 랜덤 수 생성 => import random
                                random.randint(1, 100)
                                
    알고리즘: 무한 반복 하면서
                두 정수를 랜덤으로 생성한다
                합계를 계산한다
                사용자에게 두 수를 보여주고 한계 계산 값을 입력받는다.
                만약 입력 값이 0이면
                반복을 종료한다
'''
import random

while True:

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    num3 = int(input(f"{num1} + {num2} = "))     # 사용자에게 두 수의 합을 정수로 입력받기
    hab = num1 + num2

    if num3 == 0:
        break
    if num1 + num2 == num3:         # 만약 두 난수의 합이 사용자에게 입력받은 값과 같다면
        print("잘했어요!!")          # 잘했어요 문장 출력
    else :
        print(f"정답은 {hab} 입니다. 틀렸습니다.")