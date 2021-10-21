import os
from time import sleep
import new_user as nu
import existing_user as eu

clear = lambda : os.system('cls')

def start_menu():
    clear()
    print("1. 기존사용자")
    print("2. 신규사용자\n")

    num = input("번호를 입력해주세요 : ")

    if num == '':
        clear()
        print("입력된 값이 없습니다. 다시 입력해주세요.")
        sleep(2)
        clear()
        start_menu()
    elif num == '1':
        clear()
        eu.existing_user()
    elif num == '2':
        clear()
        nu.new_user()
    else:
        clear()
        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
        sleep(2)
        clear()
        start_menu()
