'''
작성일: 2023년 6월 7일
학과 : 컴퓨터공학부
학번 : 202395035
이름 : 도스톤벡
설면 : 9장 파일 입출력
'''
# 함수 생선 - 메인 프로그램 전에 만들기

# 안녕하세요 3번 출력하는 함수
def print_3_time() :
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")


print("== 함수호출 1 ==")

# 안녕하세요 3번 출력하는 함수 호출
print_3_time()

print("-------------------")

def print_n_time(value,n) :
    for i in range(n) :
        print(value)

print("함수 호출 2")
print_n_time('hi~!', 5)

# 반지름을 입력 받아 원의 넓이를 구하시오.
# 반지름을 전달받아 
# 원의 넓이를 계산하여 결과 값을 돌려주는 함수를 작성하시오.

# 알고리즘
# * 함수
#      3. 반지름을 전달 받는다
#               1. 원의 넓의를 계산한다
#               2. 넓의 값을 돌려준다
# * 메인
#      1. 반지름을 입력 받는다.
#      2. 입력 받은 반지름을 가지고 함수를 호출한다.
#      4. 원의 넓의를 출력한다

def circle_area(radius) :
    result = radius * radius * 3.14
    return result
    
r = int(input("반지름 입력 : "))
result = circle_area(r)
print("반지름이 {}인 원의 넓이는 {}" .format(r, result))
     
                        # 함스 호출하여 돌려받은 결과값을 바로 출력
print("반지름이 {}인 원의 넓이는 {}" .format(r, circle_area(r)))

print("-------------------")

# 두 정수를 입력 받아 큰 수를 출력하시오.
# 큰 수를 판별하여 결과를 돌려주는 함수를 작성하시오.

# 알고리즘
# * 한수
#  3. 전당 반응 두 수를 
#        1) 둘 중 큰 수를 판단한다. 
#            만약에 첫번째수가 두번째수보다 크면
#                  a. 두번째 수를 돌려준다.
# * 메인
#   1. 두 정수 입력 받기.
#   2. 두 정수를 가지고 함수 호출하기
#   4. 돌려 받은 결과 출력하기 

def max_num(num1, num2) :
    if num1 > num2 :
        return num1
    else :
        return num2

num1 = int(input("첫번째 숫자 입력 : "))
num2 = int(input("두번째 숫자 입력 : "))

print("두 숫자 중 큰 수 : ", max_num(num1, num2))

