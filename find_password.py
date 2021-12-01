import os
from time import sleep
import pandas as pd
import main_menu as mm
from msvcrt import getch

clear = lambda : os.system('cls')

def find_password(user_id):
    while True:
        print('저장된 사이트 리스트')
        with open("Data\\"+user_id+".txt", "r", encoding='utf8') as user_info:
            dns = []
            id_list = []
            pw_list = []
            row_len = 0
            cnt = 1

            for line in user_info.readlines()[3:]:
                line = line.strip()
                user_info_row = line.split('\t')
                dns.append(user_info_row[0])
                id_list.append(user_info_row[1])
                pw_list.append(user_info_row[2])
                row_len = cnt
                cnt = cnt + 1

            df_user_info = pd.DataFrame({'사이트':dns, 'ID':id_list, 'PW':pw_list})
            if row_len == 0:        #저장된 사이트가 없을 시 임시 코드
                clear()
                print('저장된 사이트가 없습니다.')
                print('새로운 사이트를 추가해주세요.')
                sleep(2)
                mm.main_menu(user_id)
                
            for i in range(row_len):
                print('{}. {}'.format(i+1, df_user_info['사이트'][i]))
            try:
                site = input('\nPW를 확인하고자 하는 사이트의 번호 또는 DNS를 입력해주세요: ')
                if site.isnumeric():
                    site = int(site)
                    if 0 < site <= row_len:
                        clear()
                        print("ID는 {}".format(df_user_info['ID'][site-1]))
                        print("PW는 {}".format(df_user_info['PW'][site-1]))
                        print("입니다.")
                        print("아무키나 누르면 메인화면으로 돌아갑니다.")
                        getch()
                        clear()
                        mm.main_menu(user_id)
                    else:
                        clear()
                        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                        sleep(2)
                        clear()
                        continue
                else:
                    clear()
                    for i in range(row_len):
                        if site == df_user_info['사이트'][i]:
                            print("ID는 {}".format(df_user_info['ID'][i]))
                            print("PW는 {}".format(df_user_info['PW'][i]))
                            print("입니다.")
                            print("아무키나 누르면 메인화면으로 돌아갑니다.")
                            getch()
                            clear()
                            mm.main_menu(user_id)
                    else:
                        clear()
                        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                        sleep(2)
                        clear()
                        continue
                    
            except ValueError:
                if site == "":
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
