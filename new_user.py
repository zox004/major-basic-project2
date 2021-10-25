import os
clear = lambda : os.system('cls')
from time import sleep
import start_menu as sm

def new_user():
    while(True):
        
        print("<조건>\nID 및 PW는 4~10자로 입력하시길 바랍니다.\n")
        new_id = input("New ID : ")

        #============ ID 문법 규칙 검사 ==============
        for i in new_id:
            if (not 48<=ord(i)<=57) and (not 65<=ord(i)<=90) and (not 97<=ord(i)<=122) :
                clear()
                print("조건에 맞지 않거나 틀린 형식입니다.")
                print("다시 입력 하세요.\n")
                sleep(2)
                new_user()
        #===========================================


        #============ 기존 사용자 검색 ==============
        path = "Data"
        userinfo_list = os.listdir(path) # 해당 디렉토리의 모든 파일을 리스트로 받음
        #===========================================

        if ("{}.txt".format(new_id) in userinfo_list): # 리스트의 특정 파일 검색 (기존ID)
            clear()
            print("이미 가입된 ID 입니다.\n초기 화면으로 돌아갑니다.")
            sleep(2)
            clear()
            continue

        elif(len(new_id)<4 or len(new_id)>10):
            clear()
            print("조건에 맞지 않거나 틀린 형식입니다.")
            print("다시 입력 하세요.\n")
            sleep(2)
            continue

        else: # 모든 오류 통과 시 파일 생성 및 저장 
            new_info = open('{}.txt'.format(new_id), "w", encoding="utf8")
            new_info.close()

        new_pw = input("New PW : ")

        #============ PW 문법 규칙 검사 ==============
        for i in new_pw:
            if (not 48<=ord(i)<=57) and (not 65<=ord(i)<=90) and (not 97<=ord(i)<=122) :
                clear()
                print("조건에 맞지 않거나 틀린 형식입니다.")
                print("다시 입력 하세요.\n")
                sleep(2)
                new_user()
        #===========================================

        if(len(new_pw)<4 or len(new_pw)>10):
            clear()
            print("조건에 맞지 않거나 틀린 형식입니다.")
            print("다시 입력 하세요.\n")
            os.remove("{}.txt".format(new_id))
            sleep(2)
            continue
        else:
            new_info = open("{}.txt".format(new_id), "a", encoding="utf8")
            print("{}".format(new_pw), file=new_info)


        while True:
            hint_question = input("힌트 질문 : ")
            if str.isspace(hint_question) :
                print("조건에 맞지 않거나 틀린 형식입니다.")
                print("다시 입력 하세요.\n")
                sleep(2)
                continue
            else :
                print("{}".format(hint_question), file=new_info)
            hint_answer = input("힌트 답 : ")
            if str.isspace(hint_answer) :
                print("조건에 맞지 않거나 틀린 형식입니다.")
                print("다시 입력 하세요.\n")
                sleep(2)
                continue
            else :
                print("{}".format(hint_answer), file=new_info)
                break

        new_info.close()

        # 최종적으로 저장된 ID 텍스트 파일은 특정 지정폴더로 이동합니다
        # src : 이동 전 디렉토리 , dir : 이동 후 디렉토리
        # 해당 디렉토리를 사용자 워크스페이스에 맞춰서 변경해야 합니다.
        #================ 파일 경로 변경 ================
        import shutil 
        filename = '{}.txt'.format(new_id) 
        src = 'C:\\Users\\sinkyu\\Desktop\\PythonWorkspace\\basic_project\\' 
        dir = 'C:\\Users\\sinkyu\\Desktop\\PythonWorkspace\\basic_project\\Data\\' 
        shutil.move(src + filename, dir + filename)
        #===============================================

        break

    clear()
    sm.start_menu()
