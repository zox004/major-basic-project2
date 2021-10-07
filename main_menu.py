import os
from time import sleep

clear = lambda : os.system('cls')

def main_menu():
    clear()
    print("1. 기존 PW 찾기")
    print("2. 기존 PW 변경")
    print("3. 새로운 PW 추가")
    print("4. 시스템 종료\n")
    num = int(input("번호를 입력하여, 메뉴를 선택해주세요:"))
    if num == 1:
        pass
    elif num == 2:
        pass
    elif num == 3:
        pass
    elif num == 4:
        exit()

