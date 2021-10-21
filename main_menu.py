import os
from time import sleep
import new_password as np
import find_password as fp
import change_password as cp

clear = lambda : os.system('cls')

def main_menu(user_exiting_id):
    clear()
    print("1. 기존 PW 찾기")
    print("2. 기존 PW 변경")
    print("3. 새로운 PW 추가")
    print("4. 시스템 종료\n")
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
        exit()
    else:
        clear()
        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
        sleep(2)
        clear()
        main_menu(user_exiting_id)

