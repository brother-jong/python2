'''
    작성일: 2023년 10월 4일
    작성자: 컴공부 202395018 변형종
    설명: 두 수를 입력받아
            1. 두 수 사이의 합계 출력하기
            2. 두 수 사이의 짝수의 합계 출력하기
            for 반복문과 while 반복문을 사용하여 1에서 100까지의 정수 중에서 홀수의 합을 출력하는 프로그램을 작성하여라.
 
'''
# 두 수를 입력받는다.
num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))
# 초기값 0으로 설정
sum = 0

# 두 수 사이의 합을 계산한다.
min_num = min(num1, num2)
max_num = max(num1, num2)

# min_num부터 max_num까지의 모든 수를 더한다.
for num in range(min_num, max_num + 1):
    sum += num

print(f"{min_num}부터 {max_num}까지의 합은 {sum}입니다.")

# 두 수를 입력받는다.
# num1 = int(input("첫 번째 수를 입력하세요: "))
# num2 = int(input("두 번째 수를 입력하세요: "))
# 초기값 0으로 설정
sum = 0

# 두 수 사이의 합을 계산한다.
# min_num = min(num1, num2)
# max_num = max(num1, num2)

# min_num부터 max_num까지의 수 중에서 짝수만 더한다.
for num in range(min_num, max_num + 1):
    if num % 2 == 0:
        sum += num

print(f"{min_num}부터 {max_num}까지의 짝수의 합은 {sum}입니다.")