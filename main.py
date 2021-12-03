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
        cnt = 0
        for ids in id_list:
            cnt += 1
            # position = ids.find('.')
            # if not (4<=position<=10 or line[position+1:]=='txt'):
            #     print("규칙에 위배되는 데이터가 존재합니다1.")
            #     sleep(2)
            #     exit()

            # 복호화
            with open("Data\\{}".format(ids), 'r', encoding='utf8') as user_info:
                text = ''
                for line in user_info.readlines():
                    text += line
            with open("Data\\{}".format(ids), 'w', encoding='utf8') as user_info:
                decoding_line = ''
                for i in text:
                    if i == '\n':
                        decoding_line += '\n'
                        continue
                    elif i == '\t':
                        decoding_line += '\t'
                        continue
                    elif 65-30 <= ord(i) <= 122-30:
                        tmp = ord(i)+30
                    elif 33-30 <= ord(i) <= 64-30:
                        tmp = ord(i)+30
                    else:
                        tmp = ord(i)+100
                    decoding_line += chr(tmp)
                user_info.write(decoding_line)

            # with open("Data\\{}".format(ids), 'r', encoding='utf8') as user_info:
            #     for i, line in enumerate(user_info.readlines()[:3]):
            #         if i == 0:
            #             pw = line.strip()
            #         if i == 1:
            #             hint_question = line.strip()
            #         if i == 2:
            #             hint_answer = line.strip()
            #     for i in pw:
            #         if not (48<=ord(i)<=57 or 65<=ord(i)<=90 or 97<=ord(i)<=122) or not 4<=len(pw)<=10:
            #             clear()
            #             print("규칙에 위배되는 데이터가 존재합니다2.")
            #             sleep(2)
            #             exit()
            #     if not (len(hint_question) <= 50 or len(hint_answer) <= 50):
            #             clear()
            #             print("규칙에 위배되는 데이터가 존재합니다3.")
            #             sleep(2)
            #             exit()
        if cnt < 2:
            if ids == "pw_conditions":
                clear()
                print("기존사용자가 등록되어 있지 않습니다.")
                print("신규사용자를 등록해주세요.")
                sleep(2)   
                clear()
                nu.new_user()  
        sm.start_menu()
                    
    else:
        clear()
        print("기존사용자가 등록되어 있지 않습니다.")
        print("신규사용자를 등록해주세요.")
        sleep(2)   
        clear()
        nu.new_user()
    
integrity_test()
