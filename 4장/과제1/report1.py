'''
    작성일: 2023년 9월 20일
    작성자: 컴공부 202395018 변형종
    설명: 다음과 같이 사용자로부터 나이를 입력받아 20살 이상이면 "Adult", 
            10살 이상 20살 미만이면 "Youth", 10살 미만이면 "Kid"를 출력하는 프로그램을 
            if-elif-else 문을 사용하여 작성하시오.
'''

age = int(input("나이를 입력해주세요: "))

if age >= 20 :
    print("Adult")
elif ((age >= 10) and (age < 20)) :
    print("Youth")
else :
    print("Kid")