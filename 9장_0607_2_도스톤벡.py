'''
작성일: 2023년 6월 7일
학과 : 컴퓨터공학부
학번 : 202395035
이름 : 도스톤벡
설면 : 9장 파일 입출력
'''

import random

def make_question() :
    num1 = random.randint(1, 40)
    num1 = random.randint(1, 20)
    op = random.randint(1, 3)
    
    que = str (num1)
    
    if op == 1:
        que = que + '+'
    if op == 1:
        que = que + '-'
    if op == 1:
        que = que + '*'
        
    que = que + str(num2)
    
    return que

R_ans = 0
W_ans = 0

for i  in range(5) :
    que = make_question()
    print(que, end='')
    
    result = int(input('='))
    
    if eval(que) == result :
        print('정답입니다')
        R_ans += 1
    else :
        print('오답입니다')
        W_ans += 1
        
print('정답 : ', R_ans, '오답 : ', W_ans)

if R_ans == 5 :
    print("당신은 천재 입니다")        

    