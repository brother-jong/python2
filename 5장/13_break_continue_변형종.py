'''
    작성일: 2023년 10월 4일
    작성자: 컴공부 202395018 변형종
    설명: 반복을 제어하는 break, continue
    교재 137페이지
    
    test word: programming
'''
word = input("단어를 입력하세요: ")

print(":: break1 ::")
for i in word:
    # a 또는 e 또는 i 또는 o 또는 u면
    if i == 'a' or i == 'e' or i == 'i' or i =='o' or i =='u':
        # 멈춤
        break
    else:
        print(i, end='')
        
print()

print(":: break2 ::")
for i in word:
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']: # 모음을 만나면 반복 중지
        break # 반복을 중단한다. 반복을 빠져나간다.
    else:
        print(i, end='')
        
print()

print(":: break3 ::")
for i in word:
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']: # 모음을 만나면 반복 중지
        continue # 반복의 시작으로 돌아감. 아래 문장을 만날 수 없음.
    else:
        print(i, end='')