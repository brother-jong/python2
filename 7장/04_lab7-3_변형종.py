'''
    작성일: 2023년 10월 18일
    작성자: 컴공부 202395018 변형종
    설명: 도시의 인구  자료에 대한 슬라이싱하기
'''

people = ['Seoul', 9765, 'Busan', 3441, 'Incheon', 2954]

print("서울 인구: ", people[1])
print("인천 인구: ", people[-1])
print("각 도시 이름: ", people[0::2])
print("각 도시 인구 합: ", sum(people[1::2]))