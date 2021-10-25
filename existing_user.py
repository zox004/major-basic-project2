import os
from time import sleep
import main_menu as mm

clear = lambda : os.system('cls')

def existing_user():
    error_count = 0     #비밀번호 불일치 횟수
    user_exiting_id_correct = 0      #ID가 일치하는지 1(True) or 0(False)

    while True:
        clear()

        if 0 < error_count < 3:                               #불일치 횟수 및 재입력
            print("사용자 ID 혹은 PW가 옳지 않습니다.({}회)".format(error_count))
        elif error_count == 3 and user_exiting_id_correct == True:         #ID 일치, PW 3회 불일치일 경우 힌트제공
            print("사용자 ID 혹은 PW가 옳지 않습니다.({}회)".format(error_count))
            print("힌트를 드립니다.\n")
            print("힌트질문:", existing_user_id_data[1])
            answer = input("힌트 답: ")
            if answer == "":
                clear()
                print("입력된 값이 없습니다. 다시 입력해주세요.")
                sleep(2)
                clear()
                continue
            if answer == existing_user_id_data[2]:
                clear()
                print("ID는 ", existing_user_id)
                print("PW는 ", existing_user_id_data[0])
                print("입니다.")
                sleep(5)
                clear()
                existing_user()
            else:
                exit()
        elif error_count == 3:                                 #ID 3회 불일치일 경우
            print("사용자 ID 혹은 PW가 옳지 않습니다.({}회)".format(error_count))
            sleep(2)
            clear()
            exit()

        path_dir = 'Data'                #Data 디렉터리 
        user_id_list = os.listdir(path_dir)   #Data 디렉터리에 있는 id.txt들

        if user_exiting_id_correct == True:
            print("ID : {}".format(existing_user_id))
        else:
            existing_user_id = input("ID : ")
        if existing_user_id == '':
            clear()
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            clear()
            continue
        existing_user_pw = input("PW : ")
        if existing_user_pw == '':
            clear()
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            clear()
            continue

        for i in range(len(user_id_list)):       #존재하는 ID 중에서 입력한 ID가 있는지 체크
            position = user_id_list[i].find('.')
            user_id_list[i] = user_id_list[i][:int(position)]     #문자열 ID.txt로 저장되어있기때문에 문자열 ID로만 저장하는 작업
            if existing_user_id == user_id_list[i]:
                user_exiting_id_correct = 1
                break
            elif i == len(user_id_list)-1:       #Data 디렉터리내의 모든 파일 검사 후 error_count 없이 재입력받기
                clear()
                print("존재하지 않는 ID입니다. 다시 입력해주세요.")
                sleep(2)
                user_exiting_id_correct = 0
                continue

        if user_exiting_id_correct == True:              #ID가 일치하면 파일접근
            with open("Data\\"+existing_user_id+".txt", "r", encoding='utf8') as user_id_file:
                existing_user_id_data = user_id_file.readlines()
                for i in range(len(existing_user_id_data)):    
                    existing_user_id_data[i] = existing_user_id_data[i].strip()     #필드 문자열에 포함된 개행(\n)제거 후 저장
                if existing_user_pw == existing_user_id_data[0]:
                    clear()
                    print(existing_user_id, "님 환영합니다.")
                    sleep(2)
                    mm.main_menu(existing_user_id)
                    exit()
                elif existing_user_pw != existing_user_id_data[0]:
                    error_count = error_count + 1
                    continue
