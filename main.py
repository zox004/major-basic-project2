import os
from time import sleep
import start_menu as sm
import new_user as nu
import pandas as pd

clear = lambda : os.system('cls')

def integrity_test():
    path_dir = 'Data'                #Data 디렉터리 
    id_list = os.listdir(path_dir)   #Data 디렉터리에 있는 id.txt들
    if id_list:
        clear()
        for line in id_list:
            position = line.find('.')
            if not (4<=position<=10 or line[position+1:]=='txt'):
                print("규칙에 위배되는 데이터가 존재합니다.")
                sleep(2)
                exit()
            with open("Data\\{}".format(line), 'r', encoding='utf8') as user_info:
                for i, line in enumerate(user_info.readlines()[:3]):
                    if i == 0:
                        pw = line
                    if i == 1:
                        hint_question = line
                    if i == 2:
                        hint_answer = line
                for i in pw:
                    if not (48<=ord(i)<=57 or 65<=ord(i)<=90 or 97<=ord(i)<=122 or 4<len(pw)<10):
                        clear()
                        print("규칙에 위배되는 데이터가 존재합니다.")
                        sleep(2)
                        exit()
                if not (len(hint_question) <= 50 or len(hint_answer) <= 50):
                        clear()
                        print("규칙에 위배되는 데이터가 존재합니다.")
                        sleep(2)
                        exit()
        sm.start_menu()
                    
    else:
        clear()
        print("기존사용자가 등록되어 있지 않습니다.")
        print("신규사용자를 등록해주세요.")
        sleep(2)
        clear()
        nu.new_user()
        pass
integrity_test()
