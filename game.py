# 밥 무러간다
# 메뉴 1 2 3 아무거나 정해서
# 먹는 메뉴를 선택해서 메뉴를 출력
### 아래 전체를 반복 ###
for i in range(1,4):
    print("밥 무러 가보자")
    print("메뉴는?")
    print("1.학식 2.분식 3.중식")
    menu = input(str(i) + ".입력 : ")
    #만약에 사용자의 입력값이 1과 같으면
    if menu == '1' :
            print("학식 가보자")
    if menu == '2' :
            print("분식 가보자")
    if menu == '3' :
            print("중식 가보자")
    print("")
### 여기까지 반복 ###