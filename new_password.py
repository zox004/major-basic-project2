import os
clear = lambda : os.system('cls')
from time import sleep 
import main_menu as mm

def new_password(user_existing_id) :
    password_conditions = ["N", "N", "N", "N", 0] # PW 조건 디폴트 값 
    clear()
    while True :
        print("새로운 사이트의 DNS(이름)를 입력해주세요.")
        DNS = input("DNS : ")
        if(DNS==""):
            clear()
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            clear()
            continue
        elif (DNS.count(" ")>0):
            clear()
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
            sleep(2)
            clear()
            continue
        else:
            clear()
            break
    
    
    password_conditions_load(DNS, password_conditions, user_existing_id)


    print("새로운 사이트의 PW조건을 입력해주세요.")
    print("PW 에 탭은 들어갈 수 없습니다.")

    while True :
        special_character = input("PW 조건(특수문자 여부 -> Y/N) : ")
        if(special_character==""):
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            continue
        if(special_character == "Y" or special_character == "N"):
            if(special_character == "Y"):
                password_conditions[0] = "Y"
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
                password_conditions[1] = "Y"
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
                password_conditions[2] = "Y"
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
                password_conditions[3] = "Y"
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
            password_conditions[4] = minimum_number
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

    user_info = open("Data\\{}.txt".format(user_existing_id), "a", encoding='utf8')

    #============================================================================
    # 수정1 - 입력받은 조건들을 출력해줍니다
    clear()
    print("========비밀번호 규칙========")
    print("특수문자 사용 여부 : {} ".format(password_conditions[0]))
    print("숫자 사용 여부 : {} ".format(password_conditions[1]))
    print("대문자 사용 여부 : {} ".format(password_conditions[2]))
    print("소문자 사용 여부 : {} ".format(password_conditions[3]))
    print("최소자릿수-숫자 : {} ".format(password_conditions[4]))
    print("============================")
    #============================================================================
    print("<새로운 Password 등록>")
    print("사이트명 : {}".format(DNS))

    while True :
        #clear()
        site_new_id = input("ID : ")
        if (site_new_id == ""):
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            continue
        elif(site_new_id.count(" ")>0):
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
            continue
        elif(not site_new_id.isalnum()):
            print("특수문자를 포함하고 있습니다.")
            sleep(2)
            continue
        else:
            break

    while True :
        #clear() 

        site_new_password = input("PW : ")

        if (site_new_password ==""):
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            continue
        elif (site_new_password.count(" ")>0):
            print("올바른 입력이 아닙니다. 다시 입력해주세요")
            sleep(2)
            continue

        # 특수문자 검사 
        if(password_conditions[0]=="Y"):
            if(site_new_password.isalnum()):
                print("올바른 입력이 아닙니다. 다시 입력해주세요")
                sleep(2)
                continue
        else:
            if(not site_new_password.isalnum()):
                print("올바른 입력이 아닙니다. 다시 입력해주세요")
                sleep(2)
                continue
        
        # 숫자 검사
        number_count = 0
        if(password_conditions[1]=="Y"):
            for i in site_new_password: 
                if 48<=ord(i)<=57 :
                    number_count += 1
            if number_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue                
        else:
            for i in site_new_password: 
                if 48<=ord(i)<=57 :
                    number_count += 1
            if number_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue


        # 대문자 검사
        big_count = 0
        if(password_conditions[2]=="Y"):
            for i in site_new_password: 
                if 65<=ord(i)<=90 :
                    big_count += 1
            if big_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue                
        else:
            for i in site_new_password: 
                if 65<=ord(i)<=90 :
                    big_count += 1
            if big_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        
        # 소문자 검사
        small_count = 0
        if(password_conditions[3]=="Y"):
            for i in site_new_password: 
                if 97<=ord(i)<=122 :
                    small_count += 1
            if small_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        else:
            for i in site_new_password: 
                if 97<=ord(i)<=122 :
                    small_count += 1
            if small_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        
        # 최소 자릿수 검사 
        if(len(site_new_password) < password_conditions[4]) :
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
            sleep(2)
            continue


        break

    user_info.write("{}\t".format(DNS))
    user_info.write("{}\t".format(site_new_id))
    user_info.write("{}\n".format(site_new_password))
    # password_conditions_string = ','.join(password_conditions)
    # user_info.write("{}".format(password_conditions))
    # for index, i in enumerate(password_conditions):
    #     if index == 4:
    #         user_info.write("{}".format(i))
    #         break
    #     user_info.write("{}\t".format(i))
    # print("", file=user_info)

    #=================================================
    pw_condition_file = open("Data\\pw_conditions.txt", "a", encoding='utf8')
    pw_condition_file.write("{}\t".format(DNS))
    for index, i in enumerate(password_conditions):
        if index == 4:
            pw_condition_file.write("{}".format(i))
            break
        pw_condition_file.write("{}\t".format(i))
    print("", file=pw_condition_file)
    pw_condition_file.close()
    #=================================================

    user_info.close()
    mm.main_menu(user_existing_id)






