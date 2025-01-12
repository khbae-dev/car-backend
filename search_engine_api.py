import os
from fastapi import FastAPI
from typing import List
import pickle

# 절대 경로로 car_metadata.pkl 파일 로드
file_path = os.path.join(os.path.dirname(__file__), 'shared-data', 'car_metadata.pkl')

# 중고차 데이터 로드
with open(file_path, 'rb') as f:
    car_metadata = pickle.load(f)

# FastAPI 앱 생성
app = FastAPI()

# 메인 페이지 라우트
@app.get("/")
async def root():
    return {"message": "Welcome to the Car Search API"}

# 차량 검색 API
@app.get("/search")
async def search_cars(budget: int):
    """
    예산 이하의 차량을 검색하는 API
    - 예산(budget)은 만원 단위로 입력받음
    """
    results = [car for car in car_metadata if car['price'] <= (budget / 3)]

    if not results:
        return {"message": "No cars found within the budget"}

    return {"cars": results}