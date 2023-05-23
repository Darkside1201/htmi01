# 다중 리스트 
num = [[11,12,13], [21,22,23], [31,32,33,34], [41,42]]

# 리스트 내의 각각 리스트의  합계를 계산하여 출력
for i in range(len(num)) : # num 리스트의 길이만큼 반복
    total = 0
    for j in range(len(num[i])) : # 0번지의 길이까지 반복
        total = total + num
    print(i+1, "번째 줄의 합 : ", total)
    
    
# 실습 예제 5-6
# 1~100 사이의 램덤 수를 발생시키여 리스트에 저장하고,
# 합계, 최대값, 정렬도 하시오.
# 오름차순으로 정렬도 하시오.
import random   # 랜덤 함수를 포함.
num = []   # 빈 리스트 생선.

for i in range(10) :
    num.append(random.randint(1,100))

print("생선된 리스트 : ", num)
print("가장 큰은 값 : ", max(num))
print("가장 작은 값 : ", min(num))
print("리스트의 합 : ", sum(num))
num.sort()   # 정렬 후에 출력하기
print("정렬된 리스트 : ", (num))