def password_conditions_load(DNS, password_conditions, user_existing_id):
    lines=[]
    try:
        pw_condition_file = open("Data\\pw_conditions.txt", "r+", encoding='utf8')
    except FileNotFoundError:
        pw_condition_file = open("pw_conditions.txt", "w", encoding='utf8')
        pw_condition_file.close()
        import shutil 
        filename = 'pw_conditions.txt'
        src = '' 
        dir = 'Data\\' 
        shutil.move(src + filename, dir + filename)
        pw_condition_file = open("Data\\pw_conditions.txt", "r+", encoding='utf8')
        #new_password(user_existing_id)
    str=' '
    str_list = []
    cnt = 0
    number = ''
    while str != '' :
        str = pw_condition_file.readline() 
        str_list.append(str) # str_list[0] 자리에 들어감?
        if DNS in str :
            clear()
            print("해당 DNS의 정보가 존재합니다.")
            lines = str.split("\t")
            print("DNS 이름 : {}".format(lines[0]))
            print("특수문자 사용 여부 : {}".format(lines[1]))
            print("숫자 사용 여부 : {}".format(lines[2]))
            print("대문자 사용 여부 : {}".format(lines[3]))
            print("소문자 사용 여부 : {}".format(lines[4]))
            print("최소 자릿수-숫자 : {}".format(lines[5]))
            print("====================================")
            number = input("1)해당 조건 사용 2)조건 수정 후 사용\n 원하시는 번호를 입력하세요 : ")
            if number == '':
                clear()
                print("입력된 값이 없습니다. 다시 입력해주세요.")
                sleep(2)
                clear()
            
            elif number == '1':
                password_conditions[0] = lines[1]
                password_conditions[1] = lines[2]
                password_conditions[2] = lines[3]
                password_conditions[3] = lines[4]
                password_conditions[4] = lines[5]
                
                print("========비밀번호 규칙========")
                print("특수문자 사용 여부 : {} ".format(password_conditions[0]))
                print("숫자 사용 여부 : {} ".format(password_conditions[1]))
                print("대문자 사용 여부 : {} ".format(password_conditions[2]))
                print("소문자 사용 여부 : {} ".format(password_conditions[3]))
                print("최소자릿수-숫자 : {} ".format(password_conditions[4]))
                print("============================")

                
            elif number == '2':

                '''
                1. 조건들 input으로 받아서 list 에 저장 
                2. list 형식에 맞춰서 string 으로 바꾸고 str_tmp 에 저장.. 
                3. str_list[-1] = str_tmp
                4. str_list 를 write 해서 입력.. 
                '''
                condition_list = ["N","N","N","N",0]   
                while True:
                    special_character = input("PW 조건(특수문자 여부 -> Y/N) : ")
                    if(special_character==""):
                        print("입력된 값이 없습니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                    if(special_character == "Y" or special_character == "N"):
                        if(special_character == "Y"):
                            condition_list[0] = "Y"
                            break
                        else :
                            break
                    else :
                        print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                while True :
                    number2 = input("PW 조건(숫자 여부 -> Y/N) : ")
                    if(number2==""):
                        print("입력된 값이 없습니다. 다시 입력해주세요.")
                        sleep(2)
                        continue
                    if(number2 == "Y" or number2 == "N"):
                        if(number2 == "Y"):
                            condition_list[1] = "Y"
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
                            condition_list[2] = "Y"
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
                            condition_list[3] = "Y"
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
                        condition_list[4] = minimum_number
                        minimum_number = int(minimum_number)
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
                
                str_temp = DNS+'\t' +'\t'.join(condition_list)
                str_temp += '\n'
                str_list[cnt] = str_temp
            
            else:
                clear()
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                clear()    
        cnt+=1
    
    pw_condition_file.close()
    if number == '1':
        new_password_not_modify(password_conditions, DNS, user_existing_id)
    elif number == '2':
        pw_condition_file = open("Data\\pw_conditions.txt", "w", encoding='utf8')
        pw_condition_file.writelines(str_list)
        pw_condition_file.close()
        new_password_modify(condition_list, DNS, user_existing_id)
        
    
    print("해당 DNS의 등록된 정보가 없습니다. 새롭게 등록합니다.")
    
def new_password_modify(condition_list, DNS, user_existing_id):
    user_info = open("Data\\{}.txt".format(user_existing_id), "a", encoding='utf8')

    while True :
    #clear()
        site_new_id = input("ID : ")
        if (site_new_id == ""):
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            continue
        elif(site_new_id.count(" ")>0):
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
            continue
        elif(not site_new_id.isalnum()):
            print("특수문자를 포함하고 있습니다.")
            sleep(2)
            continue
        else:
            break

    while True :
        #clear() 

        site_new_password = input("PW : ")

        if (site_new_password ==""):
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            continue
        elif (site_new_password.count(" ")>0):
            print("올바른 입력이 아닙니다. 다시 입력해주세요")
            sleep(2)
            continue

        # 특수문자 검사 
        if(condition_list[0]=="Y"):
            if(site_new_password.isalnum()):
                print("올바른 입력이 아닙니다. 다시 입력해주세요")
                sleep(2)
                continue
        else:
            if(not site_new_password.isalnum()):
                print("올바른 입력이 아닙니다. 다시 입력해주세요")
                sleep(2)
                continue
        
        # 숫자 검사
        number_count = 0
        if(condition_list[1]=="Y"):
            for i in site_new_password: 
                if 48<=ord(i)<=57 :
                    number_count += 1
            if number_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue                
        else:
            for i in site_new_password: 
                if 48<=ord(i)<=57 :
                    number_count += 1
            if number_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue


        # 대문자 검사
        big_count = 0
        if(condition_list[2]=="Y"):
            for i in site_new_password: 
                if 65<=ord(i)<=90 :
                    big_count += 1
            if big_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue                
        else:
            for i in site_new_password: 
                if 65<=ord(i)<=90 :
                    big_count += 1
            if big_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        
        # 소문자 검사
        small_count = 0
        if(condition_list[3]=="Y"):
            for i in site_new_password: 
                if 97<=ord(i)<=122 :
                    small_count += 1
            if small_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        else:
            for i in site_new_password: 
                if 97<=ord(i)<=122 :
                    small_count += 1
            if small_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        
        # 최소 자릿수 검사 
        if(len(site_new_password) < int(condition_list[4])) :
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
            sleep(2)
            continue


        break

    user_info.write("{}\t".format(DNS))
    user_info.write("{}\t".format(site_new_id))
    user_info.write("{}\n".format(site_new_password))
    # password_conditions_string = ','.join(password_conditions)
    # user_info.write("{}".format(password_conditions))
    # for index, i in enumerate(condition_list):
    #     if index == 4:
    #         user_info.write("{}".format(i))
    #         break
    #     user_info.write("{}\t".format(i))
    print("", file=user_info)

    user_info.close()
    clear()
    mm.main_menu(id)


def new_password_not_modify(password_conditions, DNS, user_existing_id):

    user_info = open("Data\\{}.txt".format(user_existing_id), "a", encoding='utf8')

    while True :
    #clear()
        site_new_id = input("ID : ")
        if (site_new_id == ""):
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            continue
        elif(site_new_id.count(" ")>0):
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
            continue
        elif(not site_new_id.isalnum()):
            print("특수문자를 포함하고 있습니다.")
            sleep(2)
            continue
        else:
            break

    while True :
        #clear() 

        site_new_password = input("PW : ")

        if (site_new_password ==""):
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            continue
        elif (site_new_password.count(" ")>0):
            print("올바른 입력이 아닙니다. 다시 입력해주세요")
            sleep(2)
            continue

        # 특수문자 검사 
        if(password_conditions[0]=="Y"):
            if(site_new_password.isalnum()):
                print("올바른 입력이 아닙니다. 다시 입력해주세요")
                sleep(2)
                continue
        else:
            if(not site_new_password.isalnum()):
                print("올바른 입력이 아닙니다. 다시 입력해주세요")
                sleep(2)
                continue
        
        # 숫자 검사
        number_count = 0
        if(password_conditions[1]=="Y"):
            for i in site_new_password: 
                if 48<=ord(i)<=57 :
                    number_count += 1
            if number_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue                
        else:
            for i in site_new_password: 
                if 48<=ord(i)<=57 :
                    number_count += 1
            if number_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue


        # 대문자 검사
        big_count = 0
        if(password_conditions[2]=="Y"):
            for i in site_new_password: 
                if 65<=ord(i)<=90 :
                    big_count += 1
            if big_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue                
        else:
            for i in site_new_password: 
                if 65<=ord(i)<=90 :
                    big_count += 1
            if big_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        
        # 소문자 검사
        small_count = 0
        if(password_conditions[3]=="Y"):
            for i in site_new_password: 
                if 97<=ord(i)<=122 :
                    small_count += 1
            if small_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        else:
            for i in site_new_password: 
                if 97<=ord(i)<=122 :
                    small_count += 1
            if small_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        
        # 최소 자릿수 검사 
        if(len(site_new_password) < int(password_conditions[4])) :
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
            sleep(2)
            continue


        break

    user_info.write("{}\t".format(DNS))
    user_info.write("{}\t".format(site_new_id))
    user_info.write("{}\n".format(site_new_password))
    # password_conditions_string = ','.join(password_conditions)
    # user_info.write("{}".format(password_conditions))
    # for index, i in enumerate(password_conditions):
    #     if index == 4:
    #         user_info.write("{}".format(i))
    #         break
    #     user_info.write("{}\t".format(i))
    print("", file=user_info)

    user_info.close()
    clear()
    mm.main_menu(user_existing_id)
