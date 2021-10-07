import os
from time import sleep
import main_menu as mm

clear = lambda : os.system('cls')

def existing_user():
    error_count = 0     #비밀번호 불일치 횟수
    id_correct = 0      #ID가 일치하는지 1(True) or 0(False)

    while True:
        clear()

        if 0 < error_count < 3:                               #불일치 횟수 및 재입력
            print("사용자 ID 혹은 PW가 옳지 않습니다.({}회)".format(error_count))
        elif error_count == 3 and id_correct == True:         #ID 일치, PW 3회 불일치일 경우 힌트제공
            print("사용자 ID 혹은 PW가 옳지 않습니다.({}회)".format(error_count))
            print("힌트를 드립니다.\n")
            print("힌트질문:", id_data[1])
            answer = input("힌트 답: ")

            if answer == id_data[2]:
                clear()
                print("ID는 ", id)
                print("PW는 ", id_data[0])
                print("입니다.")
                sleep(2)
                clear()
        elif error_count == 3:                                 #ID 3회 불일치일 경우
            print("사용자 ID 혹은 PW가 옳지 않습니다.({}회)".format(error_count))
            sleep(2)
            clear()
            exit()

        path_dir = 'Data'                #Data 디렉터리 
        id_list = os.listdir(path_dir)   #Data 디렉터리에 있는 id.txt들

        id = input("ID : ")
        pw = input("PW : ")

        for i in range(len(id_list)):       #존재하는 ID 중에서 입력한 ID가 있는지 체크
            position = id_list[i].find('.')
            id_list[i] = id_list[i][:int(position)]     #ID.txt 문자열로 저장되어있기때문에 ID 문자열로만 저장하는 작업
            if id == id_list[i]:
                id_correct = 1
                break
            elif i == len(id_list)-1:       #Data 디렉터리내의 모든 파일 검사 후 불일치 횟수 증가
                error_count = error_count + 1
                id_correct = 0
                continue

        if id_correct == True:              #ID가 일치하면 파일접근
            with open("Data\\"+id+".txt", "r", encoding='utf8') as id_file:
                id_data = id_file.readlines()
                for i in range(len(id_data)):    
                    id_data[i] = id_data[i].strip()     #필드 문자열에 포함된 개행(\n)제거 후 저장
                if pw == id_data[0]:
                    clear()
                    print(id, "님 환영합니다.")
                    sleep(2)
                    mm.main_menu()
                    exit()
                elif pw != id_data[0]:
                    error_count = error_count + 1
                    continue