import os
import shutil

folder_path = "C:/Users/302/Documents/새 폴더/data/dogs-vs-cats/train" # C:\Users\302\Documents\새 폴더\data\dogs-vs-cats\train

#print('os 모듈 = ', os.getcwd())

def create_folder(folder_name):
    os.makedirs(os.path.join(folder_path,folder_name),exist_ok=True)


def sort_files():
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