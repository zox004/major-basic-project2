import os
from time import sleep
import pandas as pd
import main_menu as mm
from msvcrt import getch

clear = lambda : os.system('cls')

def remove_password(user_id):
    clear()
    while True:
        print('저장된 사이트 리스트')
        with open("Data\\"+user_id+".txt", "r", encoding='utf8') as user_info:
            new_text_content = ''
            for line in user_info.readlines()[:3]:
                new_text_content += line    

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
            site = input('\nPW를 삭제하고자 하는 사이트의 번호 또는 DNS를 입력해주세요: ')
            if site.isnumeric():
                site = int(site)
                if 0 < site <= row_len:
                    clear()
                    df_user_info = df_user_info.drop([site-1])
                    for i in range(row_len):
                        if i==site-1:
                            continue
                        new_line = "{}\t{}\t{}".format(df_user_info['사이트'][i],df_user_info['ID'][i],df_user_info["PW"][i])
                        new_text_content += new_line + '\n'
                    with open("Data\\"+user_id+".txt", "w", encoding='utf8') as user_info:
                        user_info.write(new_text_content)
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
                        site_index = df_user_info.index[df_user_info['사이트']==site].tolist()
                        df_user_info = df_user_info.drop([site_index[0]])
                        for i in range(row_len):
                            if i==site_index[0]:
                                continue
                            new_line = "{}\t{}\t{}".format(df_user_info['사이트'][i],df_user_info['ID'][i],df_user_info["PW"][i])
                            new_text_content += new_line + '\n'
                        with open("Data\\"+user_id+".txt", "w", encoding='utf8') as user_info:
                            user_info.write(new_text_content)
                        clear()
                        mm.main_menu(user_id)
                
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
