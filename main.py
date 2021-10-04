import os

def clear():
    os.system('cls')

def start_menu():
    print("1. 기존사용자")
    print("2. 신규사용자\n")
    num = int(input("번호를 입력해주세요 : "))
    if(num != 1 or num != 2):
        start_menu()
    else:
        clear()
        return num

def existing_user(num):
    if(num == 1):
        id = input("ID : ")
        pw = input("PW : ")

start_menu()