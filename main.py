import os
from time import sleep
import new_user as nu
import existing_user as eu

clear = lambda : os.system('cls')

def start_menu():
    clear()
    print("1. 기존사용자")
    print("2. 신규사용자\n")
    num = int(input("번호를 입력해주세요 : "))
    if num != 1 and num != 2:
        clear()
        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
        sleep(2)
        clear()
        start_menu()
    elif num == 1:
        eu.existing_user()
    elif num == 2:
        nu.new_user()

start_menu()
