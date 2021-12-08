import os
from time import sleep
import new_password as np
import find_password as fp
import change_password as cp
import remove_password as rm

clear = lambda : os.system('cls')

def main_menu(user_exiting_id):
    clear()
    print("1. 기존 PW 찾기")
    print("2. 기존 PW 변경")
    print("3. 새로운 PW 추가")
    print("4. 저장된 PW 삭제")
    print("5. 시스템 종료\n")
    num = input("번호를 입력하여, 메뉴를 선택해주세요:")
    if num == '':
        clear()
        print("입력된 값이 없습니다. 다시 입력해주세요.")
        sleep(2)
        clear()
        main_menu(user_exiting_id)
    elif num == '1':
        clear()
        fp.find_password(user_exiting_id)
    elif num == '2':
        clear()
        cp.change_password(user_exiting_id)
    elif num == '3':
        clear()
        np.new_password(user_exiting_id)
    elif num == '4':
        rm.remove_password(user_exiting_id)
    elif num == '5':
        #암호화
        encoding_line = ""
        encoding_line2 = ""
        with open("Data\\{}.txt".format(user_exiting_id), "r", encoding='utf8') as user_info:
            for line in user_info.readlines():
                for i in line:
                    if i == '\n':
                        encoding_line += '\n'
                        continue
                    elif i == '\t':
                        encoding_line += '\t'
                        continue
                    elif 65 <= ord(i) <= 122:
                        tmp = ord(i)-30
                    elif 33 <= ord(i) <= 64:
                        tmp = ord(i)-30
                    else:
                        tmp = ord(i)-100
                    encoding_line += chr(tmp)
        with open("Data\\{}.txt".format(user_exiting_id), "w", encoding='utf8') as user_info:
            user_info.write(encoding_line)

        with open("Data\\{}.txt".format("pw_conditions"), "r", encoding='utf8') as user_info:
            for line in user_info.readlines():
                for i in line:
                    if i == '\n':
                        encoding_line2 += '\n'
                        continue
                    elif i == '\t':
                        encoding_line2 += '\t'
                        continue
                    elif 65 <= ord(i) <= 122:
                        tmp = ord(i)-30
                    elif 33 <= ord(i) <= 64:
                        tmp = ord(i)-30
                    else:
                        tmp = ord(i)-100
                    encoding_line2 += chr(tmp)
        with open("Data\\{}.txt".format("pw_conditions"), "w", encoding='utf8') as user_info:
            user_info.write(encoding_line2)        
        exit()
    else:
        clear()
        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
        sleep(2)
        clear()
        main_menu(user_exiting_id)
