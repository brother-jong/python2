'''
    작성일: 2023년 11월 1일
    작성자: 컴공부 202395018 변형종
    설명: 8.1 키와 값을 가지는 딕셔너리
    
    튜플 = () 리스트 = [] 딕녀서리 = {}
'''
# 빈 딕셔너리 생성
phone_book1 = {}

# 딕셔너리에 값 저장. key, value
phone_book1['변형종'] = '01091725620'

print("phone_book1: ", phone_book1)

# 딕셔너리에 값 저장. 2. {key: value}
phone_book2 = {'변형종': '01091725620', '친구': '01099999999'}
print("phone_book2: ", phone_book2)

phone_book3 = {}
phone_book3['변형종'] = '01091725620'
phone_book3['문재인'] = '01075963549'
phone_book3['이재명'] = '01045786935'
phone_book3['윤석열'] = '01069696969'
phone_book3['안철수'] = '01058245369'

print('phone_book3: ', phone_book3)

print()
print(":: 전화번호 phone_book3 출력 ::")
# 모든 key 출력
print(phone_book3.keys())
# 모든 value 출력
print(phone_book3.values())
print(phone_book3.items())

print()
print(":: 전화번호 phone_book3 items()출력 ::")
for name, phone_num in phone_book3.items():
    print(name, ':', phone_num)
    
print()
print(":: 전화번호 phone_book3[keys]로 접근하여 출력 ::")
for key in phone_book3.keys():
    print(key, ":", phone_book3[key])
    
print()
print("딕셔너리 작성 시 :(콜론)을 기준으로 key:value 작성")
person_dict = {'name': '변형종', 'age': '19', 'clase': '1학년'}

print('name: ', person_dict['name'])
print('age: ', person_dict['age'])
print('clase: ', person_dict['clase'])

print()

print(":: 정렬 ::")
# phone_book3를 설정
print(sorted(phone_book3))

print(':: 키를 기준으로 전체 정렬 ::')
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0])
print(sort_phone_book3)

print(":: 값을 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1])
print(sort_phone_book3)

print()

print(":: 삭제 ::")
del phone_book3['변형종']
print(phone_book3)

print(":: 전체 삭제 ::")
phone_book3.clear()
print(phone_book3)