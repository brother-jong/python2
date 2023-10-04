'''
    작성일: 2023년 10월 4일
    작성자: 컴공부 202395018 변형종
    설명: 조건에 따라 반복하는 while문
'''
# while 조건식: : => : 반드시 사용.
#       들여쓰기로 반복하면서 할 일을 작성.

# 반복문에서는 반드시 종료 조건이 있어야한다.
# while True: 무한 반복

under_construction = True # 공사중.

# True일 동안 계속 반복
while under_construction:
    response = input("공사가 완료 되었습니까?")
    if response == "예": # 종료 조건
        under_construction = False # 공사 완료
        
print("루트 탈출!!!")