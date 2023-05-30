'''
작성일: 2023년 5월 30일
학과 : 컴퓨터공학부
학번 : 202395035
이름 : 도스톤벡
설면 : 8장 파일 입출력
'''
# writelines() 메소드 
list = ['월요일/n','화요일/n','수요일/n','목요일/n','금요일/n']
list2 = [1,2,3,4,5]

with open("Linetest.txt", "w") as f : # 파일 오픈(쓰기)
    f.writelines(list1)   # 중 단위 덱스트 파일 쓰기
    f.writelines(list1)   # 오류 발생.
    
# with문을 사용하여 파일 객체를 생선하는 경우
# f.close() 쓸 필요 없다