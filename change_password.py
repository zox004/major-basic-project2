import os
from time import sleep
import pandas as pd
import main_menu as mm

clear = lambda : os.system('cls')

#레코드를 dataframe으로 바꿔주는 함수
def text2dataframe(user_info):

    dns = []
    condition1 = []
    condition2 = []
    condition3 = []
    condition4 = []
    condition5 = []
    cnt = 1

    for line in user_info.readlines()[:]:
        line = line.strip()
        user_info_row = line.split('\t')
        dns.append(user_info_row[0])
        condition1.append(user_info_row[1])
        condition2.append(user_info_row[2])
        condition3.append(user_info_row[3])
        condition4.append(user_info_row[4])
        condition5.append(user_info_row[5])
        row_len = cnt
        cnt = cnt + 1

    df_user_info = pd.DataFrame({'사이트':dns, 'condition1':condition1, 'condition2':condition2,
                                'condition3':condition3, 'condition4':condition4, 'condition5':condition5})
    return row_len, df_user_info
    

def change_password(existing_user_id):
    while True:
        print('저장된 사이트 리스트')
        user_info = open("Data\\pw_conditions.txt", "r", encoding='utf8')
        row_len, df_user_info = text2dataframe(user_info)
        user_info.close()

        
        for i in range(row_len):
            print('{}. {}'.format(i+1, df_user_info['사이트'][i]))
        try:
            with open("Data\\"+existing_user_id+".txt", "r", encoding='utf8') as user_info:
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

                df_user_info2 = pd.DataFrame({'사이트':dns, 'ID':id_list, 'PW':pw_list})
            num = input('\nPW를 변경하고자 하는 사이트의 번호 또는 DNS를 입력해주세요: ')
            num = int(num)
            if 0 < num <= row_len:
                clear()
                print("사이트 : {}".format(df_user_info['사이트'][num-1]))
                print("<변경 전>")
                print("PW 에 탭은 들어갈 수 없습니다.")
                print("PW 조건(특수문자 여부 -> Y/N) : {}".format(df_user_info['condition1'][num-1]))
                print("PW 조건(숫자 여부 -> Y/N) : {}".format(df_user_info['condition2'][num-1]))
                print("PW 조건(대문자 여부 -> Y/N) : {}".format(df_user_info['condition3'][num-1]))
                print("PW 조건(소문자 여부 -> Y/N) : {}".format(df_user_info['condition4'][num-1]))
                print("PW 조건(최소자릿수-숫자) : {}\n".format(df_user_info['condition5'][num-1]))
                print("PW : {}\n".format(df_user_info2['PW'][num-1]))

                print("********************************\n")

                print("<변경 후>")
                print("PW 에 탭은 들어갈 수 없습니다.")
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
                    try:
                        minimum_number = input("PW 조건(최소자릿수-숫자) : ")
                        minimum_number = int(minimum_number)
                        df_user_info['condition5'][num-1] = minimum_number
                        break
                    except ValueError:
                        if minimum_number == "" : # 입력받은 값이 없을 경우 ..
                            clear()
                            print("입력된 값이 없습니다. 다시 입력해주세요.")
                            sleep(2)
                            clear()
                            continue
                        else: # 공백처리 문자열처리 .. 
                            clear()
                            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                            sleep(2)
                            clear()
                            continue

                while True :
                    clear() 

                    new_pw = input("PW : ")

                    if (new_pw ==""):
                        print("입력된 값이 없습니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                    elif (new_pw.count(" ")>0):
                        print("올바른 입력이 아닙니다. 다시 입력해주세요")
                        sleep(2)
                        continue

                    # 특수문자 검사
                    if(df_user_info['condition1'][num-1]=="Y"):
                        if(new_pw.isalnum()):
                            print("올바른 입력이 아닙니다. 다시 입력해주세요")
                            sleep(2)
                            continue
                    else:
                        if(not new_pw.isalnum()):
                            print("올바른 입력이 아닙니다. 다시 입력해주세요")
                            sleep(2)
                            continue
                    
                    # 숫자 검사
                    number_count = 0
                    if(df_user_info['condition2'][num-1]=="Y"):
                        for i in new_pw: 
                            if 48<=ord(i)<=57 :
                                number_count += 1
                        if number_count == 0 :
                            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                            sleep(2)
                            continue                
                    else:
                        for i in new_pw: 
                            if 48<=ord(i)<=57 :
                                number_count += 1
                        if number_count > 0 :
                            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                            sleep(2)
                            continue


                    # 대문자 검사
                    big_count = 0
                    if(df_user_info['condition3'][num-1]=="Y"):
                        for i in new_pw: 
                            if 65<=ord(i)<=90 :
                                big_count += 1
                        if big_count == 0 :
                            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                            sleep(2)
                            continue                
                    else:
                        for i in new_pw: 
                            if 65<=ord(i)<=90 :
                                big_count += 1
                        if big_count > 0 :
                            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                            sleep(2)
                            continue
                    
                    # 소문자 검사
                    small_count = 0
                    if(df_user_info['condition4'][num-1]=="Y"):
                        for i in new_pw: 
                            if 97<=ord(i)<=122 :
                                small_count += 1
                        if small_count == 0 :
                            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                            sleep(2)
                            continue
                    else:
                        for i in new_pw: 
                            if 97<=ord(i)<=122 :
                                small_count += 1
                        if small_count > 0 :
                            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                            sleep(2)
                            continue
                    
                    # 최소 자릿수 검사 
                    if(len(new_pw) < df_user_info['condition5'][num-1]) :
                        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                    df_user_info2['PW'][num-1] = new_pw
                    break
                
                #변경된 레코드 수정
                with open("Data\\"+existing_user_id+".txt", "r", encoding='utf8') as user_info:
                    lines = user_info.readlines()
                    new_text_content = ''
                    for i, line in enumerate(lines):
                        if i == num-1+3:        #num-1
                            new_line = "{}\t{}\t{}".format(df_user_info2['사이트'][num-1],df_user_info2['ID'][num-1],df_user_info2["PW"][num-1])
                        else:
                            new_line = line.strip()
                        new_text_content += new_line + '\n'
                with open("Data\\"+existing_user_id+".txt", "w", encoding='utf8') as user_info:
                    user_info.write(new_text_content)
                clear()
                mm.main_menu(existing_user_id)
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
