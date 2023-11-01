'''
    작성일: 2023년 11월 1일
    작성자: 컴공부 202395018 변형종
    설명: lab 7-6 도시의 이름과 인구를 튜플로 묶어보자

        반지름을 입력받아 원의 넓이와 둘레를 계산히시오.
        넓이와 둘레를 계산하는 함수를 작성하시오.
        함수는 넓이와 둘레를 함께 돌려줍니다.(return)
        
        [함수]
        3. 반지름을 받아서 매개 변수에 저장
        4. 넓이와 둘레를 계산한다
        5. 넓이와 둘레를 돌려준다(힘수 호출한 곳으로)
            return 넓이, 둘레
        
        [메인]
        1. 반지름을 입력받는다.
        2. 함수 호출 -> 반지름을 가지고 호출
        6. 돌려받은 넓이와 둘레를 저장
            (넓이, 둘레)
        7. 출력
'''
# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울', 9765), ('부신', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]

max_pop = 0 # 최대 인구 수 (작은 수)
min_pop = 999999999999999999 # 최소 인구 수 (큰 수)
total_pop = 0 # 평균 인구 수

max_city = None # 큰 도시는 없음
min_city = None # 작은 도시는 없음

for city in city_info:
    total_pop += city[1]
    if city[1] > max_pop :
        max_pop = city[1]
        max_city = city
    if city[1] < min_pop :
        min_pop = city[1]
        min_city = city
print('최대인구: {0}, 인구: {1}, 천명'.format(max_city[0], max_city[1]))
print('최소인구: {0}, 인구: {1}, 천명'.format(min_city[0], min_city[1]))
print('리스트 도시 평균 인구: {0} 천명'.format(total_pop / len(city_info)))