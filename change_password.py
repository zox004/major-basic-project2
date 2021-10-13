import os
from time import sleep
import pandas as pd
import main_menu as mm

clear = lambda : os.system('cls')

def text2dataframe(user_info):
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
    return row_len, df_user_info
    
def change_password(id):
    while True:
        print('저장된 사이트 리스트')
        user_info = open("Data\\"+id+".txt", "r", encoding='utf8')
        row_len, df_user_info = text2dataframe(user_info)
        user_info.close()
        
        for i in range(row_len):
            print('{}. {}'.format(i+1, df_user_info['사이트'][i]))
        try:
            num = input('\nPW를 변경하고자 하는 사이트의 번호를 입력해주세요: ')
            num = int(num)
            if 0 < num <= row_len:
                clear()
                print("사이트 : {}".format(df_user_info['사이트'][num-1]))
                print("<변경 전>")
                print("PW 에 콤마는 들어갈 수 없습니다.")
                print("PW 조건(특수문자 여부 -> Y/N) : {}".format(df_user_info['condition1'][num-1]))
                print("PW 조건(특수문자 여부 -> Y/N) : {}".format(df_user_info['condition2'][num-1]))
                print("PW 조건(특수문자 여부 -> Y/N) : {}".format(df_user_info['condition3'][num-1]))
                print("PW 조건(특수문자 여부 -> Y/N) : {}".format(df_user_info['condition4'][num-1]))
                print("PW 조건(특수문자 여부 -> 숫자) : {}\n".format(df_user_info['condition5'][num-1]))
                print("PW : {}\n".format(df_user_info['PW'][num-1]))

                print("********************************\n")

                print("<변경 후>")
                print("PW 에 콤마는 들어갈 수 없습니다.")
                while True :
                    special_character = input("PW 조건(특수문자 여부 -> Y/N) : ")
                    if(special_character==""):
                        print("입력된 값이 없습니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                    if(special_character == "Y" or special_character == "N"):
                        if(special_character == "Y"):
                            df_user_info['condition1'][num-1] = "Y"
                            break
                        elif special_character == "N":
                            df_user_info['condition1'][num-1] = "N"
                            break
                        else :
                            break
                    else :
                        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                        sleep(2)
                        continue

                while True :
                    number = input("PW 조건(숫자 여부 -> Y/N) : ")
                    if(number==""):
                        print("입력된 값이 없습니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                    if(number == "Y" or number == "N"):
                        if(number == "Y"):
                            df_user_info['condition2'][num-1] = "Y"
                            break
                        elif number =="N":
                            df_user_info['condition2'][num-1] = "N"
                            break
                        else :
                            break
                    else :
                        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                        sleep(2)
                        continue

                while True :
                    big_letter = input("PW 조건(대문자 여부 -> Y/N) : ")
                    if(big_letter==""):
                        print("입력된 값이 없습니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                    if(big_letter == "Y" or big_letter == "N"):
                        if(big_letter == "Y"):
                            df_user_info['condition3'][num-1] = "Y"
                            break
                        elif big_letter == "N":
                            df_user_info['condition3'][num-1] = "N"
                            break
                        else :
                            break
                    else :
                        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                        sleep(2)
                        continue

                while True :
                    small_letter = input("PW 조건(소문자 여부 -> Y/N) : ")
                    if(small_letter==""):
                        print("입력된 값이 없습니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                    if(small_letter == "Y" or small_letter == "N"):
                        if(small_letter == "Y"):
                            df_user_info['condition4'][num-1] = "Y"
                            break
                        elif small_letter == "N":
                            df_user_info['condition4'][num-1] = "N"
                            break
                        else :
                            break
                    else :
                        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                        sleep(2)
                        continue

                while True :
                    minimum_number = input("PW 조건(최소자릿수-숫자) : ")
                    if(minimum_number==""):
                        print("입력된 값이 없습니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                    if(minimum_number == "Y" or minimum_number == "N"):
                        if(minimum_number == "Y"):
                            df_user_info['condition5'][num-1] = "Y"
                            break
                        elif minimum_number == "N":
                            df_user_info['condition5'][num-1] = "N"
                            break
                        else :
                            break
                    else :
                        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                while True :
                    new_pw = input("\nPW : ")
                    if(new_pw==""):
                        print("입력된 값이 없습니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                    elif new_pw:
                        df_user_info['PW'][num-1] = new_pw
                        break
                    else :
                        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                        sleep(2)
                        continue

                with open("Data\\"+id+".txt", "r", encoding='utf8') as user_info:
                    lines = user_info.readlines()
                    new_text_content = ''
                    for i, line in enumerate(lines):
                        if i == num-1+3:        #num-1
                            new_line = "{},{},{},{},{},{},{},{}".format(df_user_info['사이트'][num-1],df_user_info['ID'][num-1],df_user_info["PW"][num-1],
                                                                        df_user_info['condition1'][num-1],df_user_info['condition2'][num-1],
                                                                        df_user_info['condition3'][num-1],df_user_info['condition4'][num-1],
                                                                        df_user_info['condition5'][num-1])
                        else:
                            new_line = line.strip()
                        new_text_content += new_line + '\n'
                with open("Data\\"+id+".txt", "w", encoding='utf8') as user_info:
                    user_info.write(new_text_content)
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