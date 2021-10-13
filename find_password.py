import os
from time import sleep
import pandas as pd
import main_menu as mm

clear = lambda : os.system('cls')

def find_password(id):
    while True:
        print('저장된 사이트 리스트')
        with open("Data\\"+id+".txt", "r", encoding='utf8') as user_info:
            dns = []
            id_list = []
            pw_list = []
            condition1 = []
            condition2 = []
            condition3 = []
            condition4 = []
            condition5 = []
            cnt = 1

            for line in user_info.readlines()[3:]:
                line = line.strip()
                user_info_row = line.split(',')
                dns.append(user_info_row[0])
                id_list.append(user_info_row[1])
                pw_list.append(user_info_row[2])
                condition1.append(user_info_row[3])
                condition2.append(user_info_row[4])
                condition3.append(user_info_row[5])
                condition4.append(user_info_row[6])
                condition5.append(user_info_row[7])
                row_len = cnt
                cnt = cnt + 1

            # dns.sort()
            df_user_info = pd.DataFrame({'사이트':dns, 'ID':id_list, 'PW':pw_list,
                                        'condition1':condition1, 'condition2':condition2, 'condition3':condition3,
                                        'condition4':condition4, 'condition5':condition5})
            
            for i in range(row_len):
                print('{}. {}'.format(i+1, df_user_info['사이트'][i]))
            try:
                num = input('\nPW를 확인하고자 하는 사이트의 번호를 입력해주세요: ')
                num = int(num)
                if 0 < num <= row_len:
                    clear()
                    print("ID는 {}".format(df_user_info['ID'][num-1]))
                    print("PW는 {}".format(df_user_info['PW'][num-1]))
                    print("입니다.")
                    print("아무키나 누르면 메인화면으로 돌아갑니다.")
                    sleep(2)
                    clear()
                    mm.main_menu(id)
                else:
                    clear()
                    print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                    sleep(2)
                    clear()
                    continue
            except ValueError:
                if num == "":
                    clear()
                    print("입력된 값이 없습니다. 다시 입력해주세요.")
                    sleep(2)
                    clear()
                    continue
                else:
                    clear()
                    print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                    sleep(2)
                    clear()
                    continue