'''
    작성일: 2023년 11월 8일
    작성자: 컴공부 202395018 변형종
    설명: 8.6문제
'''
student_tuple = [('211101', '강이안', '0101231111'), ('211102', '박동민', '0101232222'), ('211103', '김수정', '0101233333')]

student_dict = {}

# 1. 딕셔너리에 추가
for id_num, name, phone in student_tuple :
    student_dict[id_num] = [name, phone]
    
# 2. 딕셔너리 내용 출력
for key, value in student_dict.items() :
    print(key, " : ", value[0])
    
# 3. 학번 입력받아 이름과 연락처 출력
number = input("학번을 입력하세요: ")
print(number + '학생은' + student_dict[number][0] + '이며, 전화번호는' + student_dict[number][1] + '입니다.')