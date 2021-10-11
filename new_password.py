import os
clear = lambda : os.system('cls')
from time import sleep

def new_password(id) :
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
        

    print("새로운 사이트의 PW조건을 입력해주세요.")

    password_conditions = ["N", "N", "N", "N", "N"] # PW 조건 디폴트 값 
    print("PW 에 콤마는 들어갈 수 없습니다.")

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
        minimum_number = input("PW 조건(최소자릿수-숫자 여부 -> Y/N) : ")
        if(minimum_number==""):
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            continue
        if(minimum_number == "Y" or minimum_number == "N"):
            if(minimum_number == "Y"):
                password_conditions[4] = "Y"
                break
            else :
                break
        else :
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
            sleep(2)
            continue


    user_info = open("Data\\"+id+'.txt', "a", encoding='utf8')

    print("<새로운 Password 등록>")
    print("사이트명 : {}".format(DNS))


    while True :
        clear()
        site_id = input("ID : ")
        if (site_id == ""):
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            continue
        elif(site_id.count(" ")>0):
            print("올바른 입력이 아닙니다. 다시 입력해주세요.")
            continue
        elif(not site_id.isalnum()):
            print("특수문자를 포함하고 있습니다.")
            sleep(2)
            continue
        else:
            break




    while True :
        clear() 

        print("특수문자 포함 여부 : {}".format(password_conditions[0]))
        print("숫자 포함 여부 : {}".format(password_conditions[1]))
        print("대문자 포함 여부 : {}".format(password_conditions[2]))
        print("소문자 포함 여부 : {}".format(password_conditions[3]))


        site_password = input("PW : ")

        if (site_password ==""):
            print("입력된 값이 없습니다. 다시 입력해주세요.")
            sleep(2)
            continue
        elif (site_password.count(" ")>0):
            print("올바른 입력이 아닙니다. 다시 입력해주세요")
            sleep(2)
            continue

        # 특수문자 검사 
        if(password_conditions[0]=="Y"):
            if(site_password.isalnum()):
                print("올바른 입력이 아닙니다. 다시 입력해주세요")
                sleep(2)
                continue
        else:
            if(not site_password.isalnum()):
                print("올바른 입력이 아닙니다. 다시 입력해주세요")
                sleep(2)
                continue
        
        # 숫자 검사
        number_count = 0
        if(password_conditions[1]=="Y"):
            for i in site_password: 
                if 48<=ord(i)<=57 :
                    number_count += 1
            if number_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue                
        else:
            for i in site_password: 
                if 48<=ord(i)<=57 :
                    number_count += 1
            if number_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue


        # 대문자 검사
        big_count = 0
        if(password_conditions[2]=="Y"):
            for i in site_password: 
                if 65<=ord(i)<=90 :
                    big_count += 1
            if big_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue                
        else:
            for i in site_password: 
                if 65<=ord(i)<=90 :
                    big_count += 1
            if big_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        
        # 소문자 검사
        small_count = 0
        if(password_conditions[3]=="Y"):
            for i in site_password: 
                if 97<=ord(i)<=122 :
                    small_count += 1
            if small_count == 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        else:
            for i in site_password: 
                if 97<=ord(i)<=122 :
                    small_count += 1
            if small_count > 0 :
                print("올바른 입력이 아닙니다. 다시 입력해주세요.")
                sleep(2)
                continue
        
        # 최소 자릿수 검사 
        
        break

    user_info.write("{} , ".format(DNS))
    user_info.write("{} , ".format(site_id))
    user_info.write("{} , ".format(site_password))
    # password_conditions_string = ','.join(password_conditions)
    # user_info.write("{}".format(password_conditions))
    for index, i in enumerate(password_conditions):
        if index == 4:
            user_info.write(i)
            break
        user_info.write("{} , ".format(i))
    print("", file=user_info)

    user_info.close()
