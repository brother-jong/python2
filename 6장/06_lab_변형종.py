'''
    작성일: 2023년 10월 11일
    작성자: 컴공부 202395018 변형종
    설명: LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수
    
    리스트에 10개의 값을 랜덤으로 생성하고,
    amx 또는 min을 입력받아 최대, 최소값을 찾아 돌려주는 함수
    
    (함수)
            5) 두 값을 전달받아 매개 변수에저장
            6) 최대값, 최소값을 찾는다
            7) 값을 돌려준다
    (메인)
        1. 무한반복
            1) 랜덤으로 10~99까지 10개의 수를 리스트로 셍성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대대값을 알고 싶은지 최소값을 알고 싶은지 묻는다
                사용자가 입력할 값은 max 또는 min
            4) 입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
            8) 돌려받은 최대값 또는 최소값을 출력한다.
'''
# 무한반복
import random

def su(numbers):
    # 최대값 찾기
    if choice == 'max':
        num_max = max(numbers)
        return num_max
    # 최소값 찾기
    elif choice == 'min':
        num_min = min(numbers)
        return num_min

while True:
    # 10개의 랜덤 숫자 리스트 생성
    num = [random.randint(1, 100) for _ in range(10)]
    print(f"생성된 리스트: {num}")
    
    # 사용자로부터 'max', 'min', '종료: c' 중 하나를 입력받기
    choice = input("최대값을 찾으려면 'max', 최소값을 찾으려면 'min'을 종료하려면 '종료: c'를 입력하세요: ").lower()
    
    # 종료 조건 확인
    if choice == 'c':
        print("프로그램을 종료합니다.")
        break
    
    # 올바른 입력인지 검증
    if choice in ['max', 'min', 'c']:
        # 함수 호출하여 결과 출력
        result = su(num)
        print("결과:", result)
    else:
        print("잘못된 입력입니다. 'max', 'min', '종료: c' 중 하나를 입력하세요.")
