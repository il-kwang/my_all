import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)  # 재현성 확보

# 생성할 샘플 수 (예: 1000행)
n = 50000

# 2022-01-01 하루 동안의 탑승 시간 생성 (랜덤한 분 단위)
pickup_times = [datetime(2022, 1, 1) + timedelta(minutes=np.random.randint(0, 1440)) for _ in range(n)]
pickup_times = pd.to_datetime(pickup_times)

# 하차 시간: 탑승 시간보다 5분 ~ 60분 후로 설정
dropoff_times = [pt + timedelta(minutes=np.random.randint(5, 61)) for pt in pickup_times]
dropoff_times = pd.to_datetime(dropoff_times)

# 대전 중심: 대략 위도 36.35, 경도 127.38
# 탑승 위치: 대전 주변에서 무작위로 생성 (예: 위도 36.30~36.40, 경도 127.30~127.45)
pickup_lat = np.random.uniform(36.30, 36.40, n)
pickup_lon = np.random.uniform(127.30, 127.45, n)

# 하차 위치: 탑승 위치에서 약간의 오프셋을 주어 생성
# 오프셋은 -0.02 ~ 0.02 (위도), -0.03 ~ 0.03 (경도) 범위 내에서 무작위로
dropoff_lat = pickup_lat + np.random.uniform(-0.02, 0.02, n)
dropoff_lon = pickup_lon + np.random.uniform(-0.03, 0.03, n)

# 탑승 인원: 1~4명 무작위 정수
passenger_count = np.random.randint(1, 5, n)

# 이동 거리 계산 (간단한 유클리드 거리, 단위: km)
# 대략 1도 위도 ≒ 111km, 1도 경도 ≒ 85km (대전 근처)
lat_diff = dropoff_lat - pickup_lat
lon_diff = dropoff_lon - pickup_lon
distance = np.sqrt((lat_diff * 111)**2 + (lon_diff * 85)**2)  # km 단위

# 요금 계산: 기본 요금 + 이동 거리당 요금 + 약간의 잡음 (선형 관계 유지)
base_fare = 3000    # 기본 요금 (원)
rate = 1000         # km당 추가 요금 (원)
noise = np.random.normal(0, 200, n)  # 약간의 노이즈
fare_amount = base_fare + rate * distance + noise
fare_amount = np.round(fare_amount, 0)

# DataFrame 생성
df = pd.DataFrame({
    'pickup_datetime': pickup_times,
    'dropoff_datetime': dropoff_times,
    'pickup_longitude': pickup_lon,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_lon,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': passenger_count,
    'fare_amount': fare_amount
})

# CSV 파일로 저장
csv_filename = "synthetic_taxi_data_daejeon.csv"
df.to_csv(csv_filename, index=False)

print("Synthetic taxi data saved as", csv_filename)