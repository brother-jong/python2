'''
    작성일: 2023년 9월 27일
    작성자: 컴공부 202395018 변형종
    설명: 반복문으로 팩토리얼 구하기
            오늘의 마지막 문제
'''

num = int(input("정수를 입력하시오: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print(num, "1은", fact, "이다.") 
