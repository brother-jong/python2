'''
    작성일: 2023년 9월 13일
    작성자: 컴공부 202395018 변형종
    설명: 90페이지 문제 3.9
        평균 시속과 이동 시간을 입력받아
        이동 시간은 시,분,초 단위로 출력하고,
        이동한 거리를 계산하여 출력하시오.
'''

# 평균 시속 입력 받기
km = float(input("평균 시속(km/h)을 입력하세요: "))

# 이동 시간 입력 받기
h = float(input("이동 시간(시)을 입력하세요: "))

# 이동한 거리 계산하기
move = km * h

# 이동 시간을 분으로 변환
movetime = h * 60

# 이동 시간을 시, 분, 초로 변환하기
hours = int(movetime // 60)
minutes = int(movetime % 60)
seconds = int((movetime * 60) % 60)

print("평균 시속: {}km/h" .format(km))
print("이동 시간: {}시간 {}분 {}초" .format(hours, minutes, seconds))
print("이동 거리: {}km" .format(move))