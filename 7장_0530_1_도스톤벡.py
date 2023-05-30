'''
작성일: 2023년 5월 30일
학과 : 컴퓨터공학부
학번 : 202395035
이름 : 도스톤벡
설면 : 7장 세트와 딕셔너리


키(key)와 값(value)를 한 요소로 묶어 표현한 자료구조
키는 중복을 허용하지 않음
세트처럼  
'''
# 딕셔너리 생선 
dic1 = {1:'one', 2:'two', 3:'three'}
print("딕셔너리 dict1 내용 : ", dict)

# 리스트를 딕셔너리로 변환
dic1 = {[1:'하나'], [2:'둘'], [3:'셋']}
dic2 = dict(list)
print("리스트 list1 내용 : ", list)
print("리스트 dict2 내용 : ", dict)

# 키(key)를 지정하여 값(value) 검색
print("딕셔너리 dict2의 키 3을 한글로 무엇인까? :") 

#딕셔너리 모든 요소 삭제
dict.clear()
print("딕셔너리 dict2 내용 : ", dict)

#keys() 메소드 이용하여 사전의 모든 키 출력
print("dict1의 key :", end='')
# 반복문 사용하여 키 출력
for num in dict.keys() :
    print(num, end='')
print()

# vlaues() 메소드 이용하여 사전의 모든 값 출력
print("dict1의 value :", end='')
#반복문 사용하여 값 출력
for alpanum in dict.vlaues() :
    print(alpanum, end='')
print()

# items() 메소드 이용하여 사전의 모든 키와 값 출력 
