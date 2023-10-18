'''
    작성일: 2023년 10월 18일
    작성자: 컴공부 202395018 변형종
    설명: 입력을 받아 맛있는 과일의 리스트를 만들자
    
    좋아하는 과일 5개를 입력받아 리스트에 저장한다.
    과일 이름을 입력하여 해당 과일이 리스트에 있는지 없는지 판단한다.
    
    append() 메소드
    찾기 in 연산자
'''
# 빈 리스트 생성
fruits = []

# 5벗 반복하면서 과일 이름 입력받아 리스트에 저장
for i in range(5):
    fruits_name = input(str(i+1)+"좋아하는 과일을 입력하시오: ")
    fruits.append(fruits_name) # 입력받은 변수의 값을 리스트에 추가
print("입력한 과일 리스트: ", fruits)

# 찾기
favo_fruits = input("좋아하는 과일 하나를 입력하시오: ")

# 사용자가 입력한 과일이 리스트에 있는지 판단
# 있으면 -> 00은 당신이 좋아하는 과일입니다.
# 없으면 -> 00은 당신이 좋아하는 과일이 아닙니다.

if favo_fruits in fruits :
    print(f"{favo_fruits}은/는 당시닝 좋아하는 과일입니다.")
else :
    print(f"{favo_fruits}은/는 당시닝 좋아하는 과일이 아닙니다.")