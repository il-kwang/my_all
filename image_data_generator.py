import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

# 학습 데이터 폴더 경로 설정
train_dir = "C:/Users/302/Documents/new/data/dogs-vs-cats/train"
test_dir = "dataset/test"  # 테스트용 이미지 폴더

# 이미지 데이터 전처리 (학습 데이터)
train_datagen = ImageDataGenerator(rescale=1./255)  # 픽셀 값을 0~1 사이로 변환


train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),  # 모든 이미지를 150x150 크기로 변환
    batch_size=32,  # 한 번에 32장씩 불러옴
    class_mode='binary'  # 강아지 vs 고양이 (이진 분류)
)

images, labels = next(train_generator)


#샘플 이미지 확인
plt.figure(figsize=(10,5))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(images[i])  # 이미지 출력
    plt.title("Dog" if labels[i] == 1 else "Cat")  # 라벨 표시
    plt.axis('off')  # 축 제거

plt.show()



'''# 테스트 데이터 불러오기
test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary'
)
'''




'''
import os 
# 파일 경로 확인 
train_dir = "C:/Users/302/Documents/new/data/dogs-vs-cats/train"

if os.path.exists(train_dir):
    print("✅ 경로가 존재합니다!")
    print("📂 내부 폴더 목록:", os.listdir(train_dir))  # train 폴더 안의 파일/폴더 목록 출력
else:
    print("❌ 경로를 찾을 수 없습니다. 폴더 위치를 다시 확인하세요.")
'''