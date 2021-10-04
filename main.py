import os

def clear():
    os.system('cls')

def start_menu():
    print("1. 기존사용자")
    print("2. 신규사용자\n")
    num = int(input("번호를 입력해주세요 : "))
    if num != 1 and num != 2:
        start_menu()
    elif num == 1:
        existing_user()
    elif num == 2:
        new_user()

        

def existing_user():
    id = input("ID : ")
    pw = input("PW : ")

def new_user():
    pass

start_menu()
