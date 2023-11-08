'''
    작성일: 2023년 11월 8일
    작성자: 컴공부 202395018 변형종
    설명: 파티 동시 참석자 알아내기
'''

partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.")
print(partyA.intersection(partyB))
print("파티 A, B에 참석한 사람들", partyA.union(partyB))
print("파티 A, B에 중복없이 참석한 사람", partyA.symmetric_difference(partyB))
print("파티 A만 참석한 사람", partyA.difference(partyB))