'''
    작성일: 2023년 9월 20일
    작성자: 컴공부 202395018 변형종
    설명: 선택문 if-else
            random을 이용한 가위바위보 게임.
            
            random함수로 생성된 정수를 가지고 게임을 진행.
            0 -> 가위, 1 -> 바위 2 -> 보
            
            2명의 플레이어의 이름을 입력받아 가위바위보 게임을 진행합니다.
'''

import random # random함수 가져오기, 포함 시키기

print("<가위바위보 게임 시작>")

player1 = input("player1의 이름: ")
player2 = input("player2의 이름: ")

num1 = random.randrange(3) # 랜덤으로 0, 1, 2 생성하여 변수에 저장.
num2 = random.randrange(3)

print(player1, ":", end='')
if num1 == 0 :
    print("가위")

if num1 == 1 :
    print("바위")

if num1 == 2 :
    print("보")

print(player2, ":", end='')
if num2 == 0 :
    print("가위")

if num2 == 1 :
    print("바위")

if num2 == 2 :
    print("보")
    
if (num1 == 0 and num2 == 2) or (num1 == 1 and num2 == 0) or (num1 == 2 and num2 == 1) :
    print(f"{player1}님 승리")
elif num1 == num2 :
    print("무승부입니다.")
else:
    print(f"{player2}님 승리")