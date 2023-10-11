'''
    작성일: 2023년 10월 11일
    작성자: 컴공부 202395018 변형종
    설명: 여러개의 값을 넘겨주고 여러개의 값을 돌려받기
    
    두 수를 전달받아 사직 연산의 결과값을 돌려주는 함수
    
    [알고리즘]
    (함수)
        3. 전달받은 2개의 값을 매개 변수에 저장
        4. 두 수를 가지고 사직연산(+ - * / %)를 계산한다
        5. 사직연산의 결과 5개를 돌려준다
    
    (메인)
        1. 두 수를 입력받는다
        2. 두 수를 가지고 함수를 호출한다
        6. 돌려받은 결과를 출력한다
'''
# 함수선언
def cals(num1, num2):
    sum = num1 + num2
    minus = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    rest = num1 % num2
    return sum, minus, mul, div, rest # 돌려주는 결과는 5개
num1 = int(input("첫 번쨰 수 입력: "))
num2 = int(input("두 번째 수 입력: ")) 

sum, minus, mul, div, rest = cals(num1, num2)  
print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {minus}") 
print(f"{num1} * {num2} = {mul}") 
print(f"{num1} / {num2} = {div}") 
print(f"{num1} % {num2} = {rest}")