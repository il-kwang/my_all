import os
import shutil

folder_path = "C:/python_Ex/dogs-vs-cats/train" #실제 사진이 있는 폴더 경로
#print('os 모듈 = ', os.getcwd())

def create_folder(folder_name): #폴더 만들기 함수
    os.makedirs(os.path.join(folder_path,folder_name),exist_ok=True)#폴더를 지정한 이름으로 생성한다.


def sort_files():#파일을 cat, dog로 시작하는 파일을 폴더에 
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):  # 파일인지 확인
            if file.startswith("cat"):
                create_folder("cat")
                shutil.move(file_path, os.path.join(folder_path, "cat", file))
                print(f"Moved: {file} -> cat/")
            elif file.startswith("dog"):
                create_folder("dog")
                shutil.move(file_path, os.path.join(folder_path, "dog", file))
                print(f"Moved: {file} -> dog/")
 

def main():
    sort_files()
    print("📁정리 완료.")

main()