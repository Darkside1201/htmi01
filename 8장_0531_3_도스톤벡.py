'''
작성일: 2023년 5월 31일
학과 : 컴퓨터공학부
학번 : 202395035
이름 : 도스톤벡
설면 :
'''
# writelines() 메소드
list1 = ['월요일/n','화요일/n','수요일/n','목요일/n','금요일/n']

# readline() 메소드 사용하여 파일의 모든 내용을 리스트로 변환
print("== 리스트로 반환 ==")
with open("Linetext.txt", "r") as f :
    textList = f.readline()
    print(textList)
    print("textList 자료형 : ", type(textList))

    